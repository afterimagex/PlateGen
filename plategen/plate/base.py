# -*- coding: utf-8 -*-
# ------------------------------------------------------------
# Copyright (C) 2020-Present, Pvening, Co.,Ltd.
#
# Licensed under the BSD 2-Clause License.
# You should have received a copy of the BSD 2-Clause License
# along with the software. If not, See,
#
#      <https://opensource.org/licenses/BSD-2-Clause>
#
# ------------------------------------------------------------

import cv2
import numpy as np

from plategen import charsets as cs
from plategen.utils import overlay_image


class Plate:
    '''
    车牌基类
    '''
    _DEFAULT_H = 0
    _DEFAULT_W = 0
    _LAYOUTS = []
    _REGULAR = []
    _BG_FILES = []
    _FG_GENERATOR = None
    _CATEGORY = None

    def __init__(self, height=140):
        super().__init__()
        self.aspect_ration = height / self._DEFAULT_H
        self.layouts = np.round(np.array(self._LAYOUTS) * self.aspect_ration).astype('int32')
        self.plate_h = int(round((self.aspect_ration * self._DEFAULT_H)))
        self.plate_w = int(round((self.aspect_ration * self._DEFAULT_W)))

    def get_random_background(self):
        image = cv2.imread(np.random.choice(self._BG_FILES))
        image = cv2.resize(image, (self.plate_w, self.plate_h))
        return image

    def get_random_foreground(self, reg, size):
        color = np.random.choice(reg[0])
        char = np.random.choice(reg[1])
        image = self._FG_GENERATOR(char, color)
        image = cv2.resize(image, size)
        return char, image

    def __len__(self):
        return 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            image = self.get_random_background()
            label = []
            for i, rect in enumerate(self.layouts):
                txt, img = self.get_random_foreground(self._REGULAR[i], (rect[2], rect[3]))
                image = overlay_image(img, image, rect)
                label.append(txt)
            return image, label, self._CATEGORY


class SinglePlate(Plate):
    '''
    单行车牌
    '''
    _DEFAULT_H = 140
    _DEFAULT_W = 440
    _LAYOUTS = [
        [15, 25, 45, 90],
        [70, 25, 45, 90],
        [162, 25, 45, 90],
        [216, 25, 45, 90],
        [270, 25, 45, 90],
        [324, 25, 45, 90],
        [378, 25, 45, 90],
    ]
    _REGULAR = [
        (['black'], cs.CHINESE_BASE),
        (['black'], cs.LETTERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
    ]


class DoublePlate(Plate):
    _DEFAULT_H = 220
    _DEFAULT_W = 440
    _LAYOUTS = [
        [110, 15, 80, 60],
        [250, 15, 80, 60],
        [28, 90, 65, 110],
        [109, 90, 65, 110],
        [190, 90, 65, 110],
        [271, 90, 65, 110],
        [352, 90, 65, 110],
    ]
    _REGULAR = [
        (['black'], cs.CHINESE_BASE),
        (['black'], cs.LETTERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
        (['black'], cs.LETTERS + cs.NUMBERS),
    ]


class RandomPlateCompose(object):
    def __init__(self, genlist):
        for g in genlist:
            assert isinstance(g, Plate)

        self._genlist = genlist

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            gen = np.random.choice(self._genlist)
            img, txt, cls = next(gen)
            return img, txt, cls

    def __iadd__(self, other):
        self._genlist += other._genlist

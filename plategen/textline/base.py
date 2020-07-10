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

from plategen.config import configurable


class TextLine:
    '''
    文本基类
    '''

    @configurable
    def __init__(self, **kwargs):
        super().__init__()

        if kwargs:
            for k, v in kwargs.items():
                if k != 'self' and not k.startswith('_'):
                    setattr(self, k, v)

        # self.aspect_ration = height / self._DEFAULT_H
        # self.layouts = np.round(np.array(self._LAYOUTS) * self.aspect_ration).astype('int32')
        # self.plate_h = int(round((self.aspect_ration * self._DEFAULT_H)))
        # self.plate_w = int(round((self.aspect_ration * self._DEFAULT_W)))

    @classmethod
    def from_config(cls, cfg):
        params = {
            'height': 0,
            'width': 0,
            'layouts': [],
            'regular': [],
            'bg': [],
        }
        params.update(cfg)
        return params

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
            bg = self.get_random_background()
            text = []
            for i, rect in enumerate(self.layouts):
                txt, img = self.get_random_foreground(self._REGULAR[i], (rect[2], rect[3]))
                bg = overlay_image(img, bg, rect)
                text.append(txt)
            return bg, text


a = TextLine({}, b=123)

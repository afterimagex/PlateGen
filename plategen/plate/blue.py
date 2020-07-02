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

import os.path as osp

import cv2

from plategen import charsets as cs
from plategen.imgen import CharsGenerator
from plategen.plate import SinglePlate, DoublePlate
from plategen.resource import resource_dir


class SingleBluePlate(SinglePlate):
    '''
    小型汽车号牌
    440mm×140mm
    蓝底白字白框线
    '''

    _REGULAR = [
        (['white'], cs.CHINESE_BASE),
        (['white'], cs.LETTERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
    ]
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_blue1.bmp'),
        osp.join(resource_dir, 'template/single_blue2.bmp'),
    ]


class DoubleBluePlate(DoublePlate):
    _REGULAR = [
        (['white'], cs.CHINESE_BASE),
        (['white'], cs.LETTERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
        (['white'], cs.LETTERS + cs.NUMBERS),
    ]
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_blue1.bmp'),
        osp.join(resource_dir, 'template/single_blue2.bmp'),
    ]


if __name__ == '__main__':
    sbp = SingleBluePlate(300)

    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

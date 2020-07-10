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

from plategen import charsets as cs
from plategen.imgen import CharsGeneratorNew
from plategen.plate import SinglePlate
from plategen.resource import resource_dir


class SingleGreenPlateA(SinglePlate):
    '''
    小型新能源汽车号牌
    480mm×140mm
    渐变绿色
    '''
    _DEFAULT_H = 140
    _DEFAULT_W = 480
    _LAYOUTS = [
        [15, 25, 45, 90],
        [69, 25, 43, 90],
        [162, 25, 43, 90],
        [214, 25, 43, 90],
        [266, 25, 43, 90],
        [318, 25, 43, 90],
        [370, 25, 43, 90],
        [422, 25, 43, 90],
    ]
    _REGULAR = SinglePlate._REGULAR + [
        (['black'], cs.LETTERS + cs.NUMBERS),
    ]
    _FG_GENERATOR = CharsGeneratorNew()
    _BG_FILES = [
        osp.join(resource_dir, 'template/green_bg_2.png')
    ]
    _CATEGORY = 'single_green_a'


class SingleGreenPlateB(SingleGreenPlateA):
    '''
    大型新能源汽车号牌
    480mm×140mm
    黄绿双拼色
    '''
    _BG_FILES = [
        osp.join(resource_dir, 'template/green_bg_1.png')
    ]
    _CATEGORY = 'single_green_b'


if __name__ == '__main__':
    import cv2

    sbp = SingleGreenPlateB(300)

    for (img, txt, cls) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

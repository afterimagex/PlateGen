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

from plategen.imgen import CharsGenerator
from plategen.plate import SinglePlate, DoublePlate
from plategen.resource import resource_dir


class SingleYellowPlate(SinglePlate):
    '''
    大型汽车号牌
    440mm×140mm
    黄底黑字黑框线
    '''
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_yellow1.bmp'),
        osp.join(resource_dir, 'template/single_yellow2.bmp'),
    ]


class SingleYellowPlateXue(SingleYellowPlate):
    _REGULAR = SinglePlate._REGULAR[:-1] + [
        (['black'], ['学']),
    ]


class DoubleYellowPlate(DoublePlate):
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/double_yellow1.bmp'),
        osp.join(resource_dir, 'template/double_yellow2.bmp'),
    ]


if __name__ == '__main__':
    sbp = DoubleYellowPlate(220)

    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

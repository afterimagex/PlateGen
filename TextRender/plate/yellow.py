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
    _CATEGORY = 'single_yellow'


class SingleYellowPlateXue(SingleYellowPlate):
    '''
    教练摩托车号牌黄底黑字，黑“学”字黑框线教练用摩托车。
    '''
    _REGULAR = SinglePlate._REGULAR[:-1] + [
        (['black'], ['学']),
    ]
    _CATEGORY = 'single_yellow_xue'


class DoubleYellowPlate(DoublePlate):
    '''
    普通摩托车后号牌：黄底黑字黑框线。
    '''
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/double_yellow1.bmp'),
        osp.join(resource_dir, 'template/double_yellow2.bmp'),
    ]
    _CATEGORY = 'double_yellow'


class DoubleYellowPlateXue(DoublePlate):
    '''
    教练摩托车后号牌黄底黑字，黑“学”字黑框线教练用摩托车。
    '''
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/double_yellow1.bmp'),
        osp.join(resource_dir, 'template/double_yellow2.bmp'),
    ]
    _REGULAR = SinglePlate._REGULAR[:-1] + [
        (['black'], ['学']),
    ]
    _CATEGORY = 'single_yellow_xue'


if __name__ == '__main__':
    sbp = DoubleYellowPlateXue(220)

    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

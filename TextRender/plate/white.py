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


class SingleWhitePlateJing(SinglePlate):
    '''
    警车号牌
    440mm×140mm
    白底黑字（“警”字为红字）黑框线
    '''
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_white1.bmp'),
        osp.join(resource_dir, 'template/single_white2.bmp'),
        osp.join(resource_dir, 'template/army1.bmp'),
        osp.join(resource_dir, 'template/army2.bmp'),
    ]
    _REGULAR = SinglePlate._REGULAR[:-1] + [
        (['red'], ['警']),
    ]
    _CATEGORY = 'single_white_jing'


class DoubleWhitePlateJing(DoublePlate):
    '''
    警用摩托车号牌白底黑字，红“警”字黑框线摩托车类警车。
    '''
    _FG_GENERATOR = CharsGenerator()
    _BG_FILES = [
        osp.join(resource_dir, 'template/double_white2.bmp'),
        osp.join(resource_dir, 'template/double_white1.bmp'),
    ]
    _REGULAR = SinglePlate._REGULAR[:-1] + [
        (['red'], ['警']),
    ]
    _CATEGORY = 'double_white_jing'


if __name__ == '__main__':
    sbp = DoubleWhitePlateJing(300)
    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

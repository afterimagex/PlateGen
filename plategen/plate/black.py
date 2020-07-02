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
from plategen.imgen import CharsGenerator
from plategen.plate.base import SinglePlate
from plategen.resource import resource_dir


class SingleBlackPlate(SinglePlate):
    '''
    使、领馆汽车号牌：驻华使、领馆汽车。
    440mm×140mm
    黑底白字白框线
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
        osp.join(resource_dir, 'template/single_black1.bmp'),
        osp.join(resource_dir, 'template/single_black2.bmp'),
    ]


class SingleBlackPlateShi(SingleBlackPlate):
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['使']),
    ]


class SingleBlackPlateLing(SingleBlackPlate):
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['领']),
    ]


class SingleBlackPlateGang(SingleBlackPlate):
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['港']),
    ]


class SingleBlackPlateAo(SingleBlackPlate):
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['澳']),
    ]


if __name__ == '__main__':
    import cv2

    sbp = SingleBlackPlateAo(300)

    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

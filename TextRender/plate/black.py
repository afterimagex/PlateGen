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
from plategen.plate.base import SinglePlate, DoublePlate
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
    _CATEGORY = 'single_black'


class SingleBlackPlateShi(SingleBlackPlate):
    '''使、领馆汽车号牌：黑底白字白框线'''
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['使']),
    ]
    _CATEGORY = 'single_black_shi'


class SingleBlackPlateLing(SingleBlackPlate):
    '''使、领馆汽车号牌：黑底白字白框线'''
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['领']),
    ]
    _CATEGORY = 'single_black_ling'


class SingleBlackPlateGang(SingleBlackPlate):
    '''
    港澳入出境车号牌：
    黑底白字白框线，白“港”、“澳”字，白框线。港澳地区入出内地的汽车。
    '''
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['港']),
    ]
    _CATEGORY = 'single_black_gang'


class SingleBlackPlateAo(SingleBlackPlate):
    '''
    港澳入出境车号牌：
    黑底白字白框线，白“港”、“澳”字，白框线。港澳地区入出内地的汽车。
    '''
    _REGULAR = SingleBlackPlate._REGULAR[:-1] + [
        (['white'], ['澳']),
    ]
    _CATEGORY = 'single_black_ao'


class DoubleBlackPlate(DoublePlate):
    '''
    实际不存在
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
    _CATEGORY = 'double_black'


if __name__ == '__main__':
    import cv2

    sbp = DoubleBlackPlate(300)

    for (img, txt, cls) in sbp:
        print(txt, cls)
        cv2.imshow('1', img)
        cv2.waitKey(0)

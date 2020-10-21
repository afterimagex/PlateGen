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
from plategen.plate import SingleGreenPlateA
from plategen.plate import SinglePlate, DoublePlate
from plategen.resource import resource_dir

__all__ = [
    'ShuffleBlue',
    'ShuffleWhite',
    'ShuffleBlack',
    'ShuffleNew',
    'ShuffleDoubleWhite',
    'ShuffleDoubleBlack',
    'ShuffleDoubleBlue',
    'ShuffleDoubleYellow',
    'ShuffleYellow',
]


class ShuffleBlue(SinglePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_blue1.bmp'),
        osp.join(resource_dir, 'template/single_blue2.bmp'),
    ]
    _CATEGORY = 'single_blue'


class ShuffleYellow(SinglePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_yellow1.bmp'),
        osp.join(resource_dir, 'template/single_yellow2.bmp'),
    ]
    _CATEGORY = 'single_yellow'


class ShuffleWhite(SinglePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_white1.bmp'),
        osp.join(resource_dir, 'template/single_white2.bmp'),
    ]
    _CATEGORY = 'single_white'


class ShuffleBlack(SinglePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_black1.bmp'),
        osp.join(resource_dir, 'template/single_black2.bmp'),
    ]
    _CATEGORY = 'single_black'


class ShuffleNew(SingleGreenPlateA):
    _REGULAR = [
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE_BASE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/green_bg_1.png'),
        osp.join(resource_dir, 'template/green_bg_2.png'),
    ]
    _CATEGORY = 'single_green'


class ShuffleDoubleBlue(DoublePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_blue1.bmp'),
        osp.join(resource_dir, 'template/single_blue2.bmp'),
    ]
    _CATEGORY = 'double_bule'


class ShuffleDoubleYellow(DoublePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_yellow1.bmp'),
        osp.join(resource_dir, 'template/single_yellow2.bmp'),
    ]
    _CATEGORY = 'double_yellow'


class ShuffleDoubleWhite(DoublePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['black', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_white1.bmp'),
        osp.join(resource_dir, 'template/single_white2.bmp'),
    ]
    _CATEGORY = 'double_white'


class ShuffleDoubleBlack(DoublePlate):
    _FG_GENERATOR = CharsGenerator()
    _REGULAR = [
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
        (['white', 'red'], cs.CHINESE + cs.LETTERS + cs.NUMBERS),
    ]
    _BG_FILES = [
        osp.join(resource_dir, 'template/single_black1.bmp'),
        osp.join(resource_dir, 'template/single_black2.bmp'),
    ]
    _CATEGORY = 'double_black'


if __name__ == '__main__':
    import cv2

    sbp = ShuffleDoubleBlack(300)

    for (img, txt) in sbp:
        cv2.imshow('1', img)
        cv2.waitKey(0)

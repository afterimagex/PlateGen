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

CHINESE = list({
    '京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪',
    '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘',
    '粤', '桂', '琼', '渝', '川', '贵', '云', '藏', '陕',
    '甘', '青', '宁', '新', '港', '澳', '使', '领', '学', '警'
})

CHINESE_BASE = list({
    '京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪',
    '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘',
    '粤', '桂', '琼', '渝', '川', '贵', '云', '藏', '陕',
    '甘', '青', '宁', '新'
})

CHINESE_SP = list({
    '挂', '应', '急', '民', '航', '临', '时', '入', '境', '试',
    '年', '月', '日',
    '军', '北', '南', '广', '沈', '兰', '成', '济', '海', '空'
})

LETTERS = list({
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
    'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
})

LETTERS_ALL = list({
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
})

NUMBERS = list({
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
})


class CharSets:
    def __init__(self):
        pass

    @staticmethod
    def numbers():
        return [str(i) for i in range(10)]

    @staticmethod
    def letters_upper():
        return [chr(i) for i in range(65, 91)]

    @staticmethod
    def letters_lower():
        return [chr(i) for i in range(97, 123)]

    @staticmethod
    def punctuations():
        pass

    @staticmethod
    def plate_letters():
        return [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
            'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    @staticmethod
    def plate_chinese_province():
        return [
            '京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪',
            '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘',
            '粤', '桂', '琼', '渝', '川', '贵', '云', '藏', '陕',
            '甘', '青', '宁', '新'
        ]

    @staticmethod
    def plate_chinese_special():
        return [
            '港', '澳', '使', '领', '学', '警'
        ]

    @staticmethod
    def plate_chinese_unusual():
        return [
            '挂', '应', '急', '民', '航', '临', '时',
            '入', '境', '试', '年', '月', '日', '军',
            '北', '南', '广', '沈', '兰', '成', '济',
            '海', '空'
        ]

    @classmethod
    def get(cls, *args):
        sets = []
        for x in args:
            sets += getattr(cls, x)()
        return sorted(sets)

    @staticmethod
    def from_text(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        return [l.strip() for l in lines]

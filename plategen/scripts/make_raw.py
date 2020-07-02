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


import os

import cv2
import numpy as np

from plategen.template.chars import CharsTemplate


def make_92_raw(cw=90, ch=180, num=10):
    '''
    cw 字符宽度
    ch 字符高度
    num 每行字符数
    '''
    chars1 = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]
    chars2 = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    chars3 = [
        '京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪',
        '苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘',
        '粤', '桂', '琼', '渝', '川', '贵', '云', '藏', '陕',
        '甘', '青', '宁', '新', '港', '澳', '使', '领', '学',
        '警'
    ]
    ct = CharsTemplate(black=True)
    canvas = np.zeros((ch * 8, cw * num, 4), dtype=np.uint8)

    x, y = 0, 0
    for i, c in enumerate(chars1):
        if i % num == 0 and i != 0:
            x = 0
            y += ch
        roi = ct.get_chars(c)
        roi = cv2.resize(roi, (cw, ch))
        canvas[y:y + ch, x:x + cw] = roi
        x += cw

    for i, c in enumerate(chars2):
        if i % num == 0:
            x = 0
            y += ch
        roi = ct.get_chars(c)
        roi = cv2.resize(roi, (cw, ch))
        canvas[y:y + ch, x:x + cw] = roi
        x += cw

    for i, c in enumerate(chars3):
        if i % num == 0:
            x = 0
            y += ch
        roi = ct.get_chars(c)
        roi = cv2.resize(roi, (cw, ch))
        canvas[y:y + ch, x:x + cw] = roi
        x += cw

    cv2.imwrite('123.png', canvas)


def make_new_raw():
    img_dir = '../resource/new'

    chinese = [
        'ne000.png', 'ne001.png', 'ne002.png', 'ne003.png', 'ne004.png', 'ne005.png', 'ne006.png', 'ne007.png',
        'ne008.png', 'ne009.png', 'ne010.png', 'ne011.png', 'ne012.png', 'ne013.png', 'ne014.png', 'ne015.png',
        'ne016.png', 'ne017.png', 'ne018.png', 'ne019.png', 'ne020.png', 'ne021.png', 'ne022.png', 'ne023.png',
        'ne024.png', 'ne025.png', 'ne026.png', 'ne027.png', 'ne028.png', 'ne029.png', 'ne030.png'
    ]
    letters = [
        'ne100.png', 'ne101.png', 'ne102.png', 'ne103.png', 'ne104.png', 'ne105.png', 'ne106.png', 'ne107.png',
        'ne108.png', 'ne109.png', 'ne110.png', 'ne111.png', 'ne112.png', 'ne113.png', 'ne114.png', 'ne115.png',
        'ne116.png', 'ne117.png', 'ne118.png', 'ne119.png', 'ne120.png', 'ne121.png', 'ne122.png', 'ne123.png',
    ]

    numbers = [
        'ne124.png', 'ne125.png', 'ne126.png', 'ne127.png', 'ne128.png', 'ne129.png', 'ne130.png', 'ne131.png',
        'ne132.png', 'ne133.png'
    ]

    def make_chinese():
        i, num = 0, 10
        x = y = 0
        cw, ch = 90, 180
        canvas = np.zeros((ch * 4, cw * num, 4), dtype=np.uint8)
        for filename in chinese:

            if i % num == 0 and i != 0:
                x = 0
                y += ch

            fullpath = os.path.join(img_dir, filename)

            image = cv2.imread(fullpath)
            image = cv2.resize(image, (cw, ch))
            mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            image = cv2.bitwise_and(image, image, mask=mask_inv)
            image = cv2.merge([image, mask_inv])

            canvas[y:y + ch, x:x + cw] = image
            x += cw
            i += 1

        cv2.imwrite('chinese.png', canvas)

    def make_letters():
        i, num = 0, 10
        x = y = 0
        cw, ch = 86, 180
        canvas = np.zeros((ch * 4, cw * num, 4), dtype=np.uint8)

        for filename in letters:

            if i % num == 0 and i != 0:
                x = 0
                y += ch

            fullpath = os.path.join(img_dir, filename)

            image = cv2.imread(fullpath)
            image = cv2.resize(image, (cw, ch))
            mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            image = cv2.bitwise_and(image, image, mask=mask_inv)
            image = cv2.merge([image, mask_inv])

            canvas[y:y + ch, x:x + cw] = image
            x += cw
            i += 1

        i = 0
        for filename in numbers:

            if i % num == 0:
                x = 0
                y += ch

            fullpath = os.path.join(img_dir, filename)

            image = cv2.imread(fullpath)
            image = cv2.resize(image, (cw, ch))
            mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            image = cv2.bitwise_and(image, image, mask=mask_inv)
            image = cv2.merge([image, mask_inv])

            canvas[y:y + ch, x:x + cw] = image
            x += cw
            i += 1

        cv2.imwrite('letters.png', canvas)

    make_chinese()
    make_letters()


make_new_raw()

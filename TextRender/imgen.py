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
import numpy as np

from TextRender.resource import resource_dir


class CharsGenerator:
    def __init__(self):
        self._mapping = {}
        self._mapping.update(self._init_letters())
        self._mapping.update(self._init_chinese())

        self._color = [
            np.uint8([255, 255, 255]),
            np.uint8([0, 0, 255]),
            np.uint8([0, 0, 0]),
        ]

    def _init_letters(self):
        xs, ys = 90, 179
        filename = osp.join(resource_dir, 'raw/letters1_1.png')
        assert osp.exists(filename), filename
        image = cv2.imread(filename, -1)
        setting = [
            (0, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']),
            (1, ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']),
            (2, ['U', 'V', 'W', 'X', 'Y', 'Z']),
            (3, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']),
        ]
        mapping = {}
        for i, ms in setting:
            for j, m in enumerate(ms):
                x0 = j * xs
                y0 = i * ys
                roi = image[y0:y0 + ys, x0:x0 + xs].copy()
                mapping[m] = roi
        return mapping

    def _init_chinese(self):
        xs, ys = 90, 179
        filename = osp.join(resource_dir, 'raw/chinese1_1.png')
        assert osp.exists(filename), filename
        image = cv2.imread(filename, -1)
        setting = [
            (0, ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪']),
            (1, ['苏', '浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘']),
            (2, ['粤', '桂', '琼', '渝', '川', '贵', '云', '藏', '陕']),
            (3, ['甘', '青', '宁', '新', '港', '澳', '使', '领', '学', '警']),
        ]
        mapping = {}
        for i, ms in setting:
            for j, m in enumerate(ms):
                x0 = j * xs
                y0 = i * ys
                roi = image[y0:y0 + ys, x0:x0 + xs].copy()
                mapping[m] = roi
        return mapping

    def __call__(self, key, color='black'):
        img = self._mapping[key]
        bgr = img[:, :, :3].copy()
        alpha = img[:, :, 3].copy()

        if color == 'white':
            bgr[:] = self._color[0]
        elif color == 'red':
            bgr[:] = self._color[1]
        elif color == 'black':
            bgr[:] = self._color[2]
        elif color == 'random':
            idx = np.random.randint(0, len(self._color))
            bgr[:] = self._color[idx]
        else:
            raise NotImplemented

        dst = cv2.merge([bgr, alpha])
        return dst


class CharsGeneratorNew(CharsGenerator):
    def __init__(self):
        super().__init__()

    def _init_letters(self):
        xs, ys = 86, 180
        filename = osp.join(resource_dir, 'raw/letters3.png')
        image = cv2.imread(filename, -1)
        setting = [
            (0, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']),
            (1, ['L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']),
            (2, ['W', 'X', 'Y', 'Z']),
            (3, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']),
        ]
        mapping = {}
        for i, ms in setting:
            for j, m in enumerate(ms):
                x0 = j * xs
                y0 = i * ys
                roi = image[y0:y0 + ys, x0:x0 + xs].copy()
                mapping[m] = roi
        return mapping

    def _init_chinese(self):
        xs, ys = 90, 180
        filename = osp.join(resource_dir, 'raw/chinese3.png')
        image = cv2.imread(filename, -1)
        setting = [
            (0, ['京', '津', '冀', '晋', '蒙', '辽', '吉', '黑', '沪', '苏']),
            (1, ['浙', '皖', '闽', '赣', '鲁', '豫', '鄂', '湘', '粤', '桂']),
            (2, ['琼', '渝', '川', '贵', '云', '藏', '陕', '甘', '青', '宁']),
            (3, ['新']),
        ]
        mapping = {}
        for i, ms in setting:
            for j, m in enumerate(ms):
                x0 = j * xs
                y0 = i * ys
                roi = image[y0:y0 + ys, x0:x0 + xs].copy()
                mapping[m] = roi
        return mapping


if __name__ == '__main__':

    cg = CharsGenerator()
    for i in range(100):
        img = cg('蒙', 'random')
        print(img.shape)
        # plt.imshow(img)
        # plt.show()
        # cv2.imshow('1', img)
        # cv2.waitKey(0)

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

import cv2


def int_round(x):
    return int(round(x))


class ImageProvide:
    def __init__(self, aspect_ratio):
        self._aspect_ratio = aspect_ratio

    def get_random(self, size=None):
        pass


def overlay_image(fg, bg, rect):
    x, y, w, h = rect

    roi = bg[y: y + h, x:x + w].copy()
    bgr = fg[:, :, :3]
    alpha = fg[:, :, 3]

    _, mask = cv2.threshold(alpha, 100, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    img_fg = cv2.bitwise_and(bgr, bgr, mask=mask)

    dst = cv2.add(img_bg, img_fg)

    bg[y: y + h, x:x + w] = dst
    return bg

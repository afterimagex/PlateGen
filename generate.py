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

from plategen.default import mixed_plate_generator


def gen_normal_plate():
    ds = mixed_plate_generator()
    for (img, txt) in ds:
        print(txt)
        print(img.shape)
        cv2.imshow('demo', img)
        cv2.waitKey(0)


if __name__ == '__main__':
    gen_normal_plate()

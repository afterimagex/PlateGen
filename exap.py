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
import matplotlib.pyplot as plt
import numpy as np
from tensorpack import dataflow as df

from plategen.plate.green import SingleGreenPlateA


class MotionBlur(df.imgaug.ImageAugmentor):
    def __init__(self, range_dis: int = None, angle: float = 0):
        super(MotionBlur, self).__init__()
        self._init(locals())

    def get_transform(self, img):
        h, w = img.shape[:2]
        min_side = min(h, w) / 2
        max_dis = np.int32(np.clip(self.range_dis, 0, min_side))
        dis = np.random.randint(0, max_dis)
        rad = np.radians(np.random.randint(-self.angle, self.angle))

        psf = np.zeros((h, w))
        x_c = (w - 1) / 2
        y_c = (h - 1) / 2
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)

        for i in range(dis):
            x_offset = np.round(sin_val * i)
            y_offset = np.round(cos_val * i)
            dx = np.int32(x_c - x_offset)
            dy = np.int32(y_c + y_offset)
            psf[dy, dx] = 1

        psf = (psf / psf.sum())[:, :, np.newaxis]
        # plt.imshow(psf)
        # plt.show()

        return MotionBlurTransform(psf)


class MotionBlurTransform(df.imgaug.Transform):
    def __init__(self, psf):
        super(MotionBlurTransform, self).__init__()
        self._init(locals())

    def apply_image(self, img):
        img_f = np.fft.fft2(img)
        print(np.unique(img_f))
        print(img_f.shape)
        plt.imshow(img_f)
        plt.show()
        psf_f = np.fft.fft2(self.psf)
        blurred = np.fft.ifft2(img_f * psf_f)
        blurred = np.abs(np.fft.fftshift(blurred))
        print(np.unique(blurred))
        return np.uint8(blurred)

    def apply_coords(self, coords):
        return coords


if __name__ == '__main__':
    pg = SingleGreenPlateA(174)

    for (img, txt) in pg:
        mb = MotionBlur(10, 15).get_transform(img)

        img = mb.apply_image(img)

        cv2.imshow('123', img)
        cv2.waitKey(0)

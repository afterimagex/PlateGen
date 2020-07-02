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
import numpy as np
from tensorpack import dataflow as df


class MotionBlur(df.imgaug.ImageAugmentor):
    def __init__(self, degree=2):
        super(MotionBlur, self).__init__()
        self._init(locals())

    def get_transform(self, img):
        d = np.random.random_integers(1, self.degree)
        a = np.random.random_integers(1, 89)
        return MotionBlurTransform(d, a)


class MotionBlurTransform(df.imgaug.Transform):
    def __init__(self, degree, angle):
        super(MotionBlurTransform, self).__init__()
        self._init(locals())

    def apply_image(self, img):
        M = cv2.getRotationMatrix2D((self.degree / 2, self.degree / 2), self.angle, 1)
        mbk = np.diag(np.ones(self.degree))
        mbk = cv2.warpAffine(mbk, M, (self.degree, self.degree))
        mbk = mbk / self.degree
        blurred = cv2.filter2D(img, -1, mbk)
        cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
        blurred = np.array(blurred, dtype=np.uint8)
        return blurred

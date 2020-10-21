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


class ResizeRatio(df.imgaug.ImageAugmentor):
    def __init__(self, border_size, border_value=0, center=True):
        assert len(border_size) == 2
        self.border_size = border_size  # (w, h)
        self.center = center
        self.interp = [0, 1, 2, 3, 4, 5]
        self.border_value = border_value
        super(ResizeRatio, self).__init__()

    def get_transform(self, img):
        if self.border_value is None:
            self.border_value = img.mean()

        src_size = (img.shape[1], img.shape[0])
        offset = [0, 0]

        if src_size[0] > src_size[1]:
            dst_w = self.border_size[0]
            dst_h = int(self.border_size[0] * src_size[1] / src_size[0])
            dst_h = np.clip(dst_h, 0, self.border_size[1])
            offset[1] = (self.border_size[1] - dst_h) // 2
        else:
            dst_h = self.border_size[1]
            dst_w = int(self.border_size[1] * src_size[0] / src_size[1])
            dst_w = np.clip(dst_w, 0, self.border_size[0])
            offset[0] = (self.border_size[0] - dst_w) // 2

        if not self.center:
            offset = [0, 0]

        interp = np.random.choice(self.interp)
        return ResizeRatioTransform(self.border_size, src_size, (dst_w, dst_h), offset, interp, self.border_value)


class ResizeRatioTransform(df.imgaug.Transform):
    def __init__(self, border_size, src_size, dst_size, offset, interp=cv2.INTER_CUBIC, border_value=0):
        self.src_size = src_size
        self.dst_size = dst_size
        self.offset = offset
        self.interp = interp
        self.border_size = border_size
        self.border_value = border_value
        super(ResizeRatioTransform, self).__init__()

    def apply_image(self, img):
        resized = cv2.resize(img, self.dst_size, interpolation=self.interp)
        image = np.ones((self.border_size[1], self.border_size[0], 3), dtype=img.dtype) * self.border_value
        x1 = self.offset[0]
        y1 = self.offset[1]
        x2 = self.offset[0] + self.dst_size[0]
        y2 = self.offset[1] + self.dst_size[1]
        image[y1:y2, x1:x2, :] = resized
        return image

    def apply_coords(self, coords):
        coords[:, 0] = coords[:, 0] * (self.dst_size[0] * 1.0 / self.src_size[0]) + self.offset[0]
        coords[:, 1] = coords[:, 1] * (self.dst_size[1] * 1.0 / self.src_size[1]) + self.offset[1]
        return coords


class ResizeSquare(df.imgaug.ImageAugmentor):
    def __init__(self, length, border_value=0, center=True):
        assert isinstance(length, int)
        self.length = length
        self.center = center
        self.interp = [0, 1, 2, 3, 4, 5]
        self.border_value = border_value
        super(ResizeSquare, self).__init__()

    def get_transform(self, img):
        if self.border_value is None:
            self.border_value = img.mean()
        src_size = (img.shape[1], img.shape[0])
        offset = [0, 0]
        if src_size[0] > src_size[1]:
            dst_w = self.length
            dst_h = int(self.length * src_size[1] / src_size[0])
            offset[1] = (self.length - dst_h) // 2
        else:
            dst_h = self.length
            dst_w = int(self.length * src_size[0] / src_size[1])
            offset[0] = (self.length - dst_w) // 2
        if not self.center:
            offset = [0, 0]
        interp = np.random.choice(self.interp)
        return ResizeSquareTransform(self.length, src_size, (dst_w, dst_h), offset, interp, self.border_value)


class ResizeSquareTransform(df.imgaug.Transform):
    def __init__(self, length, src_size, dst_size, offset, interp=cv2.INTER_CUBIC, border_value=0):
        self.src_size = src_size
        self.dst_size = dst_size
        self.offset = offset
        self.interp = interp
        self.length = length
        self.border_value = border_value
        super(ResizeSquareTransform, self).__init__()

    def apply_image(self, img):
        resized = cv2.resize(img, self.dst_size, interpolation=self.interp)
        image = np.ones((self.length, self.length, 3), dtype=img.dtype) * self.border_value
        x1 = self.offset[0]
        y1 = self.offset[1]
        x2 = self.offset[0] + self.dst_size[0]
        y2 = self.offset[1] + self.dst_size[1]
        image[y1:y2, x1:x2, :] = resized
        return image

    def apply_coords(self, coords):
        coords[:, 0] = coords[:, 0] * (self.dst_size[0] * 1.0 / self.src_size[0]) + self.offset[0]
        coords[:, 1] = coords[:, 1] * (self.dst_size[1] * 1.0 / self.src_size[1]) + self.offset[1]
        return coords

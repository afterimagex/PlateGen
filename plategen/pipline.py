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

import numpy as np
from tensorpack import dataflow as df

from plategen.transform import MotionBlur


def plate_generator_pipline(pg, num_proc=10):
    augmentors = df.imgaug.AugmentorList([
        df.imgaug.RandomOrderAug([
            df.imgaug.BrightnessScale((0.6, 1.4), clip=False),
            df.imgaug.Contrast((0.6, 1.4), clip=False),
            df.imgaug.Saturation(0.4, rgb=False),
            # rgb-bgr conversion for the constants copied from fb.resnet.torch
            df.imgaug.Lighting(
                std=0.1,
                eigval=np.asarray([0.2175, 0.0188, 0.0045][::-1]) * 255.0,
                eigvec=np.array(
                    [[-0.5675, 0.7192, 0.4009],
                     [-0.5808, -0.0045, -0.8140],
                     [-0.5836, -0.6948, 0.4203]],
                    dtype='float32')[::-1, ::-1]
            )
        ]),
        df.imgaug.RandomOrderAug([
            df.imgaug.RandomApplyAug(df.imgaug.GaussianNoise(45), 0.5),
            df.imgaug.RandomApplyAug(df.imgaug.GaussianBlur(), 0.5),
            df.imgaug.RandomApplyAug(df.imgaug.JpegNoise(), 0.5),
            # # df.imgaug.RandomApplyAug(df.imgaug.Grayscale(keepshape=True), 0.2),
            df.imgaug.RandomApplyAug(df.imgaug.SaltPepperNoise(), 0.5),
            df.imgaug.RandomApplyAug(MotionBlur(15), 1.0),
        ]),
        df.imgaug.RandomOrderAug([
            df.imgaug.RandomApplyAug(
                df.imgaug.Affine(scale=(0.8, 1.0), translate_frac=(0.05, 0.05), rotate_max_deg=10, shear=35), 0.5),
        ]),
    ])

    ds = df.DataFromGenerator(pg)
    ds = df.AugmentImageComponent(ds, augmentors)
    # ds = df.MultiProcessRunnerZMQ(ds, num_proc=num_proc)
    return ds


if __name__ == '__main__':
    import cv2
    from plategen.plate.shuffle import SingleRandomPlate

    srp = SingleRandomPlate(174)
    ds = plate_generator_pipline(srp)
    ds.reset_state()

    for (img, txt) in ds:
        print(txt)
        print(img.shape)
        cv2.imshow('demo', img)
        cv2.waitKey(0)

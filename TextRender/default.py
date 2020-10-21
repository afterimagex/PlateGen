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


from plategen.pipline import plate_generator_pipline
from plategen.plate import RandomPlateCompose
from plategen.plate import (
    SingleBlackPlate,
    SingleBlackPlateAo,
    SingleBlackPlateGang,
    SingleBlackPlateLing,
    SingleBlackPlateShi
)
from plategen.plate import SingleBluePlate
from plategen.plate import SingleGreenPlateA, SingleGreenPlateB
from plategen.plate import SingleWhitePlateJing
from plategen.plate import SingleYellowPlate, SingleYellowPlateXue, DoubleYellowPlate

from plategen.plate.shuffle import (
    ShuffleBlack,
    ShuffleNew,
    ShuffleWhite,
    ShuffleBlue,
    ShuffleYellow,
    ShuffleDoubleBlue,
    ShuffleDoubleYellow,
    ShuffleDoubleBlack,
    ShuffleDoubleWhite,
)


def normal_random_plate_generator():
    pg = RandomPlateCompose([
        SingleBluePlate(140),
        SingleGreenPlateA(140),
        SingleGreenPlateB(140),
        SingleBlackPlate(140),
        SingleBlackPlateAo(140),
        SingleBlackPlateGang(140),
        SingleBlackPlateLing(140),
        SingleBlackPlateShi(140),
        SingleYellowPlate(140),
        SingleYellowPlateXue(140),
        SingleWhitePlateJing(140),
        DoubleYellowPlate(220),
    ])
    ds = plate_generator_pipline(pg, (128, 64))
    ds.reset_state()

    return ds


def shuffle_plate_generator():
    pg = RandomPlateCompose([
        ShuffleBlack(140),
        ShuffleNew(140),
        ShuffleWhite(140),
        ShuffleYellow(140),
        ShuffleBlue(140),
        ShuffleDoubleBlue(220),
        ShuffleDoubleYellow(220),
        ShuffleDoubleBlack(220),
        ShuffleDoubleWhite(220)
    ])

    ds = plate_generator_pipline(pg)
    ds.reset_state()
    return ds


def mixed_plate_generator():
    pg = RandomPlateCompose([
        ShuffleBlack(140),
        ShuffleNew(140),
        ShuffleWhite(140),
        ShuffleYellow(140),
        ShuffleBlue(140),
        ShuffleDoubleBlue(220),
        ShuffleDoubleBlack(220),
        ShuffleDoubleYellow(220),
        ShuffleDoubleWhite(220),
        SingleBluePlate(140),
        SingleGreenPlateA(140),
        SingleGreenPlateB(140),
        SingleBlackPlate(140),
        SingleBlackPlateAo(140),
        SingleBlackPlateGang(140),
        SingleBlackPlateLing(140),
        SingleBlackPlateShi(140),
        SingleYellowPlate(140),
        SingleYellowPlateXue(140),
        SingleWhitePlateJing(140),

        DoubleYellowPlate(220),
    ])
    ds = plate_generator_pipline(pg)
    ds.reset_state()
    return ds


if __name__ == '__main__':
    import cv2

    ds = normal_random_plate_generator()

    for (img, txt, cls) in ds:
        print(cls)
        print(txt)
        print(len(img))
        print(img[0].shape)

        cv2.imshow('demo', img[0])
        cv2.waitKey(0)

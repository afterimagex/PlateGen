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

from plategen import plate
from plategen.pipline import plate_generator_pipline
from plategen.plate import shuffle  as ps


def make_single():
    pg = plate.RandomPlateCompose([
        plate.SingleBluePlate(140),
        plate.SingleGreenPlateA(140),
        plate.SingleGreenPlateB(140),
        plate.SingleBlackPlate(140),
        plate.SingleBlackPlateAo(140),
        plate.SingleBlackPlateGang(140),
        plate.SingleBlackPlateLing(140),
        plate.SingleBlackPlateShi(140),
        plate.SingleYellowPlate(140),
        plate.SingleYellowPlateXue(140),
        plate.SingleWhitePlateJing(140),
    ])
    ds = plate_generator_pipline(pg)
    ds.reset_state()
    ds = iter(ds)
    nh, nw = 10, 5
    ph, pw = 140, 440
    canvas = np.zeros((ph * nh, pw * nw, 3))
    count = 0
    x, y = 0, 0
    for i in range(nh * nw):
        img, txt = next(ds)
        img = cv2.resize(img, (pw, ph))
        if count % nw == 0 and count != 0:
            x = 0
            y += ph
        canvas[y:y + ph, x:x + pw] = img
        x += pw
        count += 1
    cv2.imwrite('examples/single_plate.jpg', canvas)


def make_double():
    pg = plate.RandomPlateCompose([
        plate.DoubleYellowPlate(220),
        plate.DoubleWhitePlate(220),
        plate.DoubleBluePlate(220),
    ])
    ds = plate_generator_pipline(pg)
    ds.reset_state()
    ds = iter(ds)
    nh, nw = 10, 5
    ph, pw = 220, 440
    canvas = np.zeros((ph * nh, pw * nw, 3))
    count = 0
    x, y = 0, 0
    for i in range(nh * nw):
        img, txt = next(ds)
        img = cv2.resize(img, (pw, ph))
        if count % nw == 0 and count != 0:
            x = 0
            y += ph
        canvas[y:y + ph, x:x + pw] = img
        x += pw
        count += 1
    cv2.imwrite('examples/double_plate.jpg', canvas)


def make_shuffle():
    ph, pw = 140, 440
    pg = plate.RandomPlateCompose([
        ps.ShuffleBlue(ph),
        ps.ShuffleWhite(ph),
        ps.ShuffleNew(ph),
        ps.ShuffleYellow(ph),
        ps.ShuffleBlack(ph),
    ])
    ds = plate_generator_pipline(pg)
    ds.reset_state()
    ds = iter(ds)
    nh, nw = 10, 5

    canvas = np.zeros((ph * nh, pw * nw, 3))
    count = 0
    x, y = 0, 0
    for i in range(nh * nw):
        img, txt = next(ds)
        img = cv2.resize(img, (pw, ph))
        if count % nw == 0 and count != 0:
            x = 0
            y += ph
        canvas[y:y + ph, x:x + pw] = img
        x += pw
        count += 1
    cv2.imwrite('examples/shuffle_plate.jpg', canvas)


if __name__ == '__main__':
    # make_single()
    # make_double()
    make_shuffle()

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
from functools import lru_cache

import cv2
import numpy as np
import numpy.random as npr
from PIL import Image, ImageDraw, ImageFont

from TextRender.charsets import CharSets as cs
from TextRender.config import configurable
from TextRender.resource import resource_dir


def random_color(lower_val, upper_val):
    return [
        npr.randint(lower_val, upper_val),
        npr.randint(lower_val, upper_val),
        npr.randint(lower_val, upper_val)
    ]


def put_text(image, x, y, text, font, color=None):
    """
    写中文字
    :param image:
    :param x:
    :param y:
    :param text:
    :param font:
    :param color:
    :return:
    """

    im = Image.fromarray(image)
    draw = ImageDraw.Draw(im)
    color = (255, 0, 0) if color is None else color
    draw.text((x, y), text, color, font=font)
    return np.array(im)


class TextLine:
    '''
    文本基类
    '''

    @configurable
    def __init__(self, **kwargs):
        super().__init__()
        if kwargs:
            for k, v in kwargs.items():
                if k != 'self' and not k.startswith('_'):
                    setattr(self, k, v)

    @classmethod
    def from_config(cls, cfg):
        params = {
            'dst_h': 128,
            'dst_w': 32,
            'bg_dir': [],
            'font_paths': [
                os.path.join(resource_dir, 'fonts', 'eng_92.ttf'),
            ],
            'charsets': cs.letters_upper() + cs.numbers(),
            'font_size': [30, 25, 20, 18],
            'text_length_range': (5, 9),
        }
        params.update(cfg)
        return params

    def get_random_background(self):
        prob = npr.random()
        pure_bg = np.ones((self.dst_h, self.dst_w, 3)) * np.array(random_color(0, 255))

        random_bg = np.random.rand(self.dst_h, self.dst_w, 3) * 100
        if prob < 0.1:
            return random_bg
        elif prob < 0.8:
            return pure_bg
        else:
            b = npr.random()
            mix_bg = b * pure_bg + (1 - b) * random_bg
            return mix_bg

    def get_random_foreground(self):
        image_array = np.zeros((self.dst_h, self.dst_w, 3))
        image = np.uint8(image_array)
        image = Image.fromarray(image)
        draw = ImageDraw.Draw(image)

        length = npr.randint(5, 9)
        grids = []
        text = []
        for i in range(length):
            size = npr.choice([30, 20, 18])
            ffont = npr.choice([os.path.join(resource_dir, 'fonts', 'eng_92.ttf')])
            font = ImageFont.truetype(ffont, size=size)
            char = npr.choice(self.charsets)
            text.append(char)

        text = ''.join(text)

        w, char_h = font.getsize(text)
        char_w = int(w / len(text))

        text = self.vertical_draw(draw, text, font, tuple(random_color(105, 255)), char_w, char_h)

        image = np.array(image)
        print(image.shape)

        print(text)
        cv2.imshow('123', image)
        cv2.waitKey(0)

    def vertical_draw(self, draw, text, font, color, char_w, char_h):
        """
        锤子方向文字生成
        :param draw:
        :param text:
        :param font:
        :param color:
        :param char_w:
        :param char_h:
        :return:
        """
        text_h = len(text) * char_h
        h_margin = max(self.dst_h - text_h, 1)
        w_margin = max(self.dst_w - char_w, 1)
        x_shift = np.random.randint(0, w_margin)
        y_shift = np.random.randint(0, h_margin)
        i = 0
        while i < len(text):
            draw.text((x_shift, y_shift), text[i], color, font=font)
            i += 1
            x_shift = np.random.randint(0, w_margin)
            y_shift += char_h
            # 如果下个字符超出图像，则退出
            if y_shift + char_h > self.dst_h:
                break
        return text[:i]

    # def get_random_background(self):
    #     image = cv2.imread(np.random.choice(self._BG_FILES))
    #     image = cv2.resize(image, (self.plate_w, self.plate_h))
    #     return image
    #
    # def get_random_foreground(self, reg, size):
    #     color = np.random.choice(reg[0])
    #     char = np.random.choice(reg[1])
    #     image = self._FG_GENERATOR(char, color)
    #     image = cv2.resize(image, size)
    #     return char, image
    #
    # def __len__(self):
    #     return 0
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     while True:
    #         bg = self.get_random_background()
    #         text = []
    #         for i, rect in enumerate(self.layouts):
    #             txt, img = self.get_random_foreground(self._REGULAR[i], (rect[2], rect[3]))
    #             bg = overlay_image(img, bg, rect)
    #             text.append(txt)
    #         return bg, text


def get_random():
    @lru_cache(maxsize=512)
    def get_files():
        return os.listdir('../')

    return npr.choice(get_files())


def make_fg():
    iarray = np.zeros((780, 100, 3), dtype=np.uint8)
    canvas = Image.fromarray(iarray)
    draw = ImageDraw.Draw(canvas)

    # bg = cv2.imread('')

    text = 'BHS123ASDF3'

    x, y = 10, 0
    for i in range(len(text)):
        size = npr.choice([68])
        font = ImageFont.truetype(os.path.join(resource_dir, 'fonts', 'eng_92.ttf'), size=size)
        cw, ch = font.getsize(text[i])
        print('*', cw, ch)
        print(text[i])
        draw.text((x, y), text[i], (255, 255, 255), font)
        y += ch
        print(x, y)

    image = np.array(canvas)
    print(image.shape)
    print(text)
    cv2.imshow('123', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    # tl = TextLine({})
    # tl.get_random_foreground()
    make_fg()

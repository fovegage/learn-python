# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 10:29
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : pil_stu.py
# @Software: PyCharm

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

im = Image.open('./pic.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blue.png', 'png')

# 验证码
# 随机字母
def ranchar():
    return chr(random.randint(65, 90))

#随机颜色
def rancolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

width = 60 * 4
heigth = 60
image = Image.new('RGB', (width, heigth), (255, 255, 255))
draw = ImageDraw.Draw(image)  # 构建对象
# 填充像素点
for x in range(width):
    for y in range(heigth):
        draw.point((x, y), fill=rancolor())
# 填充字母
for i in range(4):
    draw.text((60 * i + 10, 10), ranchar(), font=ImageFont.truetype(font='C:\\Windows\\Fonts\\Arial.ttf', size=36))

image.save("code.png", "png")


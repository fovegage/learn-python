# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : qrcode_stu.py
# @Software: PyCharm

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://gaozhe.top')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
print(img)
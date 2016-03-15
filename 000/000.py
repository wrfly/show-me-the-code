#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def draw_num(iamge_path, num):
	in_img = Image.open(iamge_path)
	out_img = iamge_path.split('.')[0]+'_out_'+'.jpg'
	x, y = in_img.size
	font = ImageFont.truetype('monofont.ttf', x / 3)
	ImageDraw.Draw(in_img).text((2 * x / 3, 0), str(num), font = font, fill = 'red')
	in_img.save(out_img)

draw_num('head.jpg', '99+')
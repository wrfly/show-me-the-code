#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def draw_num(iamge_path, num):
	img = Image.open(iamge_path)
	x, y = img.size

	save_img = iamge_path.split('.')[0]+'_out_'+'.jpg'
	font = ImageFont.truetype('monofont.ttf', x / 2)
	draw_img = ImageDraw.Draw(img)
	draw_img.text([x*3/4, -10], str(num), font=font, fill='red')
	img.save(save_img)

draw_num('head.jpg', '9')

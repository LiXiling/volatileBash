# -*- coding: utf-8 -*-
__author__ = "Victor Schümmer"
__email__ = "victor_ferdinand.schuemmer@stud.tu-darmstadt.de"

import Tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageFont
from io import BytesIO

def txt2img(text, fontname='arial.ttf', fontsize=50, color='black', bgcolor='white'):
    font = ImageFont.truetype(fontname, fontsize)
    spacing = 1.2
    padding = 20
    lines = text.splitlines()
    size = textsize(lines, font, spacing)
    lineheight = size[1] / len(lines)
    img = Image.new('RGB', (size[0]+2*padding, size[1]+2*padding), bgcolor)
    y = padding
    for l in lines: 
        ImageDraw.Draw(img).text((padding,y), l, font=font, fill=color)
        y += lineheight
    file = BytesIO()
    img.save(file, 'png')
    return file
    
def textsize(lines, font, spacing):
    width = height = 0
    d = ImageDraw.Draw(Image.new('RGB', (0,0)))
    for l in lines:
        size = d.textsize(l, font)
        width = max(width, size[0])
        height += spacing * size[1]
    return int(width), int(height)
      
def show(img):
    root = tk.Tk()
    root.title('txt2img')
    image = ImageTk.PhotoImage(file = img)
    root.geometry("%dx%d+%d+%d" % (image.width(), image.height(), 0, 0))
    tk.Label(root, image=image).pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
    root.mainloop()
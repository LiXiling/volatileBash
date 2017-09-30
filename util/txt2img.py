# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

class txt2img():
    
    """A converter that generates an image containing a given text."""
    
    def __init__(self, text, fontname='LiberationMono-Regular.ttf', fontsize=50, color='black', bgcolor='white'):
        """
        Args:
            text (str): the text to be converted
            fontname (str, optional): filename of the true type font to use.
                Defaults to: LiberationMono-Regular.ttf
            fontsize (int, optional): the font size in points
            color (str, optional): font color
            bgcolor (str, optional): background color
        """
        font = ImageFont.truetype(fontname, fontsize)
        spacing = 1.2
        padding = 20
        lines = text.splitlines()
        size = self._textsize(lines, font, spacing)
        lineheight = size[1] / len(lines)
        img = Image.new('RGB', (size[0]+2*padding, size[1]+2*padding), bgcolor)
        y = padding
        for l in lines: 
            ImageDraw.Draw(img).text((padding,y), l, font=font, fill=color)
            y += lineheight
        file = BytesIO()
        img.save(file, 'png')
        self.png_image = file.getvalue()
        
    def _textsize(self, lines, font, spacing):
        """Calculates the image dimensions needed to fit the whole text."""
        width = height = 0
        d = ImageDraw.Draw(Image.new('RGB', (0,0)))
        for l in lines:
            size = d.textsize(l, font)
            width = max(width, size[0])
            height += spacing * size[1]
        return int(width), int(height)
          
    def show(self):
        try:
            from PIL import ImageTk
            import tkinter as tk
        except:
            print("cannot find tkinter")
            return
        root = tk.Tk()
        root.title('txt2img')
        image = ImageTk.PhotoImage(data = self.png_image)
        root.geometry("%dx%d+%d+%d" % (image.width(), image.height(), 0, 0))
        tk.Label(root, image=image).pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
        root.mainloop()
        
    def img_data(self):
        """Returns:
            bytes: converted image as bytes
        """
        return self.png_image
        
    def save(self, filename='out.png'):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(self.png_image)
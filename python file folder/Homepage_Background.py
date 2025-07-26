from fractions import Fraction
from PIL import Image

class Image_crop():
    def __init__(self, master,image_path):
        self.master = master
        self.image = Image.open(image_path)
        ratio = Fraction(str(self.master.winfo_screenwidth())+'/'+str(self.master.winfo_screenheight()))
        x_pixels = 3640/ratio.numerator
        y_pixels = 2160/ratio.denominator

        if x_pixels < y_pixels:
            y_pixels = 2160 - (x_pixels * ratio.denominator)
            background_crop = 0,y_pixels,3640,2160
        
        else:
            x_pixels = y_pixels* ratio.numerator
            background_crop = 0, 0, x_pixels, 2160
        
        self.image = self.image.crop(background_crop)


    def ret(self):
       return self.image
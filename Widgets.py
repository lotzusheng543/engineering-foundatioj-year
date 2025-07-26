
from PIL import Image, ImageTk


class CanvasButton:
    def __init__(self, canvas, x, y, image_path, command, posi = 'c', width=None, height=None):
        self.canvas = canvas
        x, y = canvas.canvasx(x), canvas.canvasy(y)
        
        # Load image from file
        img = Image.open(image_path)
        
        # Resize image if width or height is provided
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / img.size[1] * img.size[0])
            if height is None:
                height = int(float(width) / img.size[0] * img.size[1])
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        # Create PhotoImage from resized image
        self.btn_image = ImageTk.PhotoImage(img)
        
        # Create canvas button object and bind command to it
        self.canvas_btn_img_obj = self.canvas.create_image(x, y, anchor=posi, image=self.btn_image, tag = "buttons")
        self.canvas.tag_bind(self.canvas_btn_img_obj, '<Button-1>', lambda event: command())

    
    def configure(self, x, y, layer = None, tag = None):
        self.canvas.coords(self.canvas_btn_img_obj, x, y)
        if layer == "raise":
            #print('raise')
            self.canvas.tag_raise(self.canvas_btn_img_obj)
        elif layer == "lower":
            #print('lower')
            self.canvas.tag_lower(self.canvas_btn_img_obj, tag)
        else:
            pass
    

class CanvasLabel:
    def __init__(self, canvas, x, y, image_path ,posi = 'c', width=None, height=None, tag = None):
        self.canvas = canvas
        x, y = canvas.canvasx(x), canvas.canvasy(y)
        
        # Load image from file
        img = Image.open(image_path)
        self.img = img.copy()
        
        # Resize image if width or height is provided
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / img.size[1] * img.size[0])
            if height is None:
                height = int(float(width) / img.size[0] * img.size[1])
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        # Create PhotoImage from resized image
        self.btn_image = ImageTk.PhotoImage(img)
        if tag != None:
            # Create canvas button object and bind command to it
            self.canvas_btn_img_obj = self.canvas.create_image(x, y, anchor=posi, image=self.btn_image, tag = tag)
        else:
             self.canvas_btn_img_obj = self.canvas.create_image(x, y, anchor=posi, image=self.btn_image)

    def configure(self, x, y, width = None, height = None ):
        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / self.img.size[1] * self.img.size[0])
            if height is None:
                height = int(float(width) / self.img.size[0] * self.img.size[1])
            img = self.img.resize((width, height), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            self.canvas.itemconfig(self.canvas_btn_img_obj, image = img)
            self.btn_image = img
        else:
            pass
        self.canvas.coords(self.canvas_btn_img_obj, x, y)
        

class dial:
    def __init__(self, canvas, x, y, image_path, angle=90, width=None, height=None):
        self.canvas = canvas
        x, y = canvas.canvasx(x), canvas.canvasy(y)
        self.image_path = image_path

        img = Image.open(image_path)

        if width is not None or height is not None:
            if width is None:
                width = int(float(height) / img.size[1] * img.size[0])
            if height is None:
                height = int(float(width) / img.size[0] * img.size[1])
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            self.width = width
            self.height = height
        #img = img.resize((int(44/4),int(362/4)), Image.ANTIALIAS)
        x_img, y_img = img.size
        img = img.rotate(angle, expand=True, resample = Image.BILINEAR)

        self.image = ImageTk.PhotoImage(img)
        self.angle = angle
        self.canvas_image_obj = canvas.create_image(x, y, anchor='c', image=self.image)

    def set_angle(self, angle):
        self.angle = angle
        img = Image.open(self.image_path)
        img = img.resize((self.width,self.height), Image.Resampling.LANCZOS)
        img = img.rotate(self.angle, expand=True)
        self.image = ImageTk.PhotoImage(img)
        self.canvas.itemconfig(self.canvas_image_obj, image=self.image)

    def configure(self, x, y):
        self.canvas.coords(self.canvas_image_obj, x, y)

    def bind(self, event, command):
        self.canvas.tag_bind(self.canvas_image_obj, event, command)

class slider: 
    def __init__(self, canvas, x, y, value):
        self.canvas = canvas
        x, y = canvas.canvasx(x), canvas.canvasy(y)
        self.value = value
        self.x = x 
        self.y = y
        self.x0 = x-100
        self.y0 = y
        self.x1 = x+100
        self.x2 = x-self.value
        self.x3 = x+self.value
        self.y1 = y + 10
        

        self.main = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill = "#F35000")

        self.left = self.canvas.create_rectangle(self.x0, self.y0, self.x2, self.y1, fill = "#EBB840" )
        
        self.right = self.canvas.create_rectangle(self.x1, self.y0, self.x3, self.y1, fill='#EBB840')
        
    def set_range(self, value):
        self.value = value
        self.x2 = self.x-value
        self.x3 = self.x+value
        self.y1 = self.y + 10
        self.canvas.coords(self.left, self.x0, self.y0, self.x2, self.y1)
        self.canvas.coords(self.right,self.x3, self.y0, self.x1, self.y1)

    def configure(self, x, y):
        self.x = x
        self.y = y
        self.x0 = x-100
        self.y0 = y
        self.x1 = x+100
        self.x2 = x-self.value
        self.x3 = x+self.value
        self.y1 = y + 10
        self.canvas.coords(self.main,self.x0,self.y0,self.x1,self.y1)
        self.canvas.coords(self.left, self.x0, self.y0, self.x2,self.y1)
        self.canvas.coords(self.right,self.x1, self.y0, self.x3, self.y1)
    
    def bind(self, event, command):
        self.canvas.tag_bind(self.main, event, command)



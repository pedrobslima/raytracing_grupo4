from PIL import Image as ImagePil
import numpy as np
import os

class MyImage():
    def __init__(self, height, width, background_color) -> None:
        self.height = height
        self.width = width
        self.background_color = background_color
        self.pixel_grid = [[self.background_color for __ in range(self.width)] for _ in range(self.height)]

    def set_pixel_color(self, i: int, j: int , color: list):
        self.pixel_grid[i][j] = color

    def draw_image(self, file):
        pixel_grid = np.array(self.pixel_grid).astype(np.uint8)

        print(f'Resolution: {np.shape(pixel_grid)}')
        my_image = ImagePil.fromarray(pixel_grid)
        
        directory = os.getcwd()
        image_dir = os.path.join(directory, "imagens")

        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        path = os.path.join(image_dir, f'{file[:-5]}_out.png')
        my_image.save(path)

    def save(self, file_name):
        pixel_grid = np.array(self.pixel_grid).astype(np.uint8)
        my_image = ImagePil.fromarray(pixel_grid)
        my_image.save(file_name)

    def show(self):
        pixel_grid = np.array(self.pixel_grid).astype(np.uint8)
        my_image = ImagePil.fromarray(pixel_grid)
        my_image.show() 

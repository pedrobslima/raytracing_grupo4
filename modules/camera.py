from math import sqrt, inf, hypot
from modules.ray import Ray
import numpy as np

class Camera:
    #__slots__ = ('position', 'screen_size', 'fov')
    
    def __init__(self, camera_point: list, looking_point: list, up_vector: list,
                 distance: float, screen_height: float, screen_width: float):
        self.position = np.array(camera_point)
        self.looking_point = np.array(looking_point)
        self.up_vector = np.array(up_vector)
        self.distance = distance
        
        self.height = screen_height
        self.width = screen_width

        self.w = self.position - self.looking_point # vector w
        self.w = self.w / hypot(*self.w) # normalizing w
        self.u = np.cross(up_vector, self.w) # vector u
        self.u = self.u / hypot(*self.u) # normalizing u
        self.v = np.cross(self.w, self.u) # vector v (already normalized)
    
    def calc_pixel_center(self, pxl_size: float):
        screen_center = self.position - self.distance * self.w
        pxl_center = screen_center + pxl_size * (((self.height - 1)/2) * self.v - ((self.width - 1)/2) * self.u)
        return pxl_center

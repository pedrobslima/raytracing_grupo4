import numpy as np
from PIL import Image
from math import hypot
from ray import Ray
from objects import Sphere, Triangle, Object
from build import Build
from light import Light

# Crie uma lista de objetos da cena (uma esfera e um triângulo)
sphere = Sphere(Object,[0, 0, -3], 1.0, [1, 0, 0], 0.2, 0.8, 0.5, 32, 0.0, 0.0, 1.5)
triangle = Triangle(Object,[[-1, -1, -2], [1, -1, -2], [0, 1, -2]], [0, 0, 1], 0.2, 0.8, 0.5, 32, 0.0, 0.0, 1.5)
light1 = Light([1.0, 1.0, 1.0], [2.0, 2.0, -2.0])

# Crie um dicionário de cena com os objetos
scene_dict = {
    'v_res': 480,
    'h_res': 640,
    'square_side': 0.01,
    'dist': 1.0,
    'eye': [0, 0, 0],
    'look_at': [0, 0, -1],
    'up': [0, 1, 0],
    'background_color': [0, 0, 0],
    'objects': [sphere, triangle],
    'object_list': [sphere, triangle],
    'lights': [light1], 
    'ambient_light': [0.1, 0.1, 0.1],
    'max_depth': 5
}

# Crie uma instância da classe Build com o dicionário de cena
scene = Build(scene_dict)

# Renderize a cena
rendered_image = scene.render_scene()

# Salve a imagem renderizada em um arquivo
""" #-
rendered_image.draw_image("output.png")
#- """
rendered_image.save("imagens/output.png")
# Exiba a imagem (opcional)
rendered_image.show()

from src.fractals import *
import numpy as np

u = np.array([2, 3])
v = np.array([5, 8])
# O número 4 é a quantidade de vezes que ele irá se "auto recriar"
# recomendo usar até 5, se não o negócio fica muito doido
# e irá precisar aumentar o tamanho do plot, mas podemos extremos em aula
create_images(u, v, 4)
create_gif_from_images()

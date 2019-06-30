import os
import imageio
import numpy as np
from matplotlib import pyplot as plt
from random import randint


def create_images(u, v, quantidade):
    if quantidade < 1:
        return

    teta_um = np.array([
        [.5, -(3**.5)/6],
        [(3**.5)/6, .5]
    ])
    teta_dois = np.array([
        [.5, (3 ** .5)/6],
        [-(3 ** .5)/6, .5]
    ])
    result = [
        u,
        (2/3)*u + (1/3)*v,
        np.matmul(teta_um, v.transpose()) + np.matmul(teta_dois, u.transpose()),
        (1/3)*u + (2/3)*v,
        v
    ]
    r = [nparray.tolist() for nparray in result]

    plt.xlim(2, 8)
    plt.ylim(2, 8)
    quantidade -= 1
    create_images(np.array(r[0]), np.array(r[1]), quantidade)
    create_images(np.array(r[1]), np.array(r[2]), quantidade)
    create_images(np.array(r[2]), np.array(r[3]), quantidade)
    create_images(np.array(r[3]), np.array(r[4]), quantidade)
    plt.plot([r[0][0], r[1][0], r[2][0], r[3][0], r[4][0]], [r[0][1], r[1][1], r[2][1], r[3][1], r[4][1]], 'b')
    plt.savefig(f'images/{randint(0,99999999)}.png')


def create_gif_from_images():
    search_dir = "images/"
    files = os.listdir(search_dir)
    files = [os.path.join(search_dir, f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))

    images = [imageio.imread(file_name) for file_name in files]

    imageio.mimsave('./animation.gif', images, fps=10)

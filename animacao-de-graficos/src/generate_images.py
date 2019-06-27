import os
import imageio
from matplotlib import pyplot as plt


def create_images():
    x = 0
    y = 40
    for i in range(0, 20):
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.plot([x, y*(i/10)], [x, y*(i/10)])
        plt.savefig(f'images/{i}.png')


def create_gif_from_images():
    list_of_images = os.listdir('images/')
    list_of_images_ordered = sorted(list_of_images, key=lambda x: int(os.path.splitext(x)[0]))
    images = []

    for file_name in list_of_images_ordered:
        file_path = os.path.join('images/', file_name)
        images.append(imageio.imread(file_path))

    imageio.mimsave('./animation.gif', images, fps=30)


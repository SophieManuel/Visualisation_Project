import sys
import os
import imageio
import cv2
from wwstatviz import Visualizer


def make_frames():
    if not os.path.exists('temp'):
        os.makedirs('temp')
    v = Visualizer('covid19.csv')
    for feature in v.get_features():
        fig = v.choropleth(feature=feature, countries='all',
                           scale_feature=True,
                           title='COVID19 Evolution - Total Deaths')
        fig.save(f'temp/frame_{feature}.png')


def make_movie():
    image_folder = 'temp'
    video_name = 'movie.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
    images = list(sorted(images))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 5, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()


def make_gif():
    image_folder = 'temp'
    images = [img for img in os.listdir(image_folder) if img.endswith('.png')]
    images = list(sorted(images))
    images = [imageio.imread(f'{image_folder}/{e}') for e in images]
    imageio.mimsave('movie.gif', images, fps=5)


if __name__ == '__main__':

    print('generating movie frames...')
    make_frames()
    print('making AVI movie...')
    make_movie()
    print('making GIF movie...')
    make_gif()

'''Simple Image Manipulator for Linux'''

import os
import glob
from PIL import Image


def list_images():
    '''Walk through the current folder and return a list of filenames
    that are images'''
    image_types = ('*.jpg', '*.JPG', '*.JPEG', '*.jpeg', '*.png', '*.bmp',
                   '*.BMP', '*.gif', '*.GIF'
                   )
    image_list= []
    for file in image_types:
        image_list.append(glob.glob(file))
    return [item for sublist in image_list for item in sublist]

def make_dest_dir():
    '''Iterate through the list and resize images as per user specification'''
    # os.chdir(location)
    resize_folder = 'resized'
    if os.path.isdir(resize_folder):
        print('{} folder already exists'.format(resize_folder))
    else:
        cmd = 'mkdir {}'.format(resize_folder)
        os.system(cmd)
    destination_folder = resize_folder
    return str(destination_folder)

def resize_images(pics, new_size, destination):
    '''Resize images and put them in the destination directory'''
    images = pics
    i = 1
    numpics = len(images)
    img_quality = 95
    for image in images:
        image_object = Image.open(image)
        new_width = int(new_size)
        size_percentage = (new_width / float(image_object.size[0]))
        new_height = int(
            (float(image_object.size[1]) * float(size_percentage))
            )
        new_image = image_object.resize(
            (new_width, new_height), Image.ANTIALIAS
            )
        new_image.save(destination + '/' + image, quality=img_quality)
        print('Processed {} - {} of {}'.format(image, i, numpics))
        i += 1

    print('images processed and copied to the {} subfolder'.format(destination))


def main():
    '''Ask for information on which size'''
    
    file_sizes = {
               'L': '2376',
               'M': '1024',
               'S': '800',
               'T': '250',
               'Th': '128'
               }
    
    print('''Resize for:
          (L)arge,
          (M)edium Email,
          (S)mall Web,
          (T)inu,
          (Th)umbnail
          (Q)uit''')

    size = input('>: ')
    if size == 'q' or size == 'Q':
        exit(0)
    elif size in file_sizes.keys():
        new_size = file_sizes[size]
    else:
        print('Try Again')
        main()

    flat_list = list_images()
    if len(flat_list) == 0:
        print("No Image Files to Resize in this folder")
        print("Good Bye")
    else:
        destination = make_dest_dir()
    resize_images(flat_list, new_size, destination)
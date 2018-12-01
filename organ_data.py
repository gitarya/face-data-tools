"""Rename the image based on the folder name"""
import os
import shutil
import sys
import argparse
from PIL import Image

def main(args):
    original_path = args.data_dir
    saved_path = args.save_dir
    make_path(saved_path)
    all_folders = traversalDir_FirstDir(original_path)
    for folder in all_folders:
        files = os.listdir(original_path + folder)
        i = 1
        for file in files:
            suffix = '.png'
            name = folder + '_' + str(i).zfill(4) + suffix
            i = i + 1
            sub_saved_path = saved_path + folder
            original_file_path = original_path + folder + '/' + file
            make_path(sub_saved_path)
            if args.resize:
                resize(original_file_path, sub_saved_path + '/' + file, int(args.resize_num))
            else:
                shutil.copyfile(original_file_path, sub_saved_path + '/' + name)

# To get all sub folders in one folder
def traversalDir_FirstDir(path):
    list = []
    if (os.path.exists(path)):
        files = os.listdir(path)
        for file in files:
            m = os.path.join(path,file)
            if (os.path.isdir(m)):
                h = os.path.split(m)
                list.append(h[1])
        return list

# To judge whether a folder is existed.
def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def resize(image_path, saved_path,size):
    img = Image.open(image_path)
    img = img.resize((size, size), Image.ANTIALIAS)
    img.save(saved_path)

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, help='Directory with aligned images.', default='/nfs/data1/datasets/ourPhoto_160/')
    parser.add_argument('--save_dir', type=str, help='Directory to save renamed images.', default='/nfs/data1/datasets/ourPhoto_112_resize/')
    parser.add_argument('--resize', type=str, help='the size of resized image', default=False)
    parser.add_argument('--resize_num', type=str, help='the size of resized image', default='112')

    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))

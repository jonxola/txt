import argparse
from pathlib import Path
from PIL import Image

from .convert import convert

def txt():
    args = get_args()
    img_path = Path(args.path).resolve()
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        print(f'Image not found at {img_path}')
        raise SystemExit(1)
    else:
        art = convert(img, args.width)
        print(art)

def get_args():
    '''Set up CLI.'''
    parser = argparse.ArgumentParser(prog='txt', description='Turn an image into text art!')
    parser.add_argument('path', help='path to the image')
    parser.add_argument('-w', '--width', type=int, default=80, help='width of the text art')
    return parser.parse_args()
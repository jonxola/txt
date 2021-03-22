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
        if args.output is None: 
            print(art)
        else:
            output(art, img_path.stem, args.output)

def output(art, name, output_path):
    '''Write text art to a file.'''
    p = Path(output_path).resolve()
    if p.is_dir():
        with open(p.joinpath(f'{name}.txt'), 'a') as file:
            file.write(art)
    else:
        print(f'{p} doesn\'t exist.')
        raise SystemExit(1)

def get_args():
    '''Set up CLI.'''
    parser = argparse.ArgumentParser(prog='txt', description='Turn an image into text art!')
    parser.add_argument('path', help='path to the image')
    parser.add_argument('-w', '--width', type=int, default=80, help='width of the text art')
    parser.add_argument('-o', '--output', metavar='OUTPUT_PATH', help='optionally output text art to a file instead of printing.')
    return parser.parse_args()
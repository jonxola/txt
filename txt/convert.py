ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def convert(img, width=80):
    '''Convert a Pillow Image into text art.'''
    img = resize(img, width)
    img = grayscale(img)
    chars = get_chars(img)
    art = split_chars(chars, width)
    return art

def resize(img, width):
    '''Resize an image maintaining original aspect ratio.'''
    (og_width, og_height) = img.size
    aspect_ratio = og_height / float(og_width)
    height = int(width * aspect_ratio)
    return img.resize((width, height))

def grayscale(img):
    '''Convert an image to grayscale.

    Each pixel gets a gray value 0-255 shades of gray.
    0: black, 255: white
    '''
    return img.convert('L')

def get_chars(img):
    '''Convert grayscale pixels to ASCII characters.

    Divide the 256 shades of gray into 11 groups (for 11 available characters).
    Each group must correspond to 24 gray values to cover all 256 shades.
    Assign each pixel a character according to the group its grayscale value falls in.
    '''
    pixels = list(img.getdata())
    chars = [ASCII_CHARS[int(pixel/24)] for pixel in pixels]
    return ''.join(chars)

def split_chars(chars, width):
    '''Split a list of characters into rows of [width] characters each.'''
    rows = [
        chars[line_start:(line_start + width)]
        for line_start in range(0, len(chars), width)
    ]
    return '\n'.join(rows)
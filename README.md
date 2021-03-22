Turn an image into text art with `txt`!

## Installation
`txt` is installed with [pipx][2].

```
pipx install git+https://github.com/jonxola/txt.git
```

## Usage
```
txt <path> [-w|--width <width>]
```
* `<path>`: The path to the image you want to convert.
* `-w`, `--width`: Art width in characters (defaults to 80).

If you want to write the text art to a file, you can redirect the output:
```
txt <path> > ~/Downloads/art.txt
``` 

Built with the help of [Praveen Kumar's demo][1].

[1]: https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
[2]: https://pipxproject.github.io/pipx/
# pypixel

This is a Python image process library

# Feature

- open and save an Image 
- show an Image
- convert RGB to Gray
- convert RGB to Binary

# Usage

## Import package

```py
from pypixel import Image
```

## Open an Image

```py
img = Image.open("filepath")
```

## Save an Image

```py
img = Image.open("filepath")
...
# Do something to img
...
img.save("filepath")
```

## Show an Image

```py
img = Image.open("filepath")
img.show()
```

## Convert to gray

```py
img = Image.open("url")
img = img.gray()    # default : Float Algorithm
img = img.gray("F") # Float Algorithm : r*0.3+g*0.59+b*0.11
img = img.gray("G") # Green Only
```

## Convert to binary
```py
img = Image.open("url")
img = img.binary()
```

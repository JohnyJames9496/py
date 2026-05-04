from PIL import Image

def shrink(image, factor):
    width, height = image.size
    new = Image.new("RGB", (width // factor, height // factor))

    new_y = 0
    for y in range(0, height, factor):
        new_x = 0
        for x in range(0, width, factor):
            pixel = image.getpixel((x, y))
            new.putpixel((new_x, new_y), pixel)
            new_x += 1
        new_y += 1

    return new


img = Image.open("input.jpg")
small = shrink(img, 2)   
small.show()
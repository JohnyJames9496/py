from PIL import Image

def edge_detect(image, threshold):
    new = image.copy()

    def intensity(pixel):
        r, g, b = pixel
        return (r + g + b) // 3

    for y in range(image.height - 1):
        for x in range(1, image.width):

            p = image.getpixel((x, y))
            left = image.getpixel((x - 1, y))
            bottom = image.getpixel((x, y + 1))

            diff1 = abs(intensity(p) - intensity(left))
            diff2 = abs(intensity(p) - intensity(bottom))

            if diff1 > threshold or diff2 > threshold:
                new.putpixel((x, y), (0, 0, 0))      # edge
            else:
                new.putpixel((x, y), (255, 255, 255)) # no edge

    return new


img = Image.open("input.jpg")
edges = edge_detect(img, 20)   
edges.show()
from PIL import Image

def blur(image):
    new = image.copy()

    for y in range(1, image.height - 1):
        for x in range(1, image.width - 1):

            p1 = image.getpixel((x, y))
            p2 = image.getpixel((x-1, y))
            p3 = image.getpixel((x+1, y))
            p4 = image.getpixel((x, y-1))
            p5 = image.getpixel((x, y+1))

            r = (p1[0] + p2[0] + p3[0] + p4[0] + p5[0]) // 5
            g = (p1[1] + p2[1] + p3[1] + p4[1] + p5[1]) // 5
            b = (p1[2] + p2[2] + p3[2] + p4[2] + p5[2]) // 5

            new.putpixel((x, y), (r, g, b))

    return new


img = Image.open("input.jpg")
blurred = blur(img)
blurred.show()
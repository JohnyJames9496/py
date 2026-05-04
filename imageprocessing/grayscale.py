from PIL import Image

def grayscale(image):
  for y in range(image.height):
    for x in range(image.width):
      r,g,b = image.getpixel((x,y))

      gray = int(0.299*r + 0.587*g + 0.114*b)
      image.putpixel((x,y),(gray,gray,gray))


img = Image.open("input.jpg")
grayscale(img)
img.show()
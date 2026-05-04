from PIL import Image

def black_and_white(image):
  black_pixel = (0,0,0)
  white_pixel = (255,255,255)
  for y in range(image.height):
    for x in range(image.width):
      r,g,b = image.getpixel((x,y))
      avg = r+g+b//3

      if avg<128:
        image.putpixel((x,y),black_pixel)
      else :
        image.putpixel((x,y),white_pixel)


img = Image.open("input.jpg")
black_and_white(img)
img.show()
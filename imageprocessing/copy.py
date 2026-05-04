from PIL import Image

image = Image.open("input.jpg")

new_img = Image.new("RGB",image.size)

for y in range(image.height):
  for x in range(image.width):
      pixel = image.getpixel((x,y))
      new_img.putpixel((x,y),pixel)

new_img.show()
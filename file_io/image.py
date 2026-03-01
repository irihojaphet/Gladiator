from PIL import Image

def main():
   img = Image.open("in.jpg")
   img.close()

main()
from PIL import Image
import qrcode

def make_qr(data):
    img = qrcode.make(data)
    return img

def main():
    img = make_qr("stuff")
    print type(img)
    img.show()

if __name__ == '__main__':
    main()

from workermodule.djconnetinginterface import cutout
from rembg import remove
import cv2
from PIL import Image
import os


def cv2_imshow(a):
    a = a.clip(0, 255).astype("uint8")
    if a.ndim == 3:
        if a.shape[2] == 4:
            a = cv2.cvtColor(a, cv2.COLOR_BGRA2RGBA)
        else:
            a = cv2.cvtColor(a, cv2.COLOR_BGR2BGRA)
        return a
    else:
        return None


def rembg_algo(path):
    input = cv2.imread(path)
    output = remove(input)
    cv2.imwrite(path, output)


def motnet_algo(path):
    cutout(path)


def marge(img1, img2, pre):
    output_path = pre + " 23573498573495834795834789 " + ".png"
    marge = cv2.add(img1, img2)
    cv2.imwrite(output_path, marge)


def resize_image(path, width, height):
    input = cv2.imread(path)
    resize_image = cv2.resize(input, (width, height))
    cv2.imwrite(path, resize_image)


def center_crop_image(path, width, height):
    input = cv2.imread(path)

    print(input.shape)
    w = input.shape[1]
    h = input.shape[0]
    start_x = int((w / 2) - (width / 2))
    start_y = int((h / 2) - (height / 2))
    crop = input[start_y : start_y + height, start_x : start_x + width]
    cv2.imwrite(path, crop)


def remove_bacground_from_image(path, width=None, height=None):

    print(width)
    print(height)
    if width == None or height == None:
        pass
    else:
        if width < 0 or height < 0:
            pass
        else:
            try:
                resize_image(path, width, height)
            except:
                raise Exception("Resizing error")
    pre, ext = os.path.splitext(path)
    os.rename(path, f"{pre}.png")
    filename = path.split("/")[-1]
    try:
        rembg_algo(path)
    except:
        pass

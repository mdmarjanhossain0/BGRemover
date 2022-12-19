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


def remove_bacground_from_image(path):
    pre, ext = os.path.splitext(path)
    os.rename(path, f"{pre}.png")
    filename = path.split("/")[-1]
    rembg_algo(path)

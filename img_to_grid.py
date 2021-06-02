#! /usr/bin/env python3
import cv2 as cv
import numpy as np

def main():
    img = cv.imread("default_gzclient_camera.jpg", cv.IMREAD_GRAYSCALE)
    h, w = img.shape
    batch = 5
    for i in range(h):
        for j in range(w):

            if img[i, j] > 240:
                img[i, j] = 255
            else:
                img[i, j] = 0
    temp = np.array(img)
    map = temp[:(h//batch)*batch, :(w//batch)*batch].reshape(h//batch, batch, w//batch, batch).max(axis=(1, 3))
    cv.imwrite('map_org.jpg', img)
    cv.imwrite('./src/planning/scripts/map.jpg', map)

if __name__ == "__main__":
    main()
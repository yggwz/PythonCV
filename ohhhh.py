# 编写者:刘港
# 开发时间:2021/7/14 18:11
import copy
import os
import shutil

import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
react = []
img2 = []
file_numbers = 0
img = []
now_image = ''


def mouse_call_back(event, x, y, flags, param):
    global ix, iy, drawing, react, img2, img, now_image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        print('进入绘画模式')
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        img2 = img.copy()
        if drawing:
            cv2.rectangle(img2, (ix, iy), (x, y), (0, 0, 255), 1)
            cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False
            print('退出绘画模式,并开始记录本次绘画坐标')
            ix, x = (x, ix) if ix > x else (ix, x)
            iy, y = (y, iy) if iy > y else (iy, y)
            react.append([ix, iy, x, y])
            print([ix, iy, x, y])
            cv2.imwrite(now_image, img2)
            img = cv2.imread(now_image)


def set_attribute(output_folder):
    global img, now_image
    for picture in os.listdir(output_folder + '\\' + 'copy'):
        img = cv2.imread(output_folder + '\\' + 'copy' + '\\' + picture)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', mouse_call_back)
        now_image = output_folder + '\\' + 'copy' + '\\' + picture
        cv2.imshow('image', img)
        key = cv2.waitKey(0)
        if key == ord(' '):
            with open(output_folder+'\\'+os.path.splitext(picture)[0] + '.txt', 'w') as data_file:
                for i in range(len(react)):
                    data_file.write(str(react[i]))
                    if i < len(react) - 1:
                        data_file.write('\n')
            print('开始记录坐标到txt')
            print('该张图片警示框坐标开始如下')
            print(react)
            react.clear()
        else:
            break


# 获取文件夹中的图片数量并且在输出文件夹中建立副本
def get_picture_number_and_create_copy(target_folder, output_folder):
    global file_numbers
    os.mkdir(output_folder + '\\' + 'copy')
    for filename in os.listdir(target_folder):
        shutil.copy(target_folder + '\\' + filename, output_folder + '\\' + 'copy' + '\\' + filename)
        file_numbers += 1


if __name__ == '__main__':
    target = r'C:\Users\LGG\Desktop\arg'
    output = r'C:\Users\LGG\Desktop\111'
    get_picture_number_and_create_copy(target, output)
    set_attribute(output)

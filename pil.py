# 编写者:刘港
# 开发时间:2021/7/15 13:03
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np

img1 = cv2.imread('C:/Users/LGG/Desktop/arg/gakki_01.jpg', cv2.IMREAD_COLOR)

pil_image = Image.fromarray(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

font = ImageFont.truetype(r'C:\Windows\Fonts\FZSTK.TTF', 40, encoding='utf-8')
color = (0, 0, 255)
pos = (10, 150)
text = u'gakki是我老婆'

draw = ImageDraw.Draw(pil_image)
draw.text(pos, text, font=font, fill=color)

cv_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

cv2.imshow('image', cv_img)
cv2.waitKey(0)

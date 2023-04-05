import numpy as np
import os
from PIL import Image
root_path = './data/zalando-hd-resize/train/image-parse-v3-finetune/'

img_list = os.listdir(root_path)
for img_name in img_list:
    img = Image.open(root_path + img_name)
    img = img.convert('P')
    img.save(root_path + img_name)
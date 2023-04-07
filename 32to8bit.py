# import numpy as np
# import os
# from PIL import Image
# import cv2
# root_path = './00002_00.png'
# fname = open("changed.txt",'w')
# # img = cv2.imread(root_path)
# # img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
#
#
# img = cv2.imread('./new.png')
#
# # img = Image.open(root_path)
#
# # img = img.quantize(colors=256)
# # img.save('new.png', bitdepth=8)
#
#
# # cv2.waitKey(0)
# Xlenth = img.shape[1]
# Ylenth = img.shape[0]
# a = 1
# for i in range(Ylenth):
#     fname.write(str(a) + ':'+'\n')
#     for j in range(Xlenth):
#         fname.write(str(img[i][j])+' ')
#     a += 1
#     fname.write('\n')
#
#
#
# #
# #
# # img_list = os.listdir(root_path)
# # for img_name in img_list:
# #     img = Image.open(root_path + img_name)
# #     img = img.convert('P')
# #     img.save(root_path + img_name)
import torch
import torch.hub
from torchvision.transforms import *
from PIL import Image
from torchvision import utils
import cv2
import os

def read_image(path):
    return Image.open(path)

def save_image_tensor(input_tensor: torch.Tensor, filename):
    input_tensor = input_tensor.clone().detach()
    input_tensor = input_tensor.to(torch.device('cpu'))
    utils.save_image(input_tensor, filename)


# Create the model
model = torch.hub.load(
    repo_or_dir='guglielmocamporese/hands-segmentation-pytorch',
    model='hand_segmentor',
    pretrained=False
).cuda()

ckpt_path = './checkpoint/checkpoint.ckpt'
img_path = './data/zalando-hd-resize/train/image/'
save_path = './hand_seg/'

checkpoint = torch.load(ckpt_path)
img_list = os.listdir(img_path)

model.load_state_dict(checkpoint['state_dict'])
# Inference
model.eval()
preprocess = Compose([
    ToTensor(),
    Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

for curr_img_path in img_list:
    img = read_image(img_path + curr_img_path)
    img = preprocess(img).cuda()
    img = img.unsqueeze(0)       # [B, C, H, W]
    preds = model(img).argmax(1) # [B, H, W]
    preds = preds.squeeze().detach().cpu().numpy()
    cv2.imwrite(save_path + curr_img_path, preds*255)




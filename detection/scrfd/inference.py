import argparse

import cv2
import numpy as np
import torch

from backbones import get_model


@torch.no_grad()
def inference(weight, name, img):
    net = get_model(name, fp16=False)
    net.load_state_dict(torch.load(weight))
    net = net.cuda()
    net.eval()
    feat = net(img.cuda())
    return feat


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyTorch ArcFace Training')
    parser.add_argument('--network', type=str, default='r50', help='backbone network')
    parser.add_argument('--weight', type=str, default="C:/Users/DELL/Downloads/glint360k_cosface_r50_fp16_0.1_backbone.pth")
    parser.add_argument('--img', type=str, default="C:/Users/DELL/Desktop/face_det/111/0.jpg")
    args = parser.parse_args()
    inference(args.weight, args.network, args.img)

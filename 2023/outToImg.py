#!/bin/python3
from PIL import Image
import numpy as np

PIXSIZE = 1

inp =[list(line) for line in [l.strip() for l in open("out.txt","r").readlines() if len(l)>0]]
imgData = np.array([[np.array([255,255,255],dtype="uint8") if c=='.' else np.array([0,0,0],dtype="uint8") for c in line] for line in inp])

img = Image.fromarray(imgData,"RGB")

img.save("img.png")


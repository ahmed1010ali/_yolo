from ultralytics import YOLO
from PIL import Image
import numpy as np
import torch


class YoloModel:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available()else "cpu")
        self.model = YOLO("yolov8n.pt")
        self.model.to(self.device)
        self.model.eval()
        return
    
    @torch.no_grad()
    def predict(self, img):
        results = self.model.predict(img)
        result = results[0]
        result.save("output.jpg")
        result = Image.open('output.jpg')
        return result
    


model = YoloModel()
img_path = r"D:\Ahmed ali\AI Project\Yolo\attack-on-titan-7680x4320-21065.jpg"
model.predict(img_path)



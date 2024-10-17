
from ultralytics import YOLO
import cv2


model = YOLO("best.pt")

results=model("2.jpg",show=True)
cv2.waitKey(0)
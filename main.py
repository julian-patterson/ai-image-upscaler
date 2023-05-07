import cv2
from cv2 import dnn_superres

print(cv2.__version__)
sr = dnn_superres.DnnSuperResImpl_create()

image = cv2.imread("image.png")

path = "LapSRN_x8.pb"
sr.readModel(path)

sr.setModel("lapsrn", 8)

result = sr.upsample(image)
cv2.imwrite("./upscaled.png", result)
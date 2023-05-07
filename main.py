import cv2
from cv2 import dnn_superres

# Printing the version of the python library
print(cv2.__version__)
sr = dnn_superres.DnnSuperResImpl_create()

image_name = input('What is the file name of your image (include extension ex. ".png"): ')
image = cv2.imread(image_name)

path = input('Enter the model file name (ex. "LapSRN_x4.pb"): ')
sr.readModel(path)

model = input('Enter the model name (ex. "edsr", "fsrcnn", "lapsrn", "espcn): ')
factor = input('Enter the factor (2, 3, 4, 8) of upscaling (must correspond to the model used): ')
sr.setModel(model, factor)

result = sr.upsample(image)
cv2.imwrite("./upscaled.png", result)
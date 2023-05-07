## AI Image Upscaler

An AI image upscaler using different pretained models to upscale images by a factor of 2, 3, 4, and 8

## Installation

**This only works with Ubuntu based Linux Distributions**
**For other installation methods refer to [OpenCV's website](https://docs.opencv.org/4.x/df/d65/tutorial_table_of_content_introduction.html)**

### Clone this repository

`git clone https://github.com/julian-patterson/ai-image-upscaler`

### Install OpenCV with contrib modules

_Begin in the home directory folder_

Installing the neccessary prerequisites:
`sudo apt update && sudo apt install -y cmake g++ wget unzip`

Downloading and installing opencv packages:
`wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip`
`wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip`
`unzip opencv.zip`
`unzip opencv_contrib.zip`

Creating a build directory:
`mkdir -p build && cd build`

Configure:
`cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x`

Build:
`cmake --build .`
_Note this should take a while_

- Or else you can follow the installation guide at [OpenCV's website](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html)
- Be sure to "Build with opencv_contrib"

### Install pip libraries

- `pip install opencv-contrib-python`
- `pip install opencv-python`
- Make sure that opencv is above version 4.2.0 if not the packages can be upgrade using `pip install --upgrade opencv-contrib-python` and `pip install --upgrade opencv-python`

### Downloading pre-trained models

- You can download pretrained models [here](https://github.com/opencv/opencv_contrib/tree/master/modules/dnn_superres)
- The README also includes information on available models

## Use

- Please put all files in the same folder (model binary file, image, and main.py)
- After all the installation is done run main.py in a terminal
- This should result in an upscaled image

## Debugging

- Refer to [Open CV's Website](https://docs.opencv.org/4.x/index.html) for problems with Open CV
- Refer to the source code file for problems with the python file

## Credit

- This [article](https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066) for the tutorial

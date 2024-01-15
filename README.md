An unofficial wrapper of the [yolov7](https://github.com/WongKinYiu/yolov7.git) project.

It is very simple, and has only one function: `calculateDetections()`. 
Currently it only supports images, on CPU.

## Installation

```bash
pip install YOLOv7Detector
```

## Usage

```python
from YOLOv7Detector import Detector as det
from PIL import Image

def main():
    # Initialize the YOLO inference object
    detector = det(weights_path='yolov7.pt')

    # Load the image
    image = Image.open('image.jpg')

    dets = detector.calculateDetections(image, view_img=True)

    print(dets)


if __name__ == '__main__':
    main()

```

This returns a list of dictionaries, each dictionary is formatted as follows:
```python

{
    'class': 'person', 
    'confidence': 0.966009259223938, 
    'bbox': [31.0, 144.0, 469.0, 653.0]
}
```

where `bbox` is a list of `[x1, y1, x2, y2]` coordinates of the bounding box.
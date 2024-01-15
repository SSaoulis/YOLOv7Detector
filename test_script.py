from YOLOv7Detector.Detector import Detector as det
from PIL import Image


def main():
    # Initialize the YOLO inference object
    detector = det(weights_path='yolov7.pt')

    # Load the image
    image = Image.open('test_images/test_4.jpg')

    dets = detector.calculateDetections(image, view_img=True)

    print(dets)


if __name__ == '__main__':
    main()

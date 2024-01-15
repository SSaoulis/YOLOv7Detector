from YOLOv7Detector.Detector import Detector as det
from PIL import Image


def main():
    # Initialize the YOLO inference object
    detector = det(weights_path='yolov7.pt', conf_thres=0.7, iou_thres=0.45, img_size=640)

    # Load the image
    image = Image.open('test_images/test_4.jpg')

    download_path = 'test_images/test_4_result.jpg'  # Leave as None if not needed

    dets = detector.calculateDetections(image, view_img=True, download_path=download_path)

    print(dets)


if __name__ == '__main__':
    main()

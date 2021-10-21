# YOLO Object detection with OpenCV

## Requirements
* Python 3.5
* OpenCV
* yolov3.cfg
  * download from https://pjreddie.com/media/files/yolov3.weights
  * put the file such as `yolo-coco\yolov3.cfg`

## Running Detectors

### Image Detector

ex: `python yolo.py --image images/baggage_claim.jpg --yolo yolo-coco`

| Command      | Shortcut | Description                                    | Required | Default |
|--------------|----------|------------------------------------------------|----------|---------|
| --image      | -image   | path to image                                  | True     |         |
| --yolo       | -y       | base path to YOLO directory                    | True     |         |
| --confidence | -c       | minimum probability to filter weak detections  |          | 0.5     |
| --threshold  | -t       | threshold when applying non-maxima suppression |          | 0.3     |


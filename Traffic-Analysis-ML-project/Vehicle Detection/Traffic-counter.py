import tensorflow as tf
tf.config.list_physical_devices('GPU')

import os
os.environ['CUDA_VISIBLE-DEVICES'] = '0'

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
os.chdir(path)

HOME = path

SOURCE_VIDEO_PATH = f"{HOME}/vehicle-counting.mp4"

#!pip install ultralytics

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

#%cd {HOME}
#!git clone https://github.com/ifzhang/ByteTrack.git
#%cd {HOME}/ByteTrack

# workaround related to https://github.com/roboflow/notebooks/issues/80
#!sed -i 's/onnx==1.8.1/onnx==1.9.0/g' requirements.txt

#!pip3 install -q -r requirements.txt
#!python3 setup.py -q develop
#!pip install -q cython_bbox
#!pip install -q onemetric

from IPython import display
display.clear_output()


import sys
sys.path.append(f"{HOME}/ByteTrack")


import yolox
print("yolox.__version__:", yolox.__version__)

from yolox.tracker.byte_tracker import BYTETracker, STrack
from onemetric.cv.utils.iou import box_iou_batch
from dataclasses import dataclass


@dataclass(frozen=True)
class BYTETrackerArgs:
    track_thresh: float = 0.25
    track_buffer: int = 30
    match_thresh: float = 0.8
    aspect_ratio_thresh: float = 3.0
    min_box_area: float = 1.0
    mot20: bool = False
    
#!pip install supervision==0.1.0


from IPython import display
display.clear_output()


import supervision
print("supervision.__version__:", supervision.__version__)    


from supervision.draw.color import ColorPalette
from supervision.geometry.dataclasses import Point
from supervision.video.dataclasses import VideoInfo
from supervision.video.source import get_video_frames_generator
from supervision.video.sink import VideoSink
from supervision.notebook.utils import show_frame_in_notebook
from supervision.tools.detections import Detections, BoxAnnotator
from supervision.tools.line_counter import LineCounter, LineCounterAnnotator

from typing import List

import numpy as np


# converts Detections into format that can be consumed by match_detections_with_tracks function
def detections2boxes(detections: Detections) -> np.ndarray:
    return np.hstack((
        detections.xyxy,
        detections.confidence[:, np.newaxis]
    ))


# converts List[STrack] into format that can be consumed by match_detections_with_tracks function
def tracks2boxes(tracks: List[STrack]) -> np.ndarray:
    return np.array([
        track.tlbr
        for track
        in tracks
    ], dtype=float)


# matches our bounding boxes with predictions
def match_detections_with_tracks(
    detections: Detections, 
    tracks: List[STrack]
) -> Detections:
    if not np.any(detections.xyxy) or len(tracks) == 0:
        return np.empty((0,))

    tracks_boxes = tracks2boxes(tracks=tracks)
    iou = box_iou_batch(tracks_boxes, detections.xyxy)
    track2detection = np.argmax(iou, axis=1)
    
    tracker_ids = [None] * len(detections)
    
    for tracker_index, detection_index in enumerate(track2detection):
        if iou[tracker_index, detection_index] != 0:
            tracker_ids[detection_index] = tracks[tracker_index].track_id

    return tracker_ids

# settings
MODEL = "yolov8x.pt"

from ultralytics import YOLO

model = YOLO(MODEL)
model.fuse()

# dict maping class_id to class_name
CLASS_NAMES_DICT = model.model.names
# class_ids of interest - car, motorcycle, bus and truck
CLASS_ID = [2, 3, 5, 7]

# settings
LINE_START = Point(50, 1500)
LINE_END = Point(3840-50, 1500)

VideoInfo.from_video_path(SOURCE_VIDEO_PATH)
TARGET_VIDEO_PATH = f"{HOME}/vehicle-counting-result1.mp4"

from tqdm.notebook import tqdm
import time

# create BYTETracker instance
byte_tracker = BYTETracker(BYTETrackerArgs())
# create VideoInfo instance
video_info = VideoInfo.from_video_path(SOURCE_VIDEO_PATH)
# create frame generator
generator = get_video_frames_generator(SOURCE_VIDEO_PATH)
# create LineCounter instance
line_counter = LineCounter(start=LINE_START, end=LINE_END)
# create instance of BoxAnnotator, LineCounterAnnotator, and Speedometer
box_annotator = BoxAnnotator(color=ColorPalette(), thickness=4, text_thickness=4, text_scale=2)
line_annotator = LineCounterAnnotator(thickness=4, text_thickness=4, text_scale=2)


# initialize counts for each class
class_counts = {class_id: 0 for class_id in CLASS_ID}
# initialize dictionary to keep track of already counted vehicles
counted_vehicles = {}

# open target video file
with VideoSink(TARGET_VIDEO_PATH, video_info) as sink:
    # loop over video frames
    for frame in tqdm(generator, total=video_info.total_frames):

        # model prediction on single frame and conversion to supervision Detections
        
        results = model(frame)
        detections = Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int)
        )
        # filtering out detections with unwanted classes
        mask = np.array([class_id in CLASS_ID for class_id in detections.class_id], dtype=bool)
        detections.filter(mask=mask, inplace=True)
        # tracking detections
        tracks = byte_tracker.update(
            output_results=detections2boxes(detections=detections),
            img_info=frame.shape,
            img_size=frame.shape
        )
        tracker_id = match_detections_with_tracks(detections=detections, tracks=tracks)
        detections.tracker_id = np.array(tracker_id)
        # filtering out detections without trackers
        mask = np.array([tracker_id is not None for tracker_id in detections.tracker_id], dtype=bool)
        detections.filter(mask=mask, inplace=True)
        # loop over detections
        
        for bbox, confidence, class_id, tracker_id in detections:
            # check if vehicle has already been counted
            if tracker_id not in counted_vehicles:
                # increment count for class
                class_counts[class_id] += 1
                # add vehicle to counted vehicles
                counted_vehicles[tracker_id] = True 
       
        labels = [
        f"#{tracker_id} {CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
        for _, confidence, class_id, tracker_id
        in detections
        ]
        # updating line counter
        line_counter.update(detections=detections)
        # annotate and display frame
        frame = box_annotator.annotate(frame=frame, detections=detections, labels=labels)
        line_annotator.annotate(frame=frame, line_counter=line_counter)
        sink.write_frame(frame)


confidence_probability = 0.5
for class_id in CLASS_ID:
    class_name = CLASS_NAMES_DICT[class_id]
    count = class_counts[class_id]
    print(f"{class_name}: {int(count*confidence_probability)}")  
    
import pandas as pd

vehicles = ['Motocycle','Car','Bus','Truck']
col = ['Vehicles','Frequency']
Frequency = ([int(class_counts[3]*confidence_probability),int(class_counts[2]*confidence_probability),int(class_counts[5]*confidence_probability),int(class_counts[7]*confidence_probability)])
df = pd.DataFrame(list(zip(vehicles,Frequency)), columns=col )
print(df)


df.to_excel(r'..\Results\VOLUME STUDY\volume-data.xlsx',index = False)    
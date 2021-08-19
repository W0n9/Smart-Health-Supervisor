import numpy as np
import torch
import torch.nn as nn
import cv2
from faces_detect import faces_detect
from inference import inference
from db_feature_extract import encode
from multiprocessing import Queue, Process


def main(config, checkpoint, queue, source = 0, score_thr=0.7):
    frame_count = 0
    cap = cv2.VideoCapture(source)

    while True:
        frame_count += 1
        ret, frame = cap.read()

        if frame_count % 10 == 0:
            detected_faces, bboxes = faces_detect(frame, config=config, checkpoint=checkpoint, score_thr=score_thr)
            if len(detected_faces) > 0:
                message = detected_faces
                queue.put(message)

        if frame is None:
            message = frame
            queue.put(message)
            break 
    cap.release()

def recognize(model_path, model_name, queue, db_embeddings, labels):
    while True:
        try:
            detected_faces = queue.get(True)
            detected_faces = torch.stack(detected_faces)
            embeddings = inference(model_path, model_name, detected_faces)
            # calculate distance metric (cosine similarity)
            normed_embeddings = nn.functional.normalize(embeddings, p=2, dim=1)
            normed_db_embeddings = nn.functional.normalize(db_embeddings, p=2, dim=1)
            normed_db_embeddings = normed_db_embeddings.cuda()
            sim = normed_embeddings@normed_db_embeddings.t()
            pred = torch.max(sim, dim=1)[1]
            pred_labels = [labels[t] for t in pred]
            dist_metric = torch.max(sim, dim=1)[0]
            for f in range(len(pred_labels)):
                print(pred_labels[f], dist_metric[f].item())
        except TypeError:
            break

if __name__ == '__main__':
    db_embeddings, labels = encode(db_path="D:/face/database_aligned/", 
                                   model_path="C:/Users/DELL/Downloads/ms1mv3_arcface_r50_fp16_backbone.pth", 
                                   model_name='r50')
    mq = Queue()
    recognizer_process = Process(target=recognize, args=("C:/Users/DELL/Downloads/ms1mv3_arcface_r50_fp16_backbone.pth", 'r50', mq, db_embeddings, labels))
    detector_process1 = Process(target=main, args=('D:/face/insightface/detection/scrfd/configs/scrfd/scrfd_500m.py', 
                                                  'D:/face/insightface/detection/scrfd_500m_model.pth', mq, 
                                                  'C:/Users/DELL/Desktop/face_det/1_20210819-1140.mkv', 0.7))
    detector_process2 = Process(target=main, args=('D:/face/insightface/detection/scrfd/configs/scrfd/scrfd_500m.py', 
                                                  'D:/face/insightface/detection/scrfd_500m_model.pth', mq, 
                                                  'C:/Users/DELL/Desktop/face_det/1_20210819-1140.mkv', 0.7))
    detector_process1.start()
    detector_process2.start()
    recognizer_process.start()

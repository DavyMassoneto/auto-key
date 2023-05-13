import cv2
import os


class FrameExtractor:
    def __init__(self, video_path, output_folder, n=30):
        self.video_path = video_path
        self.output_folder = output_folder
        self.n = n

    def extract_frames(self):
        video = cv2.VideoCapture(self.video_path)

        if not video.isOpened():
            raise ValueError(f"Cannot open video file: {self.video_path}")

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        frame_num = 0

        # Use grab and retrieve to improve efficiency when skipping frames
        while True:
            ret = video.grab()
            if not ret:
                break

            if frame_num % self.n == 0:
                ret, frame = video.retrieve()
                frame_file = os.path.join(self.output_folder, f'frame{frame_num}.png')
                cv2.imwrite(frame_file, frame)
            frame_num += 1

        video.release()


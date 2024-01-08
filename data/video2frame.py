import os
import cv2
import argparse
from tqdm import tqdm


def FrameCapture(video_path, output_path):
    vidObj = cv2.VideoCapture(video_path)
    count = 1
    success = 1
    while success:
        success, image = vidObj.read()

        # to gray
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        if success:
            # cv2.imwrite(output_path + "/%d.png" % count, image)
            cv2.imwrite(output_path + "/f%03d.png" % count, image)
            cv2.imwrite(output_path + "/f%03d_gray.png" % count, gray)
            count += 1


def video2frame():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default=".", help="path of input videos")
    parser.add_argument("--output", type=str, default="frames", help="path of output clips")
    opt = parser.parse_args()

    video_path = opt.input
    output_path = opt.output
    os.makedirs(output_path, exist_ok=True)
    
    videos = [video for video in os.listdir(video_path) if video.endswith(".avi") or video.endswith(".mp4") or video.endswith(".mkv")]
    videos.sort()
    print(videos)

    print(f"Extracting frames from {len(videos)} videoes in {video_path} ...")
    for video in tqdm(videos):
        frame_path = os.path.join(output_path, video.split(".")[0])
        os.makedirs(frame_path, exist_ok=True)
        FrameCapture(os.path.join(video_path, video), frame_path)
    print('Done.')


if __name__ == "__main__":
    video2frame()

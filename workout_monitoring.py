# https://docs.ultralytics.com/guides/workouts-monitoring/#real-world-applications
from ultralytics import YOLO
from ultralytics.solutions import ai_gym
import cv2

model = YOLO("yolov8n-pose.pt")
# cap = cv2.VideoCapture("pullups.mp4")
cap = cv2.VideoCapture("abworkout.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("abworkout_detect.mp4",
                                cv2.VideoWriter_fourcc(*'mp4v'),
                                fps,
                                (w, h))

gym_object = ai_gym.AIGym()  # init AI GYM module
gym_object.set_args(line_thickness=2,
                    view_img=True,
                    pose_type="abworkout",
                    kpts_to_check=[6, 8, 10])

frame_count = 0
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
      print("Video frame is empty or video processing has been successfully completed.")
      break
    frame_count += 1
    results = model.predict(im0, verbose=False)
    im0 = gym_object.start_counting(im0, results, frame_count)
    video_writer.write(im0)

cv2.destroyAllWindows()
video_writer.release()
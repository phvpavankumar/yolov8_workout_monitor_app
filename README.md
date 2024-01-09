# Workout Monitoring with YOLOv8

This repository contains a workflow for monitoring body workout exercises such as pushups and pullups using YOLOv8, an object detection model by Ultralytics. The workflow is designed to detect and track exercises in video footage, enabling real-time analysis of workout routines.

## Features

- Utilizes YOLOv8 by Ultralytics for object detection and pose estimation.
- Monitors and tracks pushups and pullups within workout videos.
- Provides real-time analysis of exercise counts and durations.
- Customizable for different workout routines and exercises.

## Requirements

- YOLOv8 by Ultralytics (Refer to Ultralytics' [YOLOv8 repository](https://github.com/ultralytics/ultralytics/) for installation instructions)
- Python 3.x
- OpenCV
- [Optional] GPU for faster inference

## Usage

1. **Setup YOLOv8**: Ensure YOLOv8 by Ultralytics is properly installed as per the instructions provided in their repository.

2. **Clone Repository**:
   ```bash
   git clone https://github.com/phvpavankumar/yolov8_workout_monitor_app.git
   cd yolov8_workout_monitor_app
   git clone https://github.com/ultralytics/ultralytics.git
   cd ultralytics
   ```
3. **Install Requirments**
   ```bash
   pip install ultralytics
   ```
3. **Prepare Videos**: Place workout videos or live video feeds in the designated directory.

4. **Run Workflow**:
   ```bash
   python workout_monitoring.py
   ```

5. **Monitor Exercise Stats**: The workflow will detect pushups and pullups in the video and provide real-time statistics such as counts and durations.

## Customization

- Modify `workout_monitor.py` to add support for additional exercises or workout routines.
- Adjust detection thresholds and settings in YOLOv8 configuration files for better accuracy.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or additional features.


## Acknowledgements

- Ultralytics article: [article](https://docs.ultralytics.com/guides/workouts-monitoring/)
- YOLOv8 by Ultralytics: [Ultralytics YOLOv5 Repository](https://github.com/ultralytics/ultralytics/)
- OpenCV: [OpenCV Python](https://github.com/opencv/opencv-python)


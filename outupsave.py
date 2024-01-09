import cv2

# Open the four video files
video1 = cv2.VideoCapture('Pushups.mp4')
video2 = cv2.VideoCapture('pushup_detect.mp4')
video3 = cv2.VideoCapture('pullups.mp4')
video4 = cv2.VideoCapture('pullups_detect.mp4')

# Get video properties
fps = video1.get(cv2.CAP_PROP_FPS)
width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('FinalResults.mp4', fourcc, fps, (2*width, 2*height))

while True:
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()

    if not (ret1 and ret2 and ret3 and ret4):
        break

    # Create a 2x2 grid for the videos
    combined_frame = cv2.vconcat([cv2.hconcat([frame1, frame2]), cv2.hconcat([frame3, frame4])])

    # Write the combined frame to the output video
    output.write(combined_frame)

    cv2.imshow('Combined Videos', combined_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video objects and close the window
video1.release()
video2.release()
video3.release()
video4.release()
output.release()
cv2.destroyAllWindows()

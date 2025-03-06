import cv2
import os
import time

def capture_cam_img():

    # Create directory if it does not exist
    directory = 'images'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Capture four images automatically
    for i in range(4):
        # Access the camera
        camera = cv2.VideoCapture(0)

        # Check if camera opened successfully
        if not camera.isOpened():
            print("Error: Could not open camera.")
            exit()

        # Capture frame-by-frame
        ret, frame = camera.read()
        # Save the captured frame to the specified directory
        img=cv2.imwrite(os.path.join(directory, f'captured_image_{i+1}.jpg'), frame)
        print(f"Image {i+1} saved in:", directory)

        # Release the camera
        camera.release()

        # Add delay before capturing the next image
        time.sleep(1)  # Delay for 2 seconds

    # Destroy all windows
    cv2.destroyAllWindows()

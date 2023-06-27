import cv2
from physical_exercises.main import process_exercise_frame

class VideoCamera(object):
    def __init__(self):
        self.video = None
        for cam_id in [0, 1]:
            cap = cv2.VideoCapture(cam_id)
            if cap.isOpened():
                self.video = cap
                break

        if self.video is None:
            raise Exception("Could not open any video device")

    def __del__(self):
        self.video.release()

    def get_frame(self,selected_exercise):
        success, image = self.video.read()
        # image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image=process_exercise_frame(image,selected_exercise)
        
        # Check if the camera read frame correctly
        assert success, "Could not read video frame"
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

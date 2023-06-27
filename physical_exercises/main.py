import cv2
import mediapipe as mp
from physical_exercises.exercises import Exercises

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def process_exercise_frame(frame,selected_exercise,exercise_name=None, status=None):
    image_in_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    resultant = pose.process(image_in_RGB)
    
    try:
        landmarks=resultant.pose_landmarks.landmark
        exercise_name,status=Exercises(landmarks).exercise_tracking(exercise_name,status)
    except:
        pass
    if resultant.pose_landmarks:   

        mp_drawing.draw_landmarks(
            frame,
            resultant.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp.solutions.drawing_styles.get_default_pose_landmarks_style())
    
        
        position_color=(0,0,255)
        doing_exercise="Wrong"
        if exercise_name==selected_exercise:
            doing_exercise="Right"
            position_color=(0,255,0)
        else:
            doing_exercise="Wrong"
            position_color=(0,0,255)

        cv2.rectangle(frame, (0,0), (600,90), (0,0,0), -1)
        cv2.putText(frame, "Patient selected exercise : " + str(selected_exercise),
                    (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, "Doing exercise: " + str(exercise_name),
                    (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255,255,255), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, "Status: " + str(doing_exercise),
                    (5, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.65, position_color, 2,
                    cv2.LINE_AA)
        
    return frame

import mediapipe as mp
import cv2
import numpy as np
import pandas as pd


mp_pose = mp.solutions.pose

def find_body_landmark(landmarks, body_part_name):
    return[
        landmarks[mp_pose.PoseLandmark[body_part_name].value].x,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].y,
        landmarks[mp_pose.PoseLandmark[body_part_name].value].visibility
    ]
def calculate_distance(p1,p2):
    dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return dis

def body_parts_angle_calculation(b_part1,b_part2,b_part3):
    b_part1= np.array(b_part1)
    b_part2= np.array(b_part2)
    b_part3= np.array(b_part3)

    r = np.arctan2(b_part3[1]-b_part2[1],b_part3[0]-b_part2[0])-np.arctan2(b_part1[1]-b_part2[1],b_part1[0]-b_part2[0])

    angle=np.abs(r*180.0/np.pi)

    if angle>180.0:
        angle = 360-angle
    
    return angle

class Angle:
    def __init__(self,landmarks):
        self.landmarks=landmarks

    def body_points_distance_calculation(self,p1_name, p2_name):
        land_marks1 = find_body_landmark(self.landmarks,p1_name)
        land_marks2 = find_body_landmark(self.landmarks,p2_name)
        dis=calculate_distance(land_marks1,land_marks2)
        # print(dis)
        return dis

    def left_arm_angle(self):
        left_shoulder = find_body_landmark(self.landmarks,"LEFT_SHOULDER")
        left_elbow = find_body_landmark(self.landmarks,"LEFT_ELBOW")
        left_wrist = find_body_landmark(self.landmarks,"LEFT_WRIST")
        angle=body_parts_angle_calculation(left_shoulder,left_elbow,left_wrist)
        # print("arm angle: ",angle)
        return angle
    def right_arm_angle(self):
        right_shoulder = find_body_landmark(self.landmarks,"RIGHT_SHOULDER")
        right_elbow = find_body_landmark(self.landmarks,"RIGHT_ELBOW")
        right_wrist = find_body_landmark(self.landmarks,"RIGHT_WRIST")
        angle=body_parts_angle_calculation(right_shoulder,right_elbow,right_wrist)
        # print("arm angle: ",angle)
        return angle
    
    def left_hip_angle(self):
        left_shoulder = find_body_landmark(self.landmarks,"LEFT_SHOULDER")
        left_hip = find_body_landmark(self.landmarks,"LEFT_HIP")
        left_ankle = find_body_landmark(self.landmarks,"LEFT_ANKLE")
        angle=body_parts_angle_calculation(left_shoulder,left_hip,left_ankle)
        # print("hip angle: ",angle)
        return angle
    def left_knee_hip_shoulder_angle(self):
        left_knee = find_body_landmark(self.landmarks,"LEFT_KNEE")
        left_hip = find_body_landmark(self.landmarks,"LEFT_HIP")
        left_shoulder = find_body_landmark(self.landmarks,"LEFT_SHOULDER")
        angle=body_parts_angle_calculation(left_knee,left_hip,left_shoulder)
        # print("hip angle: ",angle)
        return angle
    def left_wrist_shoulder_hip_angle(self):
        left_wrist = find_body_landmark(self.landmarks,"LEFT_WRIST")
        left_hip = find_body_landmark(self.landmarks,"LEFT_HIP")
        left_shoulder = find_body_landmark(self.landmarks,"LEFT_SHOULDER")
        angle=body_parts_angle_calculation(left_wrist,left_shoulder,left_hip)
        # print("hip angle: ",angle)
        return angle
    def right_wrist_shoulder_hip_angle(self):
        right_wrist = find_body_landmark(self.landmarks,"RIGHT_WRIST")
        right_hip = find_body_landmark(self.landmarks,"RIGHT_HIP")
        right_shoulder = find_body_landmark(self.landmarks,"RIGHT_SHOULDER")
        angle=body_parts_angle_calculation(right_wrist,right_shoulder,right_hip)
        # print("hip angle: ",angle)
        return angle
    
    def left_wrist_shoulder_mouth_angle(self):
        left_wrist = find_body_landmark(self.landmarks,"LEFT_WRIST")
        left_shoulder = find_body_landmark(self.landmarks,"LEFT_SHOULDER")
        left_mouth = find_body_landmark(self.landmarks,"MOUTH_LEFT")
        angle=body_parts_angle_calculation(left_wrist,left_shoulder,left_mouth)
        # print("mouth angle: ",angle)
        return angle
    def right_knee_hip_shoulder_angle(self):
        right_knee = find_body_landmark(self.landmarks,"RIGHT_KNEE")
        right_hip = find_body_landmark(self.landmarks,"RIGHT_HIP")
        right_shoulder = find_body_landmark(self.landmarks,"RIGHT_SHOULDER")
        angle=body_parts_angle_calculation(right_knee,right_hip,right_shoulder)
        # print("right hip angle: ",angle)
        return angle
    def left_foot_hip_right_foot_angle(self):
        left_foot_index = find_body_landmark(self.landmarks,"LEFT_FOOT_INDEX")
        right_hip = find_body_landmark(self.landmarks,"RIGHT_HIP")
        right_foot_index = find_body_landmark(self.landmarks,"RIGHT_FOOT_INDEX")
        angle=body_parts_angle_calculation(right_foot_index,right_hip,left_foot_index)
        # print("right hip angle: ",angle)
        return angle
    
    def left_hip_knee_foot_angle(self):
        left_knee = find_body_landmark(self.landmarks,"LEFT_KNEE")
        left_hip = find_body_landmark(self.landmarks,"LEFT_HIP")
        left_foot_index = find_body_landmark(self.landmarks,"LEFT_FOOT_INDEX")
        angle=body_parts_angle_calculation(left_hip,left_knee,left_foot_index)
        # print("left knee angle: ",angle)
        return angle
    
    def right_hip_knee_foot_angle(self):
        right_knee = find_body_landmark(self.landmarks,"RIGHT_KNEE")
        right_hip = find_body_landmark(self.landmarks,"RIGHT_HIP")
        right_foot_index = find_body_landmark(self.landmarks,"RIGHT_FOOT_INDEX")
        angle=body_parts_angle_calculation(right_hip,right_knee,right_foot_index)
        # print("right knee angle: ",angle)
        return angle
    
    def right_shoulder_hip_foot_angle(self):
        right_shoulder = find_body_landmark(self.landmarks,"RIGHT_SHOULDER")
        right_hip = find_body_landmark(self.landmarks,"RIGHT_HIP")
        right_foot_index = find_body_landmark(self.landmarks,"RIGHT_FOOT_INDEX")
        angle=body_parts_angle_calculation(right_shoulder,right_hip,right_foot_index)
        # print("right hip angle: ",angle)
        return angle
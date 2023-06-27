from physical_exercises.angles import Angle
import numpy as np



class Exercises(Angle):
    def __init__(self, landmarks):
        super().__init__(landmarks)
    
    def get_exercise_type(self,exercise_name,stauts):
        l_arm_angle=self.left_arm_angle()
        r_arm_angle=self.right_arm_angle()
        l_hip_angle=self.left_hip_angle()
        l_knee_hip_shoulder_angle=self.left_knee_hip_shoulder_angle()
        l_wrist_shoulder_hip_angle=self.left_wrist_shoulder_hip_angle()
        r_wrist_shoulder_hip_angle=self.rignt_wrist_shoulder_hip_angle()
        l_wrist_shoulder_mouth_angle=self.left_wrist_shoulder_mouth_angle()
        r_knee_hip_shoulder_angle=self.right_knee_hip_shoulder_angle()
        l_foot_hip_r_foot_angle=self.left_foot_hip_right_foot_angle()
        l_hip_knee_foot_angle=self.left_hip_knee_foot_angle()
        r_hip_knee_foot_angle=self.right_hip_knee_foot_angle()
        r_shoulder_hip_foot_angle=self.right_shoulder_hip_foot_angle()

        
        dis_btw_left_right_foot=self.body_points_distance_calculation("LEFT_FOOT_INDEX","RIGHT_FOOT_INDEX")
        dis_btw_left_right_knee=self.body_points_distance_calculation("LEFT_KNEE","RIGHT_KNEE")
        dis_btw_left_heel_right_knee=self.body_points_distance_calculation("LEFT_HEEL","RIGHT_KNEE")
        dis_btw_right_heel_left_knee=self.body_points_distance_calculation("RIGHT_HEEL","LEFT_KNEE")
        # print(dis_btw_left_heel_right_knee,dis_btw_right_heel_left_knee)


        # if stauts:
        if (l_arm_angle>110.0 and l_arm_angle<155.0) and (l_hip_angle>=170.0 and l_hip_angle<=173.0):
            exercise_name="lumbar extension"
            stauts=False
        elif (l_knee_hip_shoulder_angle>=90 and l_knee_hip_shoulder_angle<120)and(l_wrist_shoulder_hip_angle>=65 and l_wrist_shoulder_hip_angle<=90)\
        and (l_wrist_shoulder_mouth_angle>0 and l_wrist_shoulder_mouth_angle<=25):
            exercise_name="cat and camel"
            stauts=False
        elif (l_knee_hip_shoulder_angle>=100 and l_knee_hip_shoulder_angle<170) and (r_knee_hip_shoulder_angle>=100 and r_knee_hip_shoulder_angle<170)\
        and dis_btw_left_right_foot<0.019 and dis_btw_left_right_knee<=1.5 and (l_arm_angle>70 and l_arm_angle<115):
            exercise_name="Clamshells"
            stauts=False
        elif (l_foot_hip_r_foot_angle>=60.0 and l_foot_hip_r_foot_angle<=90):
            exercise_name="Hip Leg Flexion"
        elif ((l_arm_angle>170 and l_arm_angle<=180) and (r_arm_angle>170 and r_arm_angle<=180)) and ((l_wrist_shoulder_hip_angle>70 and l_wrist_shoulder_hip_angle<110) and\
                (r_wrist_shoulder_hip_angle>70 and r_wrist_shoulder_hip_angle<110)) and (l_hip_knee_foot_angle>170 and r_hip_knee_foot_angle>170):
            exercise_name="Lateral Raises Two hand"
            stauts=False
        elif ((l_arm_angle>90 and l_arm_angle<=180) and (r_arm_angle>170 and r_arm_angle<=180)) and ((l_wrist_shoulder_hip_angle>0 and l_wrist_shoulder_hip_angle<10) and\
                (r_wrist_shoulder_hip_angle>70 and r_wrist_shoulder_hip_angle<110)) and (l_hip_knee_foot_angle>170 and r_hip_knee_foot_angle>170):
            exercise_name="Right Hand Lateral Raises"
            stauts=False
        elif (l_knee_hip_shoulder_angle>140 and l_knee_hip_shoulder_angle<180) and (l_hip_knee_foot_angle>70 and l_hip_knee_foot_angle<90) and ((l_arm_angle>160 and l_arm_angle<=180)or (r_arm_angle>160 and r_arm_angle<=180)):
            exercise_name="Glute Bridge"
            stauts=False
        elif (((l_hip_knee_foot_angle>50 and l_hip_knee_foot_angle<=90) and (r_hip_knee_foot_angle>160 and r_hip_knee_foot_angle<=180)and (dis_btw_left_heel_right_knee<0.09))or \
              ((r_hip_knee_foot_angle>50 and r_hip_knee_foot_angle<=90) and (l_hip_knee_foot_angle>160 and l_hip_knee_foot_angle<=180)and (dis_btw_right_heel_left_knee<0.09))):
            exercise_name="Mobility Hip Standing"
            stauts=False
        elif (r_hip_knee_foot_angle>65 and r_hip_knee_foot_angle<=90) and (r_knee_hip_shoulder_angle>130 and r_knee_hip_shoulder_angle<=150) :
            exercise_name="Knee flexion spine extension"
            stauts=False
        elif (r_shoulder_hip_foot_angle>60 and r_shoulder_hip_foot_angle<=75) and (r_arm_angle>160 and r_arm_angle<=180):
            exercise_name="Upper back flexion"
            stauts=False
        else:
            exercise_name="None"
        
        return [exercise_name,stauts]



    
    def exercise_tracking(self,exercise_name,status):
        
        exercise_name,status=Exercises(self.landmarks).get_exercise_type(exercise_name,status)
        return [exercise_name,status]
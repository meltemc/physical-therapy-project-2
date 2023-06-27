from flask import Flask, render_template, jsonify,request,Response
from camera import VideoCamera
import cv2
import numpy as np
import base64

app = Flask(__name__)

# Add your items here
exercises = ['lumbar extension', 'cat and camel', 'Clamshells', \
                        'Hip Leg Flexion', 'Lateral Raises Two hand', \
                        'Right Hand Lateral Raises', 'Glute Bridge', \
                        'Mobility Hip Standing', 'Knee flexion spine extension',\
                        'Upper back flexion']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-exercises', methods=['GET'])
def get_exercises():
    return jsonify(exercises)

def gen(camera,selected_exercise):
    print("selected_exercise",selected_exercise)
    while True:
        frame = camera.get_frame(selected_exercise)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    selected_exercise = request.args.get('exercise', default=None, type=str)
    return Response(gen(VideoCamera(), selected_exercise),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(gen(VideoCamera()),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

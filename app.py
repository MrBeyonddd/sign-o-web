from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
import cv2

from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

def generate_frames(camera):
  while True:
    frame = camera.get_frame()
    # encode as a jpeg image and return it (flask stuffs)
    yield(b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
  return Response(generate_frames(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
  app.run(debug=True)
 

from flask import Flask, render_template, Response
import motor_control
import servo_control
from camera_stream import generate_frames


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
               
@app.route('/forward')
def forward():
    motor_control.forward()
    return ('', 204)

@app.route('/backward')
def backward():
    motor_control.backward()
    return ('', 204)

@app.route('/left')
def left():
    motor_control.left()
    return ('', 204)

@app.route('/right')
def right():
    motor_control.right()
    return ('', 204)

@app.route('/stop')
def stop():
    motor_control.stop()
    return ('', 204)

# Pan/Tilt endpoints
@app.route('/pan_left')
def pan_left():
    servo_control.pan_left()
    return ('', 204)

@app.route('/pan_right')
def pan_right():
    servo_control.pan_right()
    return ('', 204)

@app.route('/tilt_up')
def tilt_up():
    servo_control.tilt_up()
    return ('', 204)

@app.route('/tilt_down')
def tilt_down():
    servo_control.tilt_down()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


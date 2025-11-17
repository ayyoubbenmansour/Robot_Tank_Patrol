from picamera2 import Picamera2
import cv2

picam2 = Picamera2()
camera_config = picam2.create_video_configuration(main={"size": (640, 480)})
picam2.configure(camera_config)
picam2.start()

def generate_frames():
    while True:
        frame = picam2.capture_array()

        # ? Convert BGR ? RGB (fixes wrong colors)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ? Encode to JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')


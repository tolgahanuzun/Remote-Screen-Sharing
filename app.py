import pyscreenshot as ImageGrab
import time
from io import BytesIO

from flask import Flask, render_template, Response, send_file, stream_with_context
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

def screen_grab():
    while True:
        img_buffer = BytesIO()
        ImageGrab.grab().save(img_buffer, 'PNG', quality=1)
        img_buffer.seek(0)
        yield  (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img_buffer.read() + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video_feed():
    return Response(screen_grab(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
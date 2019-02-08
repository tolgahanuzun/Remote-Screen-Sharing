import pyscreenshot as ImageGrab
import time
from io import BytesIO

from flask import Flask, render_template, Response, send_file, stream_with_context
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False
app.config['PROPAGATE_EXCEPTIONS'] = False
app.config['DEBUG'] = False

run_with_ngrok(app)

def screen_grab():
    while True:
        time.sleep(0.3)
        img_buffer = BytesIO()
        ImageGrab.grab().save(img_buffer, 'PNG', quality=1)
        img_buffer.seek(0)
        yield  (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + img_buffer.read() + b'\r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record')
def record_feed():
    return Response(screen_grab(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
    time.sleep(0.3)
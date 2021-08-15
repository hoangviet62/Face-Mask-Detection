from flask import Flask, render_template, Response, redirect, url_for
from detect_mask_camera import read_frame

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/')
def index():
  return render_template('index.html')

def gen_frame():
  while True:
    frame = read_frame()
    yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result


@app.route('/streaming')
def streaming():
  return Response(gen_frame(),
                  mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
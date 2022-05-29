from flask import Flask, render_template, Response
from camera import VideoCamera, attendance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    with open('Attendance.csv') as myfile:
        attendance_list = myfile.readlines()
        attendance_list = [x.split(',') for x in attendance_list]
    return render_template('attendance.html', attendance_list=attendance_list[2:])

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video-feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)

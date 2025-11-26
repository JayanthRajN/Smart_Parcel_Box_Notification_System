
import RPi.GPIO as GPIO
import time
from flask import Flask

# GPIO setup
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

app = Flask(__name__)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # cm
    return distance

@app.route('/')
def index():
    distance = get_distance()
    if distance < 10:  # adjust for your box size
        return "📦 Parcel Detected!"
    else:
        return "🕳️ Box is Empty."
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

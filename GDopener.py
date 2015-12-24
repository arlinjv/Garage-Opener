from flask import Flask, render_template, g, request, redirect, url_for
import time
import RPi.GPIO as GPIO

app = Flask(__name__)

left_door = 24
right_door = 25

def open_door(door):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(door, GPIO.OUT, initial = GPIO.LOW)

    GPIO.output(door, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(door, GPIO.LOW)

    GPIO.cleanup()
    
@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/opener")
def opener():
    
    if "LEFT" in request.args.values():
        open_door(left_door)
        print "opening left door"
    elif "RIGHT" in request.args.values():
        open_door(right_door)
        print "opening right door"
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=80, debug = True)

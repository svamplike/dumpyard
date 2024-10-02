from flask import Flask, send_file

app = Flask(__name__)

# Route to simulate ESP32 image capture
@app.route('/capture')
def capture_image():
    # Serve a static image (you can use any image from your local directory)
    return send_file('sun_640.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    # Run the Flask server (use 0.0.0.0 to make it accessible on your local network)
    app.run(host='0.0.0.0', port=5000)

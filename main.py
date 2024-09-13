import os
import random
from flask import Flask, render_template
from PIL import Image
import argparse

app = Flask(__name__)


# Global variables for controlling the slideshow behavior
toggle_duration = 1  # Default duration for each image
shuffle_images = True  # Whether to shuffle the images

def get_images(directory):
    # Get all image files from the directory
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif')
    images = [os.path.join(directory, f) for f in os.listdir(directory) if f.lower().endswith(supported_formats)]
    return images

@app.route('/')
def index():
    # Get the images from the "static" folder (you can change this to any directory)
    image_directory = 'static/images/Pictures'  # Make sure this folder exists in your Flask app
    images = get_images(image_directory)
    
    # Shuffle images if enabled
    if shuffle_images:
        random.shuffle(images)
    
    return render_template('index.html', images=images, duration=toggle_duration)

if __name__ == '__main__':

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run the Flask app.')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the Flask app on')
    args = parser.parse_args()

    # Run the app on the specified port
    app.run(host='0.0.0.0', port=args.port, debug=True)


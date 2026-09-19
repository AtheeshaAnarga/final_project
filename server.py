"""
A Flask server for deploying the Emotion Detection application.
This server provides a web interface to analyze text for emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """
    Route to the /emotionDetector endpoint.
    Takes text input from the user, processes it using the emotion_detector,
    and returns a formatted string with the emotion scores and dominant emotion.
    Returns an error message if the input is blank or invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """
    Initiates the rendering of the main application page over the Flask channel.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
# import modules and detector file
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Run Flask
app = Flask('EmotionDetector')

# Set the route
@app.route('/emotionDetector')
# Defining detector function
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Run retrieved text to app
    result = emotion_detector(text_to_analyze)
    #Handling error
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    else:
        # Format response
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return response_text

# Render HTML page
@app.route('/')
# Define render function
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

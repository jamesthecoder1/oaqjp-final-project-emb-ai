'''Importing from created package and additional modules'''
# import modules and detector file
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Run Flask
app = Flask('EmotionDetector')

@app.route('/emotionDetector')
def sent_detector():
    """Define detector function"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    #Handling error
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

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

@app.route('/')
def render_index_page():
    ''' Render HTML file'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

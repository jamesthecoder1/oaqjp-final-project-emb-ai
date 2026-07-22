# Importing needed modules
from flask import Flask
import requests
import json

# Run Flask
app = Flask("EmotionDetector")

# Set route
@app.route('/emotion_detection')
# Define emotion detector function
def emotion_detector(text_to_analyze):
    # Set url, headers, and input
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Set how responses are received
    response = requests.post(url, json=myobj, headers=headers)
    # Convert response to JSON
    formatted_response = json.loads(response.text)
    
    # Extract emotions and score from response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Get scores from emotions listed
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Get dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Retrieve data from formatted response
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    # Return result
    return result
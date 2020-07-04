
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

nltk.download('stopwords')

set(stopwords.words('english'))
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    stop_words = stopwords.words('english')
    test_data = request.form['test_data'].lower()

    processed_data = ' '.join([word for word in test_data.split() if word not in stop_words])

    sia = SentimentIntensityAnalyzer()
    dd = sia.polarity_scores(text=processed_data)
    compound = round((1 + dd['compound'])/2, 2)

    return render_template('form.html', final=compound, test_data=test_data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)

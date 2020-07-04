# Stock-Sentiment-Analysis using News Headlines
A flask based implementation for stock sentiment analysis.
Uses randomforest with count vectorizer to get the sentiment.
Results are given below.
## Data
[Dataset](https://www.kaggle.com/aaron7sun/stocknews)
Consists of 3 columns 
  > Date,
  > Label,
  > Headline.
Further analysis can be found in StockSentimentAnalysis.ipynb

## Result

| Classifier                         | Accuracy Avg(Precision)  |
|------------------------------------|--------------------------|
| Random Forest with countVectorizer |       86.0%              |
| Random Forest with TfidfVentorizer |       83.8%              |
| Naive Bayes MultinomialNB          |       85.1%              |
| XGBClassifier (check *.ipynb)      |       84.9%              |
| Logistic Regression                |       85.4%              |
| LinearSVC                          |       84.3%              |
| SGDClassifier                      |       84.3%              |

### TO-DO
>1. Try out LSTM and other methods.
>2. Deploy it.


### Update
(4/07/2020)
Switched to nltk and [VADERsentiment](https://github.com/cjhutto/vaderSentiment) (Valence Aware Dictionary and sEntiment Reasoner).

Credit goes to [krishnaik06](https://github.com/krishnaik06) who's livestream got me to do this. You can his work [here](https://github.com/krishnaik06/Stock-Sentiment-Analysis)

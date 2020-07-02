import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def runPrediction(test_data):
    df=pd.read_csv('Data.csv', encoding = "ISO-8859-1")

    # Removing punctuations
    data = df.iloc[:,2:27]
    data.replace("[^a-zA-Z]"," ",regex=True, inplace=True)
    # Renaming column names for ease of access
    list1= [i for i in range(25)]
    new_Index=[str(i) for i in list1]
    data.columns= new_Index
    # Convertng headlines to lower case
    for index in new_Index:
        data[index] = data[index].str.lower()
    ' '.join(str(x) for x in data.iloc[1,0:25])

    headlines = []
    for row in range(0,len(data.index)):
        headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))

    tfidfvector=TfidfVectorizer(ngram_range=(2,2))
    traindataset=tfidfvector.fit_transform(headlines)
    

    logReg = LogisticRegression(random_state=0)
    logReg.fit(traindataset,df['Label'])
    test_transform= []

    test_transform.append(' '.join(test_data))
    
    test_dataset = tfidfvector.transform(test_transform)
    
    prediction = logReg.predict(test_dataset)
    if prediction == 0:
        return 'Positive '
    else:
        return 'Negative '
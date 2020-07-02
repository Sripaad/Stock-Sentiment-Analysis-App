from flask import Flask, request, render_template
import mainFile

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    
    text1 = request.form['text1'].lower()
    compound = mainFile.runPrediction(text1)
    return render_template('form.html', final=compound, text1=text1)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5002, threaded=True)

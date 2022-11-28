from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from PIL import Image

app = Flask(__name__)

def predict(values, dic):
    if len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')

@app.route("/test" , methods=['GET', 'POST'])
def test():
    return render_template('test.html')


@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = "Please enter valid Data"
        return render_template("home.html", message = message)

    return render_template('predict.html', pred = pred)

if __name__ == '__main__':
	app.run(debug = True)
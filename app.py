import sys
from flask  import   Flask , render_template, request
from insurance.logger import logging
import sys
import numpy as np
import jsonify
import pickle
import requests
from insurance.exception import InsurancePredictor

app = Flask(__name__)

model = pickle.load(open('insurance_predict_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def hello():
    try:
        raise Exception("Testing")
    except Exception as e:
        insurance = InsurancePredictor(e,sys)
        logging.info(insurance.error_message)
        logging.info("Log test")
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['a'])
        sex = request.form['sex']
        bmi = float(request.form['c'])
        child = int(request.form['d'])
        smoker = request.form['smoker']

        region = request.form['region']
        prediction = model.predict([[age , sex, bmi, child, smoker, region]])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="Your predicted premium is : {}".format(output))
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
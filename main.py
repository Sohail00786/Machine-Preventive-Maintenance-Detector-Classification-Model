import pandas as pd
import pickle
from flask import Flask, render_template, request
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
data = pd.read_csv("clean_data.csv")
pipe = pickle.load(open("XgboostModel.pkl","rb"))


@app.route('/')
def index():
    type = sorted(data['Type'].unique())
    return render_template('index.html', type = type)


@app.route('/predict', methods=["POST"])
def predict():
    a = request.form.get("Type")
    b = request.form.get("Air temperature [K]")
    c = request.form.get("Process temperature [K]")
    d = request.form.get("Rotational speed [rpm]")
    e = request.form.get("Torque [Nm]")
    f = request.form.get("Tool wear [min]")
    
    
    
    print(a,b,c,d,e)
    encoder = LabelEncoder()
    input = pd.DataFrame([[a,b,c,d,e,f]], columns = ["Type","Air temperature [K]", "Process temperature [K]","Rotational speed [rpm]","Torque [Nm]","Tool wear [min]"])
    input["Type"] = encoder.fit_transform(input["Type"])
    prediction = pipe.predict(input)[0]
    if prediction == 0:
        return "Heat Dissipation Failure"
    elif prediction == 1:
        return "No Failure"
    elif prediction == 2:
        return "Overstrain Failure"
    elif prediction == 3:
        return "Power Failure"
    elif prediction == 4:
        return "Random Failures"
    elif prediction == 5:
        return "Tool Wear Failure"
    return str(prediction)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
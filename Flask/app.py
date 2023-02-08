from flask import Flask, render_template, request # Flask is a application
# used to run/serve our application
# request is used to access the file which is uploaded by the user in out application
# render_template is used for rendering the html pages
import pickle # pickle is used for serializing and de-serializing Python object structures

model = pickle.load(open(r'C:/Users/tsjis/Downloads/Telegram Desktop/devi/devi/Flask/CCPP.pkl','rb'))

app=Flask(__name__)

@app.route('/') # rendering the html template
def home():
    return render_template('index.html')
@app.route('/predict') # rendering the html template
def index():
    return render_template("index.html")

@app.route('/data_predict', methods=['POST']) # route for our prediction 
def predict():
    AT = request.form['AT'] # requesting for age data
    AP = request.form['AP'] # requesting for gender data
    V = request.form['V'] # requesting for Total_Bilirubin data 
    RH = request.form['RH'] # requesting for Direct_Bilirubin data
    # coverting data into float format
    data = [[float(AT), float(AP), float(V), float(RH)]]
    # Loading model which we saved
    model = pickle.load(open('C:/Users/tsjis/Downloads/Telegram Desktop/devi/devi/Flask/CCPP.pkl', 'rb'))
    prediction= model.predict(data)[0]
    return render_template('index.html', prediction_text = 'Prediction of electric output is {}'.format(prediction))

if __name__=='__main__':
    app.run()

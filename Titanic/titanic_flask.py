from flask import Flask
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bem-vindo ao sistema de previsão de sobrevivência no Titanic"

## sex, age, social_class

@app.route("/titanic/predict/<sex>/<age>/<social_class>/")
def predict(sex, age, social_class):

    sex = float(sex)
    age = float(age)
    social_class = float(social_class)


    ## carregando o modelo
    filename = 'titanic.plk'
    clf_loaded = pickle.load(open(filename, 'rb'))
    classe = clf_loaded.predict([[sex, age, social_class]])

    return classe[0]

app.run(port=5000, host="0.0.0.0")






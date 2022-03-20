from cmath import exp
from  flask import Flask,render_template,request
import joblib

app = Flask(__name__)

# code -> business logic

@app.route('/')
def base():
    return render_template('prediction.html')  #render_template will implicitly add templates/ with page

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/cart')
def cart():
    return render_template('info.html')

@app.route('/contact')
def contact():
    return 'Welcome to Contact Page'

@app.route('/details',methods=['post'])
def predict():
    exp = request.form.get('experience')
    phone = request.form.get('phone')
    email = request.form.get('email')

    print(exp)
    print(phone)
    print(email)

    return "Got the values"

@app.route('/diabetic' , methods=['post'])
def diabeticPredict():
    
    model = joblib.load('diabetic_pred.pkl')
    print('reached here')

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mas')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    data = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if data[0] == 0:
        output = 'person is not diabetic'
    else:
        output ='person is diabetic'

    return render_template('output.html', data = output)

if __name__ == "main":
    app.run(debug=True)
     # debug=True makes not
#doing Ctrl+C again and again after doing change. It means file is opened in developer mode
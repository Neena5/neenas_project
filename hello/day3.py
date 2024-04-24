from flask import *
app=Flask(__name__)
app.secret_key="aa"


@app.route('/gtstud',methods=['GET'])
def mygetmthd():
    name=request.args.get('fn')
    email=request.args.get('em')
    phone=request.args.get('ph')
    print(name,email,phone)
    return 'success'


@app.route('/ptstud',methods=['POST'])
def mypostmthd():
    name=request.form['fn']
    email=request.form['em']
    phone=request.form['ph']
    print(name,email,phone)
    return 'success POST method'



@app.route('/both',methods=['POST','GET'])
def getdata():
    if request.method=='POST':
        data=request.form
        return data
    else:
        return render_template('d3.html')
    
@app.route('/sc')
def set_cook():
    res=make_response("<h1> cookie set</h1>")
    res.set_cookie('f','Anthara')
    return res


@app.route('/gec')
def get_cook():
    name=request.cookies.get('f')
    return name



@app.route('/ss')
def set_sess():
    res=make_response('session set')
    session['phone']="45678"
    return res

@app.route('/gs')
def get_sess():
    if "phone" in session:
        return session['phone']



if __name__=="__main__":
    app.run(debug=True)
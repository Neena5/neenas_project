from flask import Flask


app=Flask(__name__)

@app.route('/')
def hai():
    return "<h1>hai</h1>"

@app.route('/hello')
def hello():
    return "<h1> hello </h1>"

@app.route('/hello/<name>')
def hello1(name):
    return "<h1>hai"+name+"</h1>"


@app.route('/hello/<int:name>')
def hello2(name):
    return "num---%d"%name


def welcome():
    return '<h1>welcome</h1>'

app.add_url_rule("/w","welcome",welcome)

if __name__=="__main__":
    app.run(debug=True)
from flask import *

app=Flask(__name__)

@app.route('/adm')
def admin():
    return 'welcome admin'


@app.route('/tech')
def teacher():
    return 'welcome Teacher'

@app.route('/stu')
def student():
    return 'welcome student'

@app.route('/user/<uname>')
def user(uname):
    if uname=="admin":
        return redirect(url_for('admin'))
    elif uname=="stu":
        return redirect(url_for('teacher'))
    elif uname=="tech":
        return redirect(url_for('student'))
    else:
        return 'invalid user'

@app.route('/pag/<job>')
def mypage(job):
    name=input('enter your name:')
    return render_template('d1.html',uname=name,j=job)


@app.route('/tab/<int:n>')
def table(n):
    return render_template('d2.html', num=n)


if __name__=="__main__":
    app.run(debug=True)
from flask import *
app=Flask(__name__)
app.secret_key="aa"




@app.route('/gets',methods=['POST','GET'])
def getdata():
    if request.method=='POST':
        email=request.form['em']
        password=request.form['pw']
        if password=='admin':
            session['em']=email
            return render_template('welcome.html',em=email)
        else:
            return 'error'

    else:
        return render_template('hw.html')



@app.route('/pro')
def profile():
    if 'em' in session:
        return render_template('h.html',emi=session['em'])
    else:
        return ("<script>window.alert('login again!!!');window.location.href='/gets'</script>")
        
    

@app.route('/out')
def out():
    # session.clear()
    if 'em' in session:
        del session['em']
    return redirect(url_for('getdata'))
    


























if __name__=="__main__":
    app.run(debug=True)
from flask import *
import sqlite3
app=Flask(__name__)



@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        n=request.form['na']
        e=request.form['em']
        p=request.form['num']
        with sqlite3.connect('stud.db') as con:
            cur=con.cursor()
            cur.execute("""
                            insert into student(name,email,phone) values(?,?,?)""",(n,e,p))
            con.commit()

        return 'success'
    else:
        return render_template('stud_reg.html')



@app.route('/view')
def studview():
    con=sqlite3.connect('stud.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    return render_template('stud_view.html',data=rows)

@app.route('/dl/<int:id>')
def studdel(id):
    print(id)
    with sqlite3.connect('stud.db') as con:
            cur=con.cursor()
            cur.execute("delete from student where id=?",(id,))
            con.commit()

    return ("<script>window.alert('deleted');window.location.href='/view'</script>")
    


@app.route('/edit/<int:id>',methods=['GET','POST'])
def studedit(id):
    con=sqlite3.connect('stud.db')
    cur=con.cursor()
    if request.method=='GET':
        cur.execute("select * from student where id=?",(id,))
        recs=cur.fetchone()
        con.close()
        if recs:
            return render_template ('stud_edit.html',recs=recs)
        else:
            return 'error'
        
    elif request.method=="POST":
        n=request.form['na']
        e=request.form['em']
        p=request.form['num']
        cur.execute("update student set name=? email=?, phone=? where id=? ",(id,n,e,p))
        con.commit()
        con.close()
        return "success"


    

     









if __name__=="__main__":
    app.run(debug=True)
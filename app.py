from flask import Flask,render_template,request
import mysql.connector


db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="employee"
)

app=Flask(__name__)


#Route for Home
@app.route('/')
def Home():
    return render_template('login.html')


#Route for Login dummy
@app.route('/dummy')
def Dummy():
    return render_template('login.html')


#Route for Login 
@app.route('/login',methods=['POST'])
def login():
    id=int(request.form['id'])
    password=request.form['password'] 
    cursor=db.cursor()
    cursor.execute('select * from emp_details where id=%s',(id,))
    d1=cursor.fetchone()
    cursor.close()
    if d1:
        return render_template('dashboard.html')
    else:
        return render_template('error.html')
 

#Route for Register dummy
@app.route('/dummyr')
def Dummyr():
    return render_template('register.html')   

 
#Route for Register
@app.route('/register',methods=['POST'])
def Register():
    id=int(request.form['id'])
    name=request.form['name']
    phone=request.form['number']
    city=request.form['city']
    password=request.form['password']
    confirm=request.form['confirm']
    cursor=db.cursor()
    cursor.execute('insert into emp_details(id,name,phone,city,password,confirm) values(%s,%s,%s,%s,%s,%s)',(id,name,phone,city,password,confirm))
    db.commit()
    cursor.close()
    return render_template('login.html')


#Route for Add dummy
@app.route('/dummya')
def Dummya():
    return render_template('add.html')


#Route for Add Employee
@app.route('/add',methods=['POST'])
def Add():
    id=int(request.form['id'])
    name=request.form['name']
    phone=request.form['number']
    city=request.form['city']
    cursor=db.cursor()
    cursor.execute('select * from emp_details where id=%s',(id,))
    data=cursor.fetchone()
    if data :
        return render_template('duplicate.html')
    else:
        cursor.execute('insert into emp_details(id,name,phone,city) values(%s,%s,%s,%s)',(id,name,phone,city))
        db.commit()
        cursor.close()    
        return render_template('success_add.html')
    
    
#Route for Update dummy
@app.route('/dummyb')
def Dummyb():
    return render_template('update.html')  
 

#Route for Update Employee
@app.route('/update',methods=['POST']) 
def Update():
    id=int(request.form['id'])
    cursor=db.cursor()
    cursor.execute('select * from emp_details where id=%s',(id,))
    data=cursor.fetchone()
    if data :
        return render_template('change.html')
    else:
        return render_template('error.html')
    
  
#Route for Change Details
@app.route('/change',methods=['POST'])
def Change():
    id=int(request.form['id'])
    name=request.form['name']
    phone=request.form['number']
    city=request.form['city']
    cursor=db.cursor()
    cursor.execute('update emp_details set name=%s,phone=%s,city=%s where id=%s',(name,phone,city,id))
    db.commit()
    cursor.close()    
    return render_template('success_update.html')


#Route for Delete dummy
@app.route('/dummyc')
def Dummyc():
    return render_template('delete.html')
    
 
#Route for Delete Employee
@app.route('/delete',methods=['POST'])
def Delete():
    id=int(request.form['id'])
    cursor=db.cursor()
    cursor.execute('delete from emp_details where id=%s',(id,))
    db.commit()
    cursor.close()
    return render_template('success_delete.html')


#Route for View dummy
@app.route('/dummyd')
def Dummyd():
    return render_template('view.html')


#Route for View Employee
@app.route('/view')
def View():
    return render_template('view.html')


#Route for View One Employee
@app.route('/viewone',methods=['POST'])
def Viewone():
    id=int(request.form['id'])
    cursor=db.cursor()
    cursor.execute('select id,name,phone,city from emp_details where id=%s',(id,))
    data = cursor.fetchall()
    if data :
        return render_template('viewone.html',details=data)
    else:
        return render_template('error.html')


#Route for View All Employee
@app.route('/viewall')
def Viewall():
    cursor=db.cursor()
    cursor.execute('select id,name,phone,city from emp_details ')
    data=cursor.fetchall()
    return render_template('viewone.html',details=data)
       
        
#Route for Forgot Password 
@app.route('/forgot')
def Forgot():
    return render_template('forgot.html')


#Route for ID Check
@app.route('/check',methods=['POST'])
def Check():
    id=int(request.form['id'])
    cursor=db.cursor()
    cursor.execute('select * from emp_details where id=%s',(id,))
    data=cursor.fetchone()
    cursor.close()
    if data:
        return render_template('cred.html')
    else:
        return render_template('error.html')
    

#Route for Update Password
@app.route('/password',methods=['POST'])
def Password():
    id=int(request.form['id'])
    password=request.form['password']
    confirm=request.form['confirm']  
    cursor=db.cursor()
    cursor.execute('update emp_details set password=%s,confirm=%s where id=%s',(password,confirm,id))
    db.commit()
    cursor.close()
    return render_template('success_update.html')
       
       
#Route for Dashboard       
@app.route('/dashboard')
def Dashboard():
    return render_template('dashboard.html')
    
    
    
if __name__=="__main__":
    app.run(debug=True)
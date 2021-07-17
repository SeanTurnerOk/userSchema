from flask import Flask, render_template, redirect, session, request
from users import User
app=Flask(__name__)

@app.route('/')
def mainFunc():
    users=User.get_all()
    print(users)
    return render_template('readAll.html', allUsers=users)
@app.route('/create')
def createUser():
    return render_template('create.html')
@app.route('/creater', methods=['POST'])
def creater():
    data={
        'id':request.form['id'],
        'first_name': request.form['firstName'],
        'last_name':request.form['lastName'],
        'email':request.form['email'],
    }
    User.save(data)
    return redirect('/')
@app.route('/showOne/<x>')
def showOne(x):
    user=User.getById(x)
    return render_template('showOne.html', user=user)
@app.route('/editUser/<x>')
def editUser(x):
    user=User.getById(x)
    return render_template('editUser.html', user=user)
@app.route('/editingUser/<x>', methods=['POST'])
def editingUser(x):
    User.editById(x,request.form)
    return redirect('/')

@app.route('/deleteUser/<x>')
def delUser(x):
    User.deleteById(x)
    return redirect('/')
if __name__=='__main__':
    app.run(debug=True)
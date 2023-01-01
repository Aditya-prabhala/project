from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)

# --------------------------------indexpage---------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --------------------------------registerpage---------------------------
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()

#Html form
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        username=request.form['username']
        password=request.form['password']
        password2=request.form['password2']
        data=[name,email,phone,username,password,password2]
        #print(name,email,email,password,confirmpassword)
        query="INSERT INTO aditya(name,email,phone,username,password,password2) VALUES (?,?,?,?,?,?)"
        cursor.execute(query,data)
        connection.commit()
        return redirect('/login')
    return render_template('register.html')

# --------------------------------loginpage---------------------------
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()

#Html form
        email=request.form['namelogin']
        password=request.form['passwordlogin']

       # print(email,password)
#query
        query = "SELECT email,password FROM aditya where email='"+email+"' and password='"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

#validation
        if len(results) == 0:
            return "userid and password is incorrect"
        else:
            return redirect("/home")
    return render_template('login.html')

# --------------------------------homepage---------------------------
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask ,render_template,request,redirect,jsonify
from pymongo import MongoClient

app = Flask(__name__)

user = {}
user['username'] = 'rekai'

#session.get('key',預設值)
#session['key']

#session['key']=值

#session.clear()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def index1():
    return render_template('index.html')

@app.route('/login',methods = ["POST","GET"])
def result():
    if request.method == 'POST':
        result = request.form
        return redirect('/')
    
@app.route('/signup')
def index2():
    return render_template('signup.html')

    
@app.route('/signup',methods = ["POST","GET"])
def signup():
    if request.method == 'POST':
        result = request.form
        return redirect('/')

@app.route('/login',methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    if username in user:
            # 檢查密碼是否正確
            if user[username] == password:
                # 登入成功，導向成功頁面
                return redirect('/success')
            else:
                # 密碼錯誤，重新輸入
                return redirect("/login", message="密碼錯誤，請重新輸入")
    else:
            # 帳號不存在，導向註冊頁面
            return redirect("/signup", message="帳號不存在，請先註冊")


@app.route('/success')
def success():
    return render_template('success.html')

    
if __name__ == '__main__':
    app.run(debug=True)
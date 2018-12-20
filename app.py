#flask run --host=$ip --port=$port
#flask run --host=0.0.0.0 --port=8080
import random


from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# variable routing
@app.route("/greeting/<string:name>")
def greeting(name) :
    return f"{name}이 들어왔니?"
    
@app.route("/google")
def google() :
    return render_template("google.html")
# 사용자에게 정보 받기
# 1. 입력창을 보여준다.

@app.route("/lunch")
def lunch() :
    return render_template("lunch.html")

# 2. 값을 받아서 처리한다.
@app.route("/menupick")
def menupick() :
    name = request.args.get("person")
    if name == "히히" :
        return f"{name}야, 초밥먹엉"
    return f"{name}야, 고기먹엉"


# 메뉴 등록할 수 있는 입력창 보여주는 페이지
@app.route("/menu/add")
def menu_add() :
    return render_template("menu_add.html")

# 메뉴 등록 작업

@app.route("/menu/create")
def menu_create() :
    menu = request.args.get("menu")
    with open("menu.txt", "a") as file :
        file.write(menu+"\n")
    
    return redirect("/menu")

# 메뉴 추천 페이지

@app.route("/menu")
def menu() :
    # 1. 파일을 불러와서 리스트에 담는다.
    with open("menu.txt", "r") as file :
        menus = file.readlines()
    
    
    # 2. 리스트에서 하나를 뽑아서 변수에 저장한다.
    recommend = random.choice(menus)
    
    
    # 3. html에 추천된 것을 보여준다.
    return render_template("menu.html", recommend=recommend)
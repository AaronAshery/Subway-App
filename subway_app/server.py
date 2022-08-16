import random
from flask import (Flask, render_template, redirect, request, make_response)
import json
from jinja2 import Environment, FileSystemLoader
from flask import Response, request, jsonify
app = Flask(__name__)
app.config['SECRET_KEY'] = "Alio"

lessons = {
    "1":{
        "lesson_id": "1",
        "title": "Five boroughs",
        "img": "map2.png",
        "text": "New York is divided into five boroughs with Manhattan being the central area where the majority of tourist attractions reside: Manhattan Queens Bronx Staten Island Brooklyn ",
        "next": "2"
    },
    "2":{
        "lesson_id": "2",
        "title": "Street system in Manhattan",
        "img": "learn2.png",
        "text": "The street system in Manhattan is composed of a rectangular street grid Streets travel east and west Avenues travel north and south Since the grid is made up of rectangle a block can be short or long Walking north/south along and avenue makes for a short bloc Walking east/west along a street makes for a long block",
        "next": "3"
    },
    "3":{
        "lesson_id": "3",
        "title": "Lines",
        "img": "learn3.png",
        "text": "Take note of the different column entries: Train Services, Line Names, Express trains, and Local trains. Each line has a name and a specific color. Example: The Broadway-7th Ave line is red. More important than the name of the line is the color of the line.  ",
        "next": "4"
    },
    "4":{
        "lesson_id": "4",
        "title": "Understanding symbols",
        "img1": "express2.png",
        "img2": "local.png",
        "text2": "Local trains stop at every station. When reading the subway map, some stations are indicated as white dots and others as black dots. A station with a black dot means that only local trains stop here; express trains skip this station.",
        "text1": "Unlike local trains, express trains skips certain stations for faster service. Most common configuration of the NYC subway platform is that express trains usually run on tracks in the middle. ",
        "next": "5"
    },
    "5":{
        "lesson_id": "5",
        "title": "Up/Mid/Downtown",
        "img1": "uptown2.png",
        "img2": "middowntown.png", 
        "text1": "Though neighborhood names and boundaries are not officially defined Manhattan is generally divided into three parts: uptown, midtown, and downtown. Upper Manhattan is the area above 96th street.",
        "text2": "Midtown Manhattan is the area between 14th street and 59th street. Lower Manhattan is the area below 14th street. Additionally, west side is the area west of Fifth Avenue and east side is the area east of Fifth Avenue.",
        "next": "end"
    }
}


quiz_questions = {"1": {
    "quiz_id":"1",
    "question":"Drag each label to the correct place on the map:",
    "choices":["Manhattan", "Brooklyn", "Staten Island", "Bronx", "Queens"],
    "img": "map2.png",
    "answer": {},
    "next":"2"
    },
    "2": {"quiz_id":"2",
    "question": ["What is the blue line?", "What is the yellow line?"],
    "choices":["street", "avenue", "road"],
    "img": "street_avenue_simple.png",
    "answer" : {"1" : "street", "2": "avenue"},
    "next":"3"
    },
    "3" : {"quiz_id":"3",
    "question":"Joey is walking down a street what direction is he traveling in?",
    "choices": ["North/South", "East/West"],
    "img": "street.gif",
    "answer": {"1": "East/West"},
    "next":"4"
    },
     "4": {"quiz_id":"4",
    "question":"in progress",
    "choices":"in progress",
    "img": "Street_ave-1.jpg",
    "answer": {},
    "next":"5"
    },
     "5": {"quiz_id":"5",
    "question":["Joey lives on 72nd street. Every day Joey gets on the subway and commutes to work. His office is located on 116th street.", "What area does Joey live in?", "What direction does he travel to get to work?"],
    "choices":["Uptown", "Midtown", "Downtown"],
    "img": "home_uptown.png",
    "answer": {"1": "Uptown", "2":"Uptown"},
    "next":"6"
    },
    "6": {"quiz_id":"6",
    "question":"Using your knowledge of the New York subway system select the statements that are true",
    "choices": ["New York has 4 boroughs", "42nd and 14th street contain transfer stations for multiple lines", "Express trains skip stations for faster service", "The 7 and L train travel east to west",  "A black dot on a subway map indicates only express trains stop"],
    "img": "",
    "answer": {"1": "42nd and 14th street contain transfer stations for multiple lines", "2": "Express trains skip stations for faster service", "3": "The 7 and L train travel east to west" },
    "next":"7"
    },
}

score = 7

user = {
    "test_started": "true",
    "last_visited_learning": "1",
    "last_visited_quiz" : "1"
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/learn',methods=['GET'])
def learn():
    return render_template('learn.html')

@app.route('/bouroughs',methods=['GET'])
def bouroughs():
    return render_template('bouroughs.html')

@app.route('/street',methods=['GET'])
def street():
    return render_template('street.html')

@app.route('/quiz_home',methods=['GET'])
def quiz_home():
    return render_template('quiz_home.html', user=user)

@app.route('/downtown',methods=['GET'])
def downtown():
    return render_template('downtown.html')

@app.route('/express',methods=['GET'])
def express():
    return render_template('express.html')

@app.route('/circle',methods=['GET'])
def circle():
    return render_template('circle.html')

@app.route('/line',methods=['GET'])
def line():
    return render_template('line.html')

@app.route('/redLine',methods=['GET'])
def redLine():
    return render_template('redLine.html')

@app.route('/orangeLine',methods=['GET'])
def orangeLine():
    return render_template('orangeLine.html')

@app.route('/blueLine',methods=['GET'])
def blueLine():
    return render_template('blueLine.html')

@app.route('/L7',methods=['GET'])
def L7():
    return render_template('L7.html')

@app.route('/quiz/<quiz_id>',methods=['GET'])
def quiz(quiz_id):
    global score
    if int(quiz_id) > len(quiz_questions):
        return render_template('results.html', score = score)
    else:
        question = quiz_questions[quiz_id]
        # different template 
        if int(quiz_id) == 1:
            return render_template('q_draggable.html', score=score)

        if int(quiz_id) == 2:
            print("return new template")
            return render_template('q_dropdown.html', question = question, score=score)
        elif int(quiz_id) == 3:
            return render_template ('q_fillin.html', question = question, score=score)
        elif int(quiz_id) == 4:
            return render_template ('q_fillin_variation.html', question = question, score=score)
        elif int(quiz_id) == 5:
            return render_template('q_dropdown_variation.html', question = question, score=score)
        elif int(quiz_id) == 6:
            return render_template('q_checkbox.html', question = question, score=score)
        else:
            return render_template('quiz.html', question = question )
    


@app.route('/update_score', methods=['GET', 'POST'])
def update_score():  
    global score 
    json_data = request.get_json()
    score += int(json_data)
    print("the current score is: ", score)
    return jsonify(score = score)

@app.route('/user_info', methods=['GET', 'POST'])
def update_user_info():
    global score
    json_data = request.get_json()
    update = json_data['test_started']
    user['test_started'] = update 
    # user just began the quiz so the score should be reset 
    score = 6
    print(json_data)
    return jsonify(user = user)

if __name__ == '__main__':
   app.run(debug = True)
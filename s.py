from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

sneakers = [
    {
        "id": 1,
        "brand": "Nike",
        "name": "Air Jordan",
        "price": 5000,
        "color": "red",
        "group": 1,
        "size": 37,
        "groupSize": 1,
        "count": 50,
        "description": "Материал: Верх - текстиль, резина; Подкладка - текстиль; Низ - резина",
        "sex": 0
    },
    {
        "id": 2,
        "brand": "Nike",
        "name": "Air Jordan",
        "price": 5000,
        "color": "blue",
        "group": 1,
        "size": 38,
        "groupSize": 1,
        "count": 10,
        "description": "Материал: Верх - текстиль, резина; Подкладка - текстиль; Низ - резина",
        "sex": 0
    }
]

users = [
    {
        "login": "gfg",
        "password": "qwerty",
        "id": 1,
        "name": "Рома",
        "phone": "88005553535",
        "email": "example@mail.ru",
        "adress": "Пирогова 5/1",
        "money": 6000,
        "sex": 0,
        "image": "https://telegrator.ru/wp-content/uploads/2021/05/chat_avatar-136.jpg"
    }
]

cart = [
    {
        "id": 1,
        "ownerId":1,
        "items": [{
            "sneakersId": 1
        }

        ],

    }
]

who = [
    {
        "name": "Рома",
        "phone": "88005553535",
        "question": "Забыл пароль от аккаунта. ПАМАГИТИ!!!"
    }


]

messages = [
    # {
    #     "text": "Привет",
    #     "date": "12/14/2022",
    #     "sender": {
    #         "name": "Рома",
    #         "id": 1,
    #         "image": "",
    #     },
    #     "room": 1

    # },
    # {
    #     "text": "Привет",
    #     "date": "12/14/2022",
    #     "sender": {
    #         "name": "Рома",
    #         "id": 1,
    #         "image": "",
    #     },
    #     "room": 2

    # },
    # {
    #     "text": "Здарова, Артурка!",
    #     "date": "12/14/2022",
    #     "sender": {
    #         "name": "Рома",
    #         "id": 1,
    #         "image": "",
    #     },
    #     "room": 1

    # }



]

rooms = [
    { 
        "id": 1,
        "title": "Котики всем!!!",
        "private": 0

    },
    { 
        "id": 2,
        "title": "Собачки всем!!!(без корейцев)",
        "private": 1,
        "invited_id":[1, 2]
    }  

]

@app.post("/send_msg")
def sendMsg():
    msg_data = request.get_json()
    messages.append(msg_data)
    #return getMessagesForRoom(msg_data["room"])
    return '200'



@app.get("/allmsg")
def getAllMsg():
    return messages


@app.get("/msg_room/<room>/<user_id>")
def getMessagesForRoom(room, user_id):
    private = 0
    currentRoom = {}
    for r in rooms:
        if r["id"] == int(room):
            private = r["private"]
            currentRoom = r
    if private == 0:
        msgRoom = []
        for msg in messages:
            if msg["room"] == int(room):
                msgRoom.append(msg)
        return msgRoom
    else:
        ok = False
        for invite in currentRoom["invited_id"]:
            if invite == int(user_id):
                ok = True
        if ok:
            msgRoom = []
            for msg in messages:
                if msg["room"] == int(room):
                    msgRoom.append(msg)
            return msgRoom
        else:
            return "Доступ запрещен!!! Чат только для Артура и его коллег по рынку"
        
            
            

        





@app.post("/log")
def logIn():
    user_data = request.get_json()
    find = False
    user = False
    for i in users:
        if i["login"] == user_data["login"] and i["password"] == user_data["password"]:
            find = True
            user = i
    if find:
        return user
    else:
        return "ОШИБКA!!"

@app.post("/reg")
def registr():
    user_data = request.get_json()
    find = False
    for i in users:
        if i["login"] == user_data["login"] or i["email"] == user_data["email"]:
            find = True
    if find:
        return "Данные не уникальны!"
    else:
        users.append(user_data)
        return user_data

@app.get("/call")
def calls():
    return who



@app.get("/")
def getAlluser():
    return users


if __name__ == "__main__":
    app.run(debug=True)

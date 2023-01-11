from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

sneakers = [

]

users = [

]

cart = [

]

who = [



]

messages = [




]

rooms = [
   

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
            return "non dostup"
        
            
            

        





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
        return "err"

@app.post("/reg")
def registr():
    user_data = request.get_json()
    find = False
    for i in users:
        if i["login"] == user_data["login"] or i["email"] == user_data["email"]:
            find = True
    if find:
        return "not uniq"
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

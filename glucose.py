from flask import Flask, jsonify, request

import json

app = Flask(__name__)

glucose = [
    {
        "glucose_id": 1,
        "date" : "November 1, 2022",
        "glucose" : "75mg"
    },

    {
        "glucose_id": 2,
        "date" : "November 22, 2022",
        "glucose" : "75mg"
    }
]
@app.route('/glucose', methods=['POST'])
def addGlucose():
    reqGlu = request.get_json()
    glucose.append(reqGlu)
    return {'id':len(glucose)}, 200

@app.route('/glucose', methods=['GET'])
def displayGlucose():
    return jsonify(glucose)

@app.route('/glucose/<int:index>', methods=['GET'])
def getGlucose(index):
    if index < len(glucose):
        return jsonify(glucose[index]), 200
    else:
        return "Glucose ID Not Found", 404

@app.route('/glucose/<int:index>', methods=['POST'])
def updateGlucose(index):
    reqGlu = request.get_json()
    glucose.pop(index)
    glucose.append(reqGlu)
    return f"Successfully Updated glucose_id {index}", 200

@app.route('/glucose/<int:index>', methods=['DELETE'])
def deleteGlucose(index):
    glucose.pop(index)
    return "Glucose Successfully Deleted", 200

if __name__== '__main__':
    app.run()

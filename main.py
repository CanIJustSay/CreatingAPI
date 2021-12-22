from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        "name": 'Wyatt',
        'number': '6026169716'
    }
]

@app.route("/show")
def showCon():
    return jsonify({
        "data":contacts
    })

@app.route('/add', methods=['POST'])
def addCon():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'No data entered'
        })
    c = {
        'id': contacts[-1]["id"] + 1,
        'number': request.json['number'],
        'name': request.json['name']
    }
    contacts.append(c)
    return jsonify({
        'status': 'success',
        'message': 'Task created'
    })

if (__name__ == '__main__'):
    app.run(debug=True)
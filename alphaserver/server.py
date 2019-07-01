from flask import Flask, session, request, jsonify, render_template
import os, json
app = Flask('alpa')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.before_first_request
def _declareStuff():
    if not os.path.exists(os.path.join(app.static_folder, 'data.json')):
        with open(os.path.join(app.static_folder, 'data.json'), 'w'): pass


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/retrieve", methods=['GET','POST'])
def retrieve():
    if request.method == 'POST':
        req_data = request.get_json()
        data = {}
        filename = os.path.join(app.static_folder, 'data.json')
        if os.stat(filename).st_size != 0:
            with open(filename) as blog_file:
                data = json.load(blog_file)

        if req_data['server'] in data:
            ses = data[req_data['server']]
            total = ses['total']
            if req_data['status'] == 'disconnect':
                total -= 1
            else:
                total += 1
            data[req_data['server']]['total'] = total
        else:
            data[req_data['server']] = {
                "total" : 1
            }

        with open(os.path.join(app.static_folder, 'data.json'), 'w') as fp:
            json.dump(data, fp)

        return "success"

    data = {}
    filename = os.path.join(app.static_folder, 'data.json')
    if os.stat(filename).st_size != 0:
        with open(filename) as blog_file:
            data = json.load(blog_file)

    data = {
        "data" : data
    }
    return jsonify(data)
app.run(host='0.0.0.0')

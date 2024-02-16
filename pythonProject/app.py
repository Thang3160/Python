from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pha-do')
def genealogical():
    return render_template('genealogical.html')

@app.route('/lich-su')
def hitory():
    return render_template('hitory.html')

@app.route('/su-kien')
def event():
    return render_template('event.html')

@app.route('/chi-tiet')
def event_detail():
    return render_template('event-detail.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)

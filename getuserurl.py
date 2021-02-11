from flask import *
import requests

app = Flask(__name__)


@app.route('/')
def customer():
    return render_template('geturl.html')

@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['text']
    r = requests.get(url)

    spliturl = url.split("/")
    urllength = len(spliturl)

    filename = spliturl[urllength - 1]

    print(filename)

    with open(filename, 'wb') as f:
        f.write(r.content)
    return "Successfully downloaded your file"

if __name__ == '__main__':
    app.run(port=5002,debug=True)


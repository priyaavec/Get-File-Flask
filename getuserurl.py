from flask import *
import requests

app = Flask(__name__)

#Display Home page to user to get url
@app.route('/')
def user():
    return render_template('geturl.html')

#Download user specified URL
@app.route('/', methods=['POST'])
def downloadfile():
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
    app.run(port=5003,debug=True)


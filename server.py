from flask import Flask, render_template, request
from downloader import download

app = Flask(__name__)

@app.route('/')
@app.route('/download', methods =['GET', 'POST'])
def home():
    # getting input from form
    if request.method == 'POST': 
        link = request.form.get('link')
        format = request.form.get('format')
        return render_template('download.html', info = download(link,format))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
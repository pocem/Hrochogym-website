from flask import Flask, render_template, request

app = Flask(__name__)





@app.route("/")
def home_page():
    return render_template('index.html')


@app.route("/location/<city>")
def choose_gym(city):

    return render_template('location.html', city=city)

if __name__ == '__main__':
    app.run(debug=True)
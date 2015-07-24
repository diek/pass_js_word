from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    wing_options = [
        "Uncle Lou's Sweet Spicy Love",
        "Diek's Wings of the Chicken",
        "Asian Flame Throwers",
        "Twisted BBQ",
        "Dusted and Crispy"
    ]
    if request.method == 'POST':
        wing_choice = request.form['wing-type']
        return render_template('index.html', choice=wing_choice,
                               wing_options=json.dumps(wing_options))
    return render_template('index.html', wing_options=json.dumps(wing_options))


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from scraper import get_multipliers
from predictor import calculate_prediction

app = Flask(__name__)

@app.route('/')
def home():
    multipliers = get_multipliers()
    prediction = calculate_prediction(multipliers)
    return render_template('index.html', multipliers=multipliers, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

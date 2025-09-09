from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model
model = pickle.load(open("student_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form values
        hours = int(request.form['hours'])
        prev_scores = int(request.form['prev_scores'])
        extra = request.form['extra']
        extra = 1 if extra.lower() == 'yes' else 0
        sleep = int(request.form['sleep'])
        papers = int(request.form['papers'])

        # Prepare features
        features = np.array([[hours, prev_scores, extra, sleep, papers]])
        prediction = model.predict(features)[0]
        prediction = round(prediction, 2)

        # Performance category
        if prediction < 35:
            comment = "Needs more practice, Improving with guidance."
            category = "Slow Learner"
        elif 35 <= prediction < 70:
            comment = "Shows good progress, Can achieve more with effort."
            category = "Mid Learner"
        else:
            comment = "Quick grasp of concepts, Performs excellently."
            category = "Fast Learner"

        return render_template('output.html',
                               score=prediction,
                               category=category,
                               comment=comment)

if __name__ == "__main__":
    app.run(debug=True)

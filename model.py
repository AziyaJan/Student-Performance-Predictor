import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
student_dataset = pd.read_csv('Student_Performance.csv')

# Features & Target
X = student_dataset[['Hours Studied', 'Previous Scores',
                     'Extracurricular Activities',
                     'Sleep Hours', 'Sample Question Papers Practiced']]
y = student_dataset['Performance Index']  # <-- replace with actual target column name

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model using pickle
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as student_model.pkl")

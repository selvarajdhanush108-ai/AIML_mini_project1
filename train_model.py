import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/student_data.csv")

# We do NOT use RollNo or Class for training
X = data[['Attendance', 'StudyHours', 'InternalMarks', 'Assignment', 'PreviousSem']]
y = data['FinalGrade']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/student_model.pkl")

print("Model trained and saved successfully!")
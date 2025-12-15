import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

# =========================================================
# 1️⃣ LOAD DATA
# =========================================================
data = pd.read_csv("data/students_data.csv")

X = data.drop("placed", axis=1)
y = data["placed"]

# =========================================================
# 2️⃣ TRAIN–TEST SPLIT
# =========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================================================
# 3️⃣ MODEL TRAINING
# =========================================================
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("✅ Model trained successfully")

# =========================================================
# 4️⃣ MODEL EVALUATION
# =========================================================
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("📊 Model Accuracy:", acc)

# =========================================================
# 5️⃣ USER INPUT (SIMULATION)
# =========================================================
print("\nEnter student details (0–5 scale, CGPA 0–10):")

prog = int(input("Programming: "))
dsa = int(input("DSA: "))
projects = int(input("Projects: "))
internship = int(input("Internship (0/1): "))
cgpa = float(input("CGPA: "))
communication = int(input("Communication: "))

student_input = [[prog, dsa, projects, internship, cgpa, communication]]

# =========================================================
# 6️⃣ PREDICTION
# =========================================================
prediction = model.predict(student_input)

if prediction[0] == 1:
    print("\n🎯 Result: Placement Ready ✅")
else:
    print("\n❌ Result: Not Placement Ready")

# =========================================================
# 7️⃣ EXPLAINABILITY (AI DECISION LOGIC)
# =========================================================
print("\n🧠 How the AI made this decision:")
print("""
The model evaluates the following parameters:
• Programming skills
• DSA problem-solving ability
• Project experience
• Internship exposure
• CGPA
• Communication skills

Based on patterns learned from historical student data,
the model predicts placement readiness and identifies weak areas.
""")

# =========================================================
# 8️⃣ WEAK AREAS & SUGGESTIONS
# =========================================================
weak_areas = []
suggestions = []

if prog < 3:
    weak_areas.append("Programming")
    suggestions.append("Improve programming fundamentals")

if dsa < 3:
    weak_areas.append("DSA")
    suggestions.append("Practice DSA daily")

if projects < 2:
    weak_areas.append("Projects")
    suggestions.append("Build more real-world projects")

if internship == 0:
    weak_areas.append("Internship")
    suggestions.append("Apply for internships")

if cgpa < 7:
    weak_areas.append("CGPA")
    suggestions.append("Improve academic performance")

if communication < 3:
    weak_areas.append("Communication")
    suggestions.append("Work on communication skills")

if prediction[0] == 0:
    print("\n📉 Weak Areas:")
    for w in weak_areas:
        print("-", w)

    print("\n📌 Suggestions:")
    for s in suggestions:
        print("-", s)

# =========================================================
# 9️⃣ SAVE MODEL
# =========================================================
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ Model saved as model.pkl")

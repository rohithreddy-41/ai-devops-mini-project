import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import sys

# Load past build logs
df = pd.read_csv('logs/build_logs.csv')

# Prepare data
X = df[['code_changes', 'test_passed']]
y = df['build_success']

# Train model
model = RandomForestClassifier().fit(X, y)

# Simulate current build input (example: 5 changes, tests failed)
current = [[5, 0]]
prediction = model.predict(current)
prob = model.predict_proba(current)[0][1]

# Output and exit logic
if prediction[0] == 0:
    print(f"High failure risk! Probability of success: {prob:.2f}")
    sys.exit(1)
else:
    print(f"Low risk. Proceeding... Success probability: {prob:.2f}")


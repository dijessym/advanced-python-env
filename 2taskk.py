# ===== DILYAZ STYLE =====

import json

with open("students.json", "r", encoding="utf-8") as dfile:
    dstudents = json.load(dfile)

for dstudent in dstudents:
    dgrades = dstudent["grades"]
    dstudent["average_grade"] = sum(dgrades) / len(dgrades)

with open("students_updated.json", "w", encoding="utf-8") as dout:
    json.dump(dstudents, dout, indent=4)
print("DONE")

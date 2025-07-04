from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from logic.diagnose import diagnose_condition

app = Flask(__name__)
CORS(app)

# Load questions once
with open("data/questions.json", "r") as f:
    question_flow = json.load(f)

user_sessions = {}

@app.route("/api/start", methods=["POST"])
def start_chat():
    data = request.get_json()
    pain_area = data.get("pain_area")

    if pain_area not in question_flow:
        return jsonify({"error": "Unsupported body part"}), 400

    user_sessions[data["user_id"]] = {
        "pain_area": pain_area,
        "question_index": 0,
        "answers": []
    }

    question = question_flow[pain_area][0]
    return jsonify({"question": question})

@app.route("/api/answer", methods=["POST"])
def next_question():
    data = request.get_json()
    user_id = data["user_id"]
    answer = data["answer"]

    session = user_sessions.get(user_id)
    if not session:
        return jsonify({"error": "Session not found"}), 400

    session["answers"].append(answer)
    session["question_index"] += 1

    questions = question_flow[session["pain_area"]]

    if session["question_index"] >= len(questions):
        result = diagnose_condition(session["pain_area"], session["answers"])
        del user_sessions[user_id]  # End session
        return jsonify({"diagnosis": result})

    next_q = questions[session["question_index"]]
    return jsonify({"question": next_q})
if __name__ == '__main__':
    app.run(debug=True)

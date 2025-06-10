from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__, template_folder='templates')  # Use 'templates' folder

# Your valid API key here:
genai.configure(api_key="***") 

# Use a valid model name (check with genai.list_models())
model = genai.GenerativeModel("gemini-pro")  # without "models/"

app = Flask(__name__, template_folder='template')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_response():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "Please provide a message."}), 400

    try:
        # Single-turn generation
        response = model.generate_content(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

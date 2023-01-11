import openai
from flask import Flask, render_template, request
from GPTLearn import configure, create_completion, testQuestion

app = Flask(__name__)

@app.route("/")
def index():
    name = "Luke"
    return render_template("index.html", name=name)

@app.route("/process", methods=["POST"])
def process():
    configure()
    model = "text-davinci-003"
    organization = ORGANIZATION
    user_input = request.form["user_input"]
    temperature = 0.7
    result = create_completion(model, organization, user_input, temperature)
    return result

if __name__ == "__main__":
    app.run(host="HOST", port=port_number)
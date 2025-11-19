from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/render")
def render_vuln():
    user_input = request.args.get("text", "")
    
    template = f"""
    <h2>You entered:</h2>
    <div>{user_input}</div>
    """

    return render_template_string(template)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5558)

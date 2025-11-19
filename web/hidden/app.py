from flask import Flask, request, jsonify, make_response, send_from_directory
import jwt
import datetime
import base64

app = Flask(__name__)

SECRET_KEY = "ali_slimani_lwa3r_sba3"

users = {}

FLAG = "CyberZ{h1dd3n_1n_c55}"

@app.route("/")
def index():
    return """
    <h1></h1>
    <p><a href='/register'>Register</a> | <a href='/login'>Login</a></p>
    """

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if username in users:
            return jsonify({"message": "User already exists"}), 400
        
        users[username] = {"password": password, "role": "user"}
        return jsonify({"message": "User registered successfully"})
    
    return """
    <form method='post' onsubmit='register(event)'>
      <input name='username' placeholder='Username'><br>
      <input name='password' placeholder='Password' type='password'><br>
      <button type='submit'>Register</button>
    </form>
    <script>
    async function register(e){
      e.preventDefault();
      const data = {
        username: e.target.username.value,
        password: e.target.password.value
      };
      const res = await fetch('/register', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
      alert(await res.text());
    }
    </script>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = users.get(username)
        if not user or user["password"] != password:
            return jsonify({"message": "Invalid credentials"}), 401

        token = jwt.encode({
            "username": username,
            "role": user["role"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")

        return jsonify({"token": token})
    
    return """
    <form method='post' onsubmit='login(event)'>
      <input name='username' placeholder='Username'><br>
      <input name='password' placeholder='Password' type='password'><br>
      <button type='submit'>Login</button>
    </form>
    <script>
    async function login(e){
      e.preventDefault();
      const data = {
        username: e.target.username.value,
        password: e.target.password.value
      };
      const res = await fetch('/login', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
      const out = await res.json();
      if(out.token){
        alert('Login successful! Use this JWT in Authorization header.');
        console.log('Your JWT:', out.token);
      } else {
        alert(out.message);
      }
    }
    </script>
    """

@app.route("/admin")
def admin():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"message": "Missing Authorization header"}), 401

    try:
        token = auth_header.split()[1]
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if data.get("role") != "admin":
            return jsonify({"message": "Access denied. Admins only."}), 403
    except Exception as e:
        return jsonify({"message": f"Invalid token: {e}"}), 401

    return jsonify({"flag": FLAG})

@app.route("/static/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5554)

from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)
DB = "passwords.db"

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<title>🔒 Local Password Breach Checker</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  background: radial-gradient(ellipse at top left, #23243a 0%, #181926 100%);
  font-family: 'Fira Mono', 'Consolas', 'Menlo', monospace;
  color: #e0e0e0;
  margin: 0;
  min-height: 100vh;
}
.container {
  max-width: 420px;
  margin: 70px auto;
  background: rgba(22, 23, 40, 0.97);
  border-radius: 16px;
  padding: 2.5rem 2rem 2rem 2rem;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, .25);
  border: 2px solid #2de0a7;
  position: relative;
  overflow: hidden;
}
h2 {
  color: #2de0a7;
  text-shadow: 0 0 8px #2de0a7cc;
  margin-top: 0;
  font-size: 1.6rem;
  letter-spacing: 1px;
  text-align: center;
}
form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 24px;
}
input[type=password] {
  background: #26283e;
  color: #e0e0e0;
  padding: 15px 14px;
  border: 1.5px solid #2de0a7;
  border-radius: 6px;
  font-size: 1.1rem;
  letter-spacing: 1.5px;
  transition: border .2s, background .2s;
  outline: none;
}
input[type=password]:focus {
  border: 2px solid #45ffdb;
  background: #23243a;
}
button {
  background: linear-gradient(90deg,#2de0a7,#45ffdb);
  color: #161728;
  border: none;
  border-radius: 6px;
  padding: 14px 0;
  font-weight: bold;
  font-size: 1.1rem;
  letter-spacing: 1px;
  box-shadow: 0 0 10px #2de0a7aa;
  cursor: pointer;
  margin-top: 5px;
  transition: background .18s, color .2s, box-shadow .18s;
}
button:hover {
  background: linear-gradient(90deg,#45ffdb,#2de0a7);
  color: #222;
  box-shadow: 0 0 18px #2de0a7cc;
}
.result {
  margin-top: 32px;
  padding: 19px 0 14px 0;
  border-radius: 7px;
  text-align: center;
  font-size: 1.3rem;
  font-family: inherit;
  font-weight: 500;
  letter-spacing: 1px;
  background: rgba(20,33,40,0.83);
  box-shadow: 0 0 24px 0 #45ffdb33;
  animation: resultFadeIn .85s cubic-bezier(.44,2.03,.55,.89);
}
@keyframes resultFadeIn {
  0% { opacity: 0; transform: translateY(24px) scale(.9);}
  100% { opacity: 1; transform: translateY(0) scale(1);}
}
.breach {
  border: 2px solid #fd326f;
  color: #fd326f;
  text-shadow: 0 0 6px #fd326faa;
}
.safe {
  border: 2px solid #2de0a7;
  color: #2de0a7;
  text-shadow: 0 0 7px #2de0a788;
}
::-webkit-input-placeholder { color: #8bf7e0; opacity: 1; }
::-moz-placeholder { color: #8bf7e0; opacity: 1; }
:-ms-input-placeholder { color: #8bf7e0; opacity: 1; }
::placeholder { color: #8bf7e0; opacity: 1; }

@media (max-width: 600px) {
  .container { padding: 1.2rem 0.5rem 1.5rem 0.5rem; }
  h2 { font-size: 1.1rem; }
}
.footer {
  margin-top: 38px;
  color: #54627a;
  font-size: .92rem;
  text-align: center;
  letter-spacing: .5px;
}
</style>
</head>
<body>
  <div class="container">
    <h2>🔒 Local Password<br>Breach Checker</h2>
    <form method="post" autocomplete="off">
        <input type="password" name="password" placeholder="Enter password to check..." required>
        <button type="submit">Check Password</button>
    </form>
    {% if result is not none %}
    <div class="result {{ 'breach' if result else 'safe' }}">
        {{ '⚠️ This password <b>was found</b> in a data breach.' if result else '✅ This password <b>was NOT found</b> in known breaches.' }}
    </div>
    {% endif %}
  </div>
  <div class="footer">
    <span>Runs 100% locally. Passwords are never sent anywhere.</span>
  </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        pw = request.form['password']
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT 1 FROM passwords WHERE pw=? LIMIT 1", (pw,))
        result = c.fetchone() is not None
        conn.close()
    return render_template_string(TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

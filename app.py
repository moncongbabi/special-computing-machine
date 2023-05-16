import os
from flask import Flask
from flask import render_template
import culturestreak

app = Flask(__name__)
culturestreak.processing()
@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

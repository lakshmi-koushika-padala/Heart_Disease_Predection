from flask import Flask, render_template, request
from model import predict_heart

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    result = None

    if request.method == "POST":
        values = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["thalach"])
        ]

        result = predict_heart(values)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

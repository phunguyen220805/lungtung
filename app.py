from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    male_value = request.form.get("male", "")
    female_value = request.form.get("female", "")

    if request.method == "POST":
        try:
            male = int(male_value)
            female = int(female_value)
            if male < 0 or female < 0:
                raise ValueError
        except ValueError:
            error = "Vui lòng nhập số nguyên không âm cho cả hai ô."
        else:
            total = male + female
            scale = max(male, female, 1)
            result = {
                "male": male,
                "female": female,
                "total": total,
                "male_height": max(8, round(male / scale * 100)),
                "female_height": max(8, round(female / scale * 100)),
                "male_percent": round(male / total * 100) if total else 0,
                "female_percent": round(female / total * 100) if total else 0,
            }

    return render_template(
        "index.html",
        result=result,
        error=error,
        male_value=male_value,
        female_value=female_value,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5175, debug=False)
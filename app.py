from flask import Flask, render_template, request
import csv
import matplotlib.pyplot as plt

app = Flask(__name__)

def read_csv():
    with open("data.csv", newline='') as f:
        reader = csv.DictReader(f)
        # Strip spaces from both keys and values
        return [{k.strip(): v.strip() for k, v in row.items()} for row in reader]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id_type = request.form.get("ID")
        id_value = request.form.get("id_value")

        if not id_type or not id_value:
            return render_template("error.html", message="Please select an ID type and enter a value.")

        data = read_csv()

        if id_type == "student_id":
            student_data = [row for row in data if row["Student id"] == id_value]
            if not student_data:
                return render_template("error.html", message="No student found with the given ID.")

            total_marks = sum(int(row["Marks"]) for row in student_data)
            return render_template("student_details.html", data=student_data, total=total_marks)

        elif id_type == "course_id":
            course_data = [int(row["Marks"]) for row in data if row["Course id"] == id_value]
            if not course_data:
                return render_template("error.html", message="No course found with the given ID.")

            avg_marks = round(sum(course_data) / len(course_data), 2)
            max_marks = max(course_data)

            # Generate histogram
            plt.figure()
            plt.hist(course_data, bins=10, color='skyblue', edgecolor='black')
            plt.title(f"Histogram for Course {id_value}")
            plt.xlabel("Marks")
            plt.ylabel("Frequency")
            plt.savefig("static/histogram.png")
            plt.close()

            return render_template("course_details.html", avg=avg_marks, maxm=max_marks)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

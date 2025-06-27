# Flask Project 1

A simple Flask web application.

## 📋 Features

- 📄 Takes input as Student ID or Course ID from a form
- 📊 Displays student-wise marks and total
- 📈 Displays course-wise average, max marks, and a histogram
- ✅ Error handling for invalid IDs

## 🗂️ Folder Structure

```
project 1/
├── app.py
├── data.csv
├── static/
│   └── histogram.png
├── templates/
│   ├── index.html
│   ├── student_details.html
│   ├── course_details.html
│   └── error.html
└── README.md
```

## 🚀 How to Run

1. Install the required packages:
   ```bash
   pip install flask matplotlib
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## 📁 Notes

- Make sure `data.csv` is present in the same directory as `app.py`.
- The histogram image is auto-generated in the `static/` folder upon submitting a Course ID.
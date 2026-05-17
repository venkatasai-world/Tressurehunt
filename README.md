# 🏴‍☠️ Treasure Hunt Game

A fun and interactive web-based Treasure Hunt game where players choose directions to find the hidden treasure. Users must make the correct choices to successfully reach the treasure.

Built using Python Flask for the backend and HTML/CSS for the frontend. The project is fully ready for deployment on Render using Gunicorn.

---

## 🚀 Features

- Interactive treasure hunt gameplay
- Direction-based decision making
- Simple and attractive user interface
- Flask-powered backend
- Responsive frontend using HTML and CSS
- Ready for Render deployment with Gunicorn

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- Gunicorn

---

## 📂 Project Structure

```bash
Tressurehunt/
│
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ▶️ How the Game Works

The player starts the treasure hunt and must choose directions like:

- Left or Right
- Wait or Swim
- Select the correct door

Each correct decision takes the player closer to the treasure, while wrong choices end the game.

---

## 💻 Example Gameplay

```bash
You are at a crossroad.
Where do you want to go?

Type "left" or "right"
> left

You come to a lake.
Type "wait" to wait for a boat or "swim" to swim across.
> wait

You arrive at the island safely.
There are 3 doors: Red, Blue, Yellow.
Choose one door.
> yellow

🎉 Congratulations! You found the treasure!
```

---

## 📜 Flask Application Example

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/venkatasai-world/Tressurehunt.git
```

### 2️⃣ Navigate to the Project Folder

```bash
cd Tressurehunt
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application

```bash
python app.py
```

---

## 🌐 Render Deployment

This project is fully configured for deployment on Render using Gunicorn.

### Start Command

```bash
gunicorn app:app
```

---

## 📌 Requirements

Example `requirements.txt`

```txt
Flask
gunicorn
```

---

## 🎯 Learning Objectives

This project helps beginners understand:

- Flask Basics
- Routing in Flask
- Frontend and Backend Integration
- HTML/CSS Design
- User Interaction Handling
- Render Deployment

---

## 🌟 Future Improvements

- Add background music and sound effects
- Add animations and images
- Create multiple treasure levels
- Add score tracking system
- Make the game mobile responsive

---

## 🔗 GitHub Repository

:contentReference[oaicite:0]{index=0}

---

## 👨‍💻 Author

Created by Venkata Sai

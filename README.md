# VITAMIN-DEFICIENCY-DETECTION-using-image-processing-neural-network
# 🧪 Vitamin Deficiency Detection using Deep Learning

This Flask-based web application predicts vitamin deficiencies from user-uploaded images using a trained deep learning model.

## 🚀 Features

- Upload an image (e.g., skin condition)
- AI model detects vitamin type
- Returns predicted deficiency with detailed explanation
- Clean UI built with Flask

## 🛠 Tech Stack

- Python 🐍
- Flask 🌐
- TensorFlow / Keras 🧠
- HTML/CSS (Templates)
- Git & GitHub 💻
This project is an intelligent web-based system that uses deep learning to predict vitamin deficiencies based on visual clues in user-uploaded images (like facial skin, nails, or tongue).
Built with Flask, this AI-powered tool analyzes the image using a trained TensorFlow model and delivers meaningful predictions along with medically researched descriptions of the deficiency and its symptoms.

# 🔍 Problem Statement
Vitamin deficiencies often go unnoticed due to subtle physical symptoms. Early detection can prevent long-term health issues such as:
Eye problems (Vitamin A)
Weak immunity and fatigue (Vitamin B, C)
Bone issues (Vitamin D)
Nervous system problems (Vitamin E)
Traditional diagnosis requires expensive tests and doctor visits. This project demonstrates how AI can help in early screening using images.

# 🚀 Key Features
✅ Upload image for analysis
✅ AI model predicts vitamin deficiency (A, B, C, D, E)
✅ Rich description with symptoms and treatment tips
✅ Easy-to-use web interface built with Flask
✅ Real-time processing with immediate results
✅ Modular code structure for future improvement

# 🧰 Tech Stack
Component	Technology
Backend	Python, Flask
Machine Learning	TensorFlow (Keras)
Frontend	HTML, CSS, Jinja2
Deployment	Localhost / GitHub
File Handling	Werkzeug / Flask

# 📸 How It Works
User uploads an image (e.g. tongue, skin, eye area).
Flask server saves the image temporarily.
Image is sent to label_image.py, which loads a trained model and classifies it.
Flask returns the predicted vitamin type and description.
File is deleted after processing.

# Deficiency Information Included
Vitamin A – Vision issues, dry eyes, poor immunity
Vitamin B – Anemia, tiredness, nerve problems
Vitamin C – Scurvy, bleeding gums, weak skin
Vitamin D – Rickets, bone pain, muscle weakness
Vitamin E – Muscle and nerve damage, vision problems
Each prediction is followed by a detailed paragraph describing the medical significance and symptoms.

# Project Structure
vitamin-deficiency-detector/
│
├── app1.py               # Flask server
├── label_image.py        # AI model and prediction logic
├── templates/            # HTML pages (first.html, login.html, etc.)
├── static/               # CSS, images, etc.
├── model/                # Trained model files (e.g., .pb or .h5)
├── uploads/              # Temporary upload folder (auto-deleted)
├── .gitignore            # Git ignore rules
└── README.md             # Project description (this file)

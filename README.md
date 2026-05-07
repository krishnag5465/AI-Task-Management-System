# AI Powered Task Management System

Machine Learning based AI-powered task management system that predicts and manages tasks intelligently using NLP and classification models.

---

## Features

- Task classification
- Priority prediction
- NLP-based task analysis
- Multiple ML models
- Streamlit/Python interface

---

## Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- NLP
- Jupyter Notebook

---

## Project Structure

```text
AI-Task-Management-ML/
│
├── app.py
├── requirements.txt
├── README.md
├── ai_task_management_system.ipynb
```

---

## Dataset

The dataset files are not uploaded to GitHub because of large file size.

Download dataset from Google Drive:

[https://drive.google.com/file/d/1wd8_4-NglkuWItDjRKDalJ2QuetxEE9u/view?usp=drive_link]

After downloading, place the dataset inside the project folder.

---

## Model Files

The `.pkl` model files are not uploaded to GitHub.

They will be generated automatically after training the model.

Run:

```bash
python train_model.py
```

OR run the notebook:

```bash
ai_task_management_system.ipynb
```

This will automatically create:
- model.pkl
- final_model.pkl
- priority_model.pkl
- svm_model.pkl
- tfidf.pkl

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python app.py
```

---

## Author

Krishna Gupta
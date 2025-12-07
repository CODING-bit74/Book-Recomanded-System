# Book Recommendation System

A Flask + Machine Learning web application that recommends books based on user input.
It uses collaborative filtering on a user–book interaction matrix to find similar books.

## Features

- 🔥 **Popular Books Dashboard**
  - Displays the most popular books with title, author, cover image and vote count
  - Redesigned dark UI layout (responsive)

- 🎯 **Smart Recommendations**
  - Enter a book title to get similar recommendations
  - Combines collaborative filtering with content-aware metadata
  - Handles spelling variations and case-insensitive matches
  - Clean & responsive UI

- 🧠 **ML Artifacts**
  - `pt.pkl` — user-item pivot matrix
  - `similarity_scores.pkl` — precomputed similarity matrix
  - `books.pkl` — book metadata
  - `popular.pkl` — popular books dataframe

## Folder Structure

Book-Recomanded-System/
├── app.py
├── popular.pkl
├── pt.pkl
├── books.pkl
├── similarity_scores.pkl
├── requirements.txt
├── Dockerfile
└── templates/
├── index.html
└── recommend.html


How It Works

Popular Books: extracted from popular.pkl (e.g., by number of ratings, avg rating)

Recommendations:

Use the user–book pivot table pt.pkl

Precomputed cosine similarity in similarity_scores.pkl

When user supplies a title, fuzzy match to find nearest title

Return top N similar books (default 4)


Future Improvements

Autocomplete search bar (typeahead)

Improved similarity (hybrid: content + collaborative)

Streamlit version for rapid prototyping

Deploy on Render / Heroku / Railway / Vercel / Docker

Add rating preview & reviews

Add caching and async loading for large models

Author

AKM — Freelancer & ML Developer
Open to collaborations and AI projects.


1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Book-Recomanded-System.git
cd Book-Recomanded-System
pip install -r requirements.txt
python app.py
Open the app in your browser
Visit: http://127.0.0.1:5000
'''



## Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Book-Recomanded-System.git
cd Book-Recomanded-System
pip install -r requirements.txt
python app.py
Open the app in your browser
Visit: http://127.0.0.1:5000
'''

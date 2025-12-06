from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import sys

app = Flask(__name__)

# ---------- Helper: safe pickle loading ----------
def safe_load(path):
    if not os.path.exists(path):
        print(f"[FATAL] Missing file: {path}")
        sys.exit(1)
    with open(path, "rb") as f:
        return pickle.load(f)

# ---------- Load artifacts ----------
popular_df = safe_load('popular.pkl')
pt = safe_load('pt.pkl')
books = safe_load('books.pkl')
similarity_scores = safe_load('similarity_scores.pkl')

# Prepare lowercase index for case-insensitive search
pt_index_lower = [str(x).lower() for x in pt.index]


# ---------- Routes ----------

@app.route('/')
def index():
    # IMPORTANT: we are NOT using any 'avg_rating' column here
    book_name = list(popular_df['Book-Title'].values)
    author = list(popular_df['Book-Author'].values)
    image = list(popular_df['Image-URL-M'].values)
    votes = list(popular_df['num_ratings'].values)

    return render_template(
        'index.html',
        book_name=book_name,
        author=author,
        image=image,
        votes=votes
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', data=None, message=None)


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if not user_input:
        return render_template(
            'recommend.html',
            data=None,
            message="Please enter a book title."
        )

    user_input_clean = user_input.strip().lower()

    # Check if book exists case-insensitively
    if user_input_clean not in pt_index_lower:
        return render_template(
            'recommend.html',
            data=None,
            message=f"No exact match found for \"{user_input}\". Please check the spelling or try another title."
        )

    # Get index in pt
    index = pt_index_lower.index(user_input_clean)

    # Get similar items (skip itself at position 0)
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]  # top 4 similar

    data = []
    for i in similar_items:
        book_title = pt.index[i[0]]
        temp_df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')

        if temp_df.empty:
            continue

        title = temp_df['Book-Title'].values[0]
        author = temp_df['Book-Author'].values[0]
        image = temp_df['Image-URL-M'].values[0]

        data.append([title, author, image])

    if not data:
        msg = f"Couldn't find recommendations for \"{user_input}\" even though it exists in the matrix."
        return render_template('recommend.html', data=None, message=msg)

    return render_template('recommend.html', data=data, message=None)


if __name__ == '__main__':
    app.run(debug=True)

import streamlit as st

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Book Recommender", layout="wide")

import pickle
import numpy as np
import pandas as pd
import os
import sys


# ---------- Helper: safe pickle loading ----------
def safe_load(path):
    if not os.path.exists(path):
        st.error(f"Missing file: {path}")
        st.stop()
    with open(path, "rb") as f:
        return pickle.load(f)


# ---------- Load artifacts ----------
@st.cache_resource
def load_data():
    popular_df = safe_load('popular.pkl')
    pt = safe_load('pt.pkl')
    books = safe_load('books.pkl')
    similarity_scores = safe_load('similarity_scores.pkl')

    # Detect rating column
    rating_col = None
    possible_cols = ['avg_rating', 'Average Rating', 'average_rating', 'rating', 'Avg-Rating']
    for col in possible_cols:
        if col in popular_df.columns:
            rating_col = col
            break

    lower_index = [str(x).lower() for x in pt.index]

    return popular_df, pt, books, similarity_scores, rating_col, lower_index


popular_df, pt, books, similarity_scores, rating_col, pt_index_lower = load_data()


# ---------- Recommender Function ----------
def recommend_books(user_input: str):
    if not user_input:
        return [], "Please enter a book title."

    query = user_input.strip().lower()

    if query not in pt_index_lower:
        return [], f"No match found for '{user_input}'. Check spelling."

    idx = pt_index_lower.index(query)

    similar = sorted(
        list(enumerate(similarity_scores[idx])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    results = []
    for i in similar:
        book_title = pt.index[i[0]]
        df = books[books['Book-Title'] == book_title].drop_duplicates('Book-Title')

        if df.empty:
            continue

        results.append({
            "title": df['Book-Title'].values[0],
            "author": df['Book-Author'].values[0],
            "image": df['Image-URL-M'].values[0]
        })

    return results, None


# ---------- Streamlit UI ----------
st.title("📚 Book Recommendation System")

tab1, tab2 = st.tabs(["🔥 Popular Books", "🎯 Recommendations"])

# -------- Tab 1 ---------
with tab1:
    st.subheader("Top Popular Books")

    for i in range(0, len(popular_df), 4):
        cols = st.columns(4)

        for j, col in enumerate(cols):
            if i + j >= len(popular_df):
                break

            row = popular_df.iloc[i + j]

            with col:
                st.image(row['Image-URL-M'], use_column_width=True)
                st.markdown(f"**{row['Book-Title']}**")
                st.markdown(f"*{row['Book-Author']}*")

                if 'num_ratings' in popular_df.columns:
                    st.write(f"Votes: {row['num_ratings']}")

                if rating_col:
                    st.write(f"Rating: {row[rating_col]}")


# -------- Tab 2 ---------
with tab2:
    st.subheader("Find Similar Books")

    user_input = st.text_input("Enter a book title", "")

    if st.button("Recommend"):
        with st.spinner("Processing..."):
            results, error = recommend_books(user_input)

        if error:
            st.error(error)
        else:
            st.success(f"Books similar to **{user_input}**:")

            for i in range(0, len(results), 4):
                cols = st.columns(4)

                for j, col in enumerate(cols):
                    if i + j >= len(results):
                        break

                    book = results[i + j]

                    with col:
                        st.image(book["image"], use_column_width=True)
                        st.markdown(f"**{book['title']}**")
                        st.markdown(f"*{book['author']}*")

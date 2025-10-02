import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load data
with open("recommendation_data.pkl", "rb") as f:
    data = pickle.load(f)

book_pivot = data["book_pivot"]
similarity_scores = data["similarity_scores"]
isbn_to_title = data["isbn_to_title"]


# Load books data (used for images and authors)
books = pd.read_csv("Books_sample.csv")


# Load ratings data for popular books (ensure Ratings.csv is loaded)
ratings = pd.read_csv("Ratings.csv")

# Define recommendation function

def recommend_books_with_images(isbn, top_n=5):
    try:
        index = np.where(book_pivot.index == isbn)[0][0]
    except IndexError:
        return []

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n + 1]

    results = []
    for i, score in similar_items:
        similar_isbn = book_pivot.index[i]
        similar_title = isbn_to_title.get(similar_isbn, "Unknown Title")
        book_info = books[books["ISBN"] == similar_isbn].drop_duplicates("ISBN")
        if not book_info.empty:
            author = book_info["Book-Author"].values[0]
            image = book_info["Image-URL-M"].values[0]
            results.append((similar_title, author, image, round(score, 3)))
    return results

# Define popular books function

def get_popular_books(top_n=5):
    popular = ratings.groupby("ISBN").agg(
        avg_rating=("Book-Rating", "mean"),
        num_ratings=("ISBN", "count")
    ).sort_values(by=["num_ratings", "avg_rating"], ascending=False).head(top_n)

    results = []
    for isbn in popular.index:
        book_info = books[books["ISBN"] == isbn].drop_duplicates("ISBN")
        if not book_info.empty:
            title = book_info["Book-Title"].values[0]
            author = book_info["Book-Author"].values[0]
            image = book_info["Image-URL-M"].values[0]
            results.append((title, author, image))
    return results

# UI
st.title("📚 Book Recommender")

user_type = st.radio("Are you a new or existing user?", ("New User", "Existing User"))

if user_type == "Existing User":
    # Build a mapping only for books that exist in book_pivot
    valid_isbn = book_pivot.index
    valid_titles = [(isbn_to_title[isbn], isbn) for isbn in valid_isbn if isbn in isbn_to_title]

    # Dropdown: display titles, but store ISBN
    title_options = {title: isbn for title, isbn in valid_titles}
    selected_title = st.selectbox("Select a book you've read", list(title_options.keys()))
    selected_isbn = title_options[selected_title]

    if st.button("Recommend"):
        recs = recommend_books_with_images(selected_isbn)
        if recs:
            st.subheader("Recommended Books:")
            for title, author, image, score in recs:
                st.image(image, width=120)
                st.markdown(f"**{title}** by *{author}*")
                st.write(f"Similarity Score: {score}")
                st.markdown("---")
        else:
            st.warning("No recommendations found.")

else:  # New User
    st.subheader("Popular Books for You:")
    popular_books = get_popular_books(5)
    for title, author, image in popular_books:
        st.image(image, width=120)
        st.markdown(f"**{title}** by *{author}*")
        st.markdown("---")

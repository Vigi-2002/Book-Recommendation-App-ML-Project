📚 Book Recommender System

A Streamlit web app that provides personalized book recommendations based on user ratings. The app supports both new users (showing popular books) and existing users (based on books they've read).

🌐 Deployment

Try it live on Streamlit Cloud: https://book-recommendation-app-ml-project-yangdtg8ndrmv4celb6cyv.streamlit.app/

⚡ Features

Personalized Recommendations: Suggests books similar to those a user has read.

New User Support: Shows popular books for users who haven’t rated any books yet.

Author & Cover Info: Displays book author and cover image alongside recommendations.

Lightweight Deployment: All datasets and pickle files downsized to be GitHub-friendly (<25 MB).

🗂 Project Structure

book-recommendation-ml-project/

│

├─ book_app.py # Streamlit app

├─ data/

│ ├─ Users_sample.csv

│ ├─ Ratings_sample.csv

│ ├─ Books_sample.csv

│ └─ recommendation_data.pkl # Pickle with book pivot and similarity scores

├─ README.md

└─ requirements.txt

📊 Dataset

Users.csv: User data.

Ratings.csv: Book ratings.

Books_sample.csv: Sample of book metadata (title, author, cover image).

recommendation_data.pkl: Precomputed pivot table and similarity scores for quick recommendations.

🔧 Notes

All datasets are downsized to fit GitHub’s 25 MB file limit.

The app can be deployed directly on Streamlit Cloud.

👨‍💻 Author

Vigi-2002 – GitHub

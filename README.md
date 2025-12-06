📚 Book Recommendation System
A Flask + Machine Learning web application that recommends books based on user input.
The system uses collaborative filtering to find similar books using user–item interaction patterns.
🚀 Features
🔥 Popular Books Dashboard
Displays the most popular books
Shows title, author, cover image, and vote count
Fully redesigned dark-UI layout
🎯 Smart Recommendations
Enter a book title to get similar recommendations
Content-aware + collaborative filtering
Handles spelling variations (case-insensitive)
Clean UI with responsive design
🧠 ML Components
Preprocessed matrices (pt.pkl, similarity_scores.pkl)
Book metadata (books.pkl)
Popularity dataframe (popular.pkl)
💡 Built With
Python 3.x
Flask (backend)
HTML + CSS (UI)
Pickle (model artifacts)
NumPy, Pandas
📦 Folder Structure
Book-Recomanded-System/
│
├── app.py                     # Flask backend
├── popular.pkl                # Popular books dataframe
├── pt.pkl                     # Pivot table matrix
├── books.pkl                  # Books metadata
├── similarity_scores.pkl      # Calculated similarity matrix
│
└── templates/
    ├── index.html             # Popular Books UI
    └── recommend.html         # Recommendation UI
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/Book-Recomanded-System.git
cd Book-Recomanded-System
2️⃣ Install dependencies
pip install flask numpy pandas
3️⃣ Run the application
python app.py
4️⃣ Open the app in your browser
Visit:
http://127.0.0.1:5000
🧩 How It Works
Popular Books
Popular books are extracted using:
Number of ratings
Average ratings (if available)
Image & metadata from dataset
Recommendations
We compute similarity using:
User–Book interaction matrix (pt.pkl)
Cosine similarity on interaction vectors
Retrieve top 4 most similar books
🖼️ Screenshots
🔥 Popular Books Page
Add your screenshot here
🎯 Recommendation Page
Add your screenshot here
🚀 Future Improvements
Autocomplete search bar
Improved similarity scoring
Streamlit version (optional)
Deploy on Render/Netlify
Add rating preview & reviews
🧑‍💻 Author
AKM — Freelancer & ML Developer
💼 Open to collaborations and AI projects.

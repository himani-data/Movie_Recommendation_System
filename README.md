# 🎬 Movie Recommendation System  
✨ *Smart • Simple • Personalized* ✨  

A **content-based Movie Recommendation System** that suggests movies similar to the one you love — built using **Python, Machine Learning, and Streamlit**, and deployed as an interactive web app.

---

## 🌟 Project Highlights

🎥 Recommends **Top 5 similar movies**  
🧠 Uses **Cosine Similarity** for recommendations  
📊 Built on **TMDB 5000 Movies Dataset**  
🎨 Clean & interactive **Streamlit UI**  
🚀 Deployed using **Streamlit Cloud**

---

## 🎞️ Dataset Overview

This project uses the **TMDB 5000 Movie Dataset**, consisting of two main files:

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

📌 **Total Movies:** ~5000  
📌 **Source:** The Movie Database (TMDB)

---

## 🔄 Project Workflow (End-to-End)

### 1️⃣ Data Collection
- Loaded TMDB movies and credits datasets
- Selected relevant columns such as:
  - `title`, `overview`, `genres`
  - `keywords`, `cast`, `crew`

---

### 2️⃣ Data Preprocessing 🧹
- Converted JSON-like strings into Python lists
- Extracted:
  - Top 3 actors from cast
  - Director name from crew
- Removed missing & duplicate values
- Applied text normalization:
  - Lowercasing
  - Removing spaces for consistency

---

### 3️⃣ Feature Engineering ⚙️
- Created a **combined feature column** (`tags`) using:

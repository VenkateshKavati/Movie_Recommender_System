# Movie Recommender System

A content-based movie recommendation system that suggests similar movies based on a movie the user likes, using the TMDB 5000 Movie Dataset.

## Overview

This project analyzes movie metadata (genres, cast, crew, keywords, and overview) to compute similarity between movies. Given a movie title, it recommends a list of similar movies using cosine similarity on vectorized movie features.

## Dataset

- `tmdb_5000_movies.csv` — Movie metadata (title, genres, overview, keywords, etc.)
- `tmdb_5000_credits.csv` — Cast and crew information for each movie

Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) (Kaggle)

## How It Works

1. Movie metadata (genres, keywords, cast, crew, overview) is combined into a single text feature ("tags") for each movie.
2. Text is vectorized (e.g., using CountVectorizer / TF-IDF).
3. Cosine similarity is computed between all movie vectors and stored in `similarity.pkl`.
4. Processed movie data is stored in `movies.pkl`.
5. When a user selects a movie, the system looks up its similarity scores and returns the top N most similar movies.

## Project Files

| File | Description |
|------|-------------|
| `movies.pkl` | Preprocessed movie data used for lookup |
| `similarity.pkl` | Precomputed cosine similarity matrix |
| `tmdb_5000_movies.csv` | Raw movie metadata |
| `tmdb_5000_credits.csv` | Raw cast/crew data |

> Note: Large `.pkl` files are tracked using [Git LFS](https://git-lfs.github.com/).

## Installation

```bash
git clone https://github.com/VenkateshKavati/Movie_Recommender_System.git
cd Movie_Recommender_System
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then enter a movie title to get a list of recommended similar movies.

## Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn (CountVectorizer, cosine similarity)
- Streamlit (if used for the UI)

## Future Improvements

- Add collaborative filtering for personalized recommendations
- Deploy as a web app
- Add posters/images using the TMDB API

## Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the dataset
- Dataset hosted on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

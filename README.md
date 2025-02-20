# Simple Content-Based Movie Recommendation System 

## Overview
This is a simple **content-based recommendation system** that suggests movies based on a user's text input.

## Dataset 
- **Dataset Name:** [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Columns Used:** `title`, `overview`, `genres`, `keywords`
- **Preprocessing:** The dataset is cleaned, merged, and reduced to **500 movies** to ensure quick computation.


## Installation & Setup

### **Prerequisites**
Ensure you have:
- **Python 3.7+** installed
- **pip** installed (comes with Python)

### 1. **Clone the Repository**
```sh
git clone https://github.com/JoshuaLauu/lumaa-spring-2025-ai-ml.git
cd lumaa-spring-2025-ai-ml
```
### 2. **Create a Virtual Environment & Install Dependencies**
```sh
pip install -r requirements.txt
```

### 3. **Download & Place the Dataset**
Ensure `tmdb_5000_movies.csv` is placed in the `data/` directory.

## How to Run
Run the recommendation system using:
```sh
python src/recommend.py "I love thrilling action movies set in space, with a comedic twist."
```
or interactive mode:
```sh
python src/recommend.py`
```
Then, enter your preferences manually.

## Example Output


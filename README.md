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
**Open your terminal (CMD on Windows, Terminal on Mac/Linux) and run:**
```sh
git clone https://github.com/JoshuaLauu/lumaa-spring-2025-ai-ml.git
cd lumaa-spring-2025-ai-ml
```
This downloads the entire source code from GitHub to your computer.
It creates a new folder named lumaa-spring-2025-ai-ml.
The `cd` command lets you move into the project directory for the next command followed.

### 2. **Create a Virtual Environment & Install Dependencies**
```sh
pip install -r requirements.txt
```
This installs all the required Python libraries 
### 3. **Download & Place the Dataset**
Ensure `tmdb_5000_movies.csv` is placed in the `data/` directory.

## How to Run
Run the recommendation system using:
```sh
python src/recommend.py
```
Then, enter your preferences manually (e.g., "I like action movies set in space").

## Example Output
### After running the recommendation system, the output will look like this:

Enter your preferences: e.g., "I like action movies set in space"

Top Recommendations:

1. Spaceballs (Score: 0.3444)  
    Genres: Comedy, Science Fiction

2. Cargo (Score: 0.3441)     
             Genres: Thriller, Mystery, Science Fiction

3. Mission to Mars (Score: 0.2987)              
   Genres: Science Fiction



✔ **The system ranks movies based on relevance to your input query.**  
✔ **The higher the score, the more relevant the recommendation.**  
✔ **Genres are displayed to help users understand the movie themes.**  

---
## Future Improvements

### **Possible Improvements**
- **Use BM25 instead of cosine similarity** (better ranking for text-based search)  
- **Expand to Hybrid Filtering** (combine content-based & collaborative filtering)  
- **Improve dataset filtering** (e.g., allow filtering by release year, director, etc.) 

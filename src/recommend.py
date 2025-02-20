import os
import sys
from utils import ContentRecommender

def main():
    # Get absolute path to the dataset
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
    dataset_path = os.path.join(script_dir, "..", "data", "tmdb_5000_movies.csv")  # Construct full path

    # Check if file exists before proceeding
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset not found at {dataset_path}")
        print("Make sure tmdb_5000_movies.csv is placed in the 'data/' directory.")
        return

    # Load the recommender
    recommender = ContentRecommender(dataset_path)

    # Get user input
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("Enter your preferences: ")

    # Get recommendations
    recommendations, scores = recommender.get_recommendations(user_query)

    # Display results
    print("\nTop Recommendations:")
    for i, (row, score) in enumerate(zip(recommendations.iterrows(), scores)):
        index, data = row
        print(f"\n{i + 1}. {data['title']} (Score: {score:.4f})")
        print(f"   Genres: {data['genres']}")



if __name__ == "__main__":
    main()


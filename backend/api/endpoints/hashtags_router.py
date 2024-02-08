from typing import List, Tuple
from fastapi import APIRouter, HTTPException, Query
import csv

# Create an APIRouter instance to organize routes
router = APIRouter()

# Sample data path
CSV_FILE_PATH = "data/top_hashtags_data.csv"

def read_csv_data(file_path: str) -> List[dict]:
    """
    Read data from a CSV file and return it as a list of dictionaries.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        List[dict]: List of dictionaries representing the CSV data.
    """
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def get_top_hashtags(data: List[dict], start_date: str, end_date: str) -> List[Tuple[str, int]]:
    """
    Calculate the top hashtags based on click counts within a specified date range.

    Args:
        data (List[dict]): List of dictionaries representing the CSV data.
        start_date (str): Start date in the format "YYYY-MM-DD HH:MM:SS".
        end_date (str): End date in the format "YYYY-MM-DD HH:MM:SS".

    Returns:
        List[Tuple[str, int]]: List of tuples containing top hashtags and their click counts.
    """
    # Filter data based on the specified date range
    filtered_data = [entry for entry in data if start_date <= entry["DateTime"] <= end_date]

    # Dictionary to store hashtag counts
    hashtag_counts = {}

    # Iterate over filtered data
    for entry in filtered_data:
        # Extract hashtags from the "PostContent" field
        hashtags = [tag.strip("#") for tag in entry["PostContent"].split() if tag.startswith("#")]

        # Update hashtag counts in the dictionary
        for hashtag in hashtags:
            hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + int(entry["Clicks"])

    # Sort hashtags based on click counts in descending order and select the top 5
    top_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Return the list of tuples containing top hashtags and their click counts
    return top_hashtags

# Define a route for the "/top_hashtags" endpoint
@router.get("/top_hashtags")
async def get_top_hashtags_api(start_date: str = Query(..., description="Start date (YYYY-MM-DD HH:MM:SS)"),
                               end_date: str = Query(..., description="End date (YYYY-MM-DD HH:MM:SS)")) -> dict:
    """
    Endpoint to get the top hashtags within a specified date range.

    Args:
        start_date (str): Start date in the format "YYYY-MM-DD HH:MM:SS".
        end_date (str): End date in the format "YYYY-MM-DD HH:MM:SS".

    Returns:
        dict: JSON response containing the top hashtags and their click counts.
    """
    try:
        # Read data from the CSV file
        data = read_csv_data(CSV_FILE_PATH)

        # Calculate top hashtags within the specified date range
        top_hashtags = get_top_hashtags(data, start_date, end_date)

        # Return the result as a JSON response
        return {"top_hashtags": top_hashtags}

    except Exception as e:
        # Raise an HTTPException with a 500 status code if an exception occurs
        raise HTTPException(status_code=500, detail=str(e))

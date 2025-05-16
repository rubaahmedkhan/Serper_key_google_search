import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Serper API key from environment variable
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_API_KEY="757f224e2ead8dcde87f06413e7919051dc1fe67"

# Check if API key is set
if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set. Please set it in the .env file.")

def search_web(query: str, num_results: int = 5) -> list:
    """
    Perform a Google search using the Serper API and return formatted results.
    Args:
        query (str): The search query.
        num_results (int): Number of results to return (default: 5).
    Returns:
        list: List of dictionaries containing title, url, and snippet.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "q": query,
        "num": num_results
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        results = response.json().get("organic", [])
        
        if not results:
            return [{"title": "No Results", "url": "", "snippet": "No results found for the query."}]
        
        formatted_results = []
        for result in results[:num_results]:
            formatted_results.append({
                "title": result.get("title", "No Title"),
                "url": result.get("link", ""),
                "snippet": result.get("snippet", "No snippet available.")
            })
        return formatted_results
    
    except requests.exceptions.HTTPError as http_err:
        return [{"title": "HTTP Error", "url": "", "snippet": f"HTTP error occurred: {http_err}"}]
    except requests.exceptions.Timeout:
        return [{"title": "Timeout Error", "url": "", "snippet": "The request timed out. Please try again later."}]
    except requests.exceptions.RequestException as req_err:
        return [{"title": "Request Error", "url": "", "snippet": f"Error occurred: {req_err}"}]

def print_results(results: list):
    """
    Print search results in a formatted way.
    Args:
        results (list): List of result dictionaries.
    """
    print("\nSearch Results:")
    print("=" * 50)
    for i, result in enumerate(results, 1):
        print(f"Result {i}:")
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Snippet: {result['snippet']}")
        print("-" * 50)

def main():
    """Main function to get user query and display search results."""
    print("Simple Google Search using Serper API")
    print("Enter 'exit' to quit.")
    
    while True:
        query = input("\nEnter your search query: ").strip()
        if query.lower() == "exit":
            print("Exiting program.")
            break
        if not query:
            print("Please enter a valid query.")
            continue
        
        results = search_web(query)
        print_results(results)

if __name__ == "__main__":
    main()
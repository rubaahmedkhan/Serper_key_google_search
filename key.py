import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_API_KEY = "757f224e2ead8dcde87f06413e7919051dc1fe67"

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY is not set. Please set it in the .env file.")

def search_web(query: str, num_results: int = 5) -> list:
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
        response.raise_for_status()
        results = response.json().get("organic", [])
        
        if not results:
            return [{"title": "No Results", "snippet": "No results found for the query."}]
        
        formatted_results = []
        for result in results[:num_results]:
            formatted_results.append({
                "title": result.get("title", "No Title"),
                "snippet": result.get("snippet", "No snippet available.")
            })
        return formatted_results
    
    except requests.exceptions.HTTPError as http_err:
        return [{"title": "HTTP Error", "snippet": f"HTTP error occurred: {http_err}"}]
    except requests.exceptions.Timeout:
        return [{"title": "Timeout Error", "snippet": "The request timed out. Please try again later."}]
    except requests.exceptions.RequestException as req_err:
        return [{"title": "Request Error", "snippet": f"Error occurred: {req_err}"}]

def main():
    while True:
        query = input("").strip()
        if query.lower() == "exit":
            break
        if not query:
            print("Please enter a valid query.")
            continue
        
        results = search_web(query)
        for result in results:
            print(f"{result['title']}: {result['snippet']}")

if __name__ == "__main__":
    main()
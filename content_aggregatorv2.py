import requests
import json


# Function to fetch content from the Google News API
def fetch_from_google_news(api_key, query="technology", language="en"):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': query,
        'language': language,
        'apiKey': api_key,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = []
        for item in data['articles']:
            articles.append({
                'title': item['title'],
                'link': item['url'],
                'summary': item['description'],
                'published': item['publishedAt']
            })
        return articles
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []


# Function to aggregate content from different sources
def aggregate_content(*sources):
    aggregated_articles = []
    for source in sources:
        if source:
            aggregated_articles.extend(source)
    return aggregated_articles


# Function to display the aggregated content
def display_articles(articles):
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary']}")
        print(f"Published: {article.get('published', 'N/A')}")
        print("-" * 80)


# Optional: Save the aggregated content to a JSON file
def save_to_json(articles, filename):
    with open(filename, 'w') as f:
        json.dump(articles, f, indent=4)


# Main function to run the aggregator
def main():
    api_key = "bed82c87a346440886b70394647327fb"  # Replace with your Google News API key

    # Get user input for search query and language
    query = input("Enter the search query: ")
    language = input("Enter the language code (e.g., en for English, fr for French): ")

    # Fetch articles based on user input
    google_news_articles = fetch_from_google_news(api_key, query=query, language=language)

    # Aggregate content (you can add more sources if needed)
    all_articles = aggregate_content(google_news_articles)

    # Display the aggregated articles
    display_articles(all_articles)

    # Optionally, save the aggregated articles to a file
    save_to_json(all_articles, 'aggregated_content.json')


if __name__ == "__main__":
    main()

# News App

News App is a Python-based application that provides users with the latest news articles from various sources. It leverages external news APIs to fetch and display up-to-date news information.

## Features

- Fetch and display the latest news articles.
- Filter news articles by categories such as sports, technology, business, and more.
- Search for specific news topics.
- Save favorite articles for later viewing.
- Responsive and user-friendly web interface.

## Installation

Follow these steps to set up and run the News App:

1. Clone the repository:

git clone https://github.com/Musa-Tahawar/news-app.git


The app will be accessible in your web browser at `http://localhost:5000`.

## Usage

1. Upon running the app, you'll see the home page with a list of the latest news articles.
2. Use the navigation bar to filter news by category or search for specific topics.
3. Click on an article to view the full content.
4. Save your favorite articles by clicking the "Save" button.

## Configuration

The News App uses external news APIs to fetch data. To configure these APIs and other settings, you can modify the `config.py` file. Here's an example configuration:

```python
# config.py

NEWS_API_KEY = 'your_news_api_key'
NEWS_API_BASE_URL = 'https://newsapi.org/v2'
SECRET_KEY = 'your_secret_key'
DEBUG = True

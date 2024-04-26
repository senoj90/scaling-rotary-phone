import streamlit as st
import requests
import pandas as pd

# NewsAPI key
API_KEY = 'your_api_key_here'

def fetch_news(company):
    """ Fetch news articles from NewsAPI for a specific company. """
    url = f"https://newsapi.org/v2/everything?q={company}&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles

def main():
    st.title('Supply Chain News Fetcher')
    
    company = st.text_input("Enter the company name:", "Apple")
    
    if st.button("Fetch News"):
        with st.spinner('Fetching news...'):
            articles = fetch_news(company)
            if articles:
                for article in articles:
                    st.subheader(article['title'])
                    st.write("Published At:", article['publishedAt'])
                    st.write(article['description'])
                    st.markdown(f"[Read More]({article['url']})")
                    st.write("---")
            else:
                st.error("No news articles found.")
    
if __name__ == "__main__":
    main()

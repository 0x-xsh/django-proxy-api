import os

import requests
from django.utils import timezone
import schedule
from rest_framework.response import Response
from rest_framework import status

from news.models import Article


"""
    Function to fetch latest news periodically
    :return: None
    """


def fetch_latest():
     
       
        
        api_key = os.getenv('NEWS_API_KEY')
                
        country_code = 'ae' 
        
        url = f'https://newsapi.org/v2/top-headlines?apiKey={api_key}&country={country_code}'

        try:
            response = requests.get(url)
           

            data = response.json()
            articles = data.get('articles', [])

            if not articles:
                return Response({'error': 'No articles found'}, status=status.HTTP_404_NOT_FOUND)

            # Save articles directly to the model
            saved_articles = []
            for article_data in articles:
                # Extract source information
                source_data = article_data.get('source', {})
                source_id = source_data.get('id', '')
                source_name = source_data.get('name', '')

                # Combine source information with other article attributes
                article_data.update({'source_id': source_id, 'source_name': source_name})

                # Remove source field from original article data
                article_data.pop('source', None)

                # Directly create and save the Article object 
                Article.objects.create(
                    source_id=article_data.get('source_id', ''),
                    source_name=article_data.get('source_name', ''),
                    author=article_data.get('author', ''),
                    title=article_data.get('title', ''),
                    description=article_data.get('description', ''),
                    url=article_data.get('url', ''),
                    url_to_image=article_data.get('url_to_image', ''),
                    published_at=article_data.get('published_at', timezone.now()),
                    content=article_data.get('content', '')
                )

                saved_articles.append(article_data)
                
            print(f'Fetched {len(saved_articles)} Article ')
        except Exception as e:
            print(e)

        

schedule.every(10).seconds.do(fetch_latest)

while True: 
    schedule.run_pending()
    
     

            

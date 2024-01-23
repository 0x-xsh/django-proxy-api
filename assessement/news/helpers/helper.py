from django.utils import timezone

import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from news.models import Article



"""
    Function to process api requests, shared amongst views
    :return: Response
    """




def process_api_request(url, page_size, page):
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        articles = data.get('articles', [])

        if articles:
            total_results = data.get('totalResults', 0)
            total_pages = (total_results + page_size - 1) // page_size

            # Check if the provided page number is valid given a page size
            if page > total_pages and page_size:
                return Response({'error': 'Invalid page number'}, status=status.HTTP_400_BAD_REQUEST)

            

            # Include additional information in the response
            response_data = {
                'articles': articles,
                'total_pages': total_pages,
                'total_results': total_results,                
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return Response({"error": "No Article Corresponds to your search"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data, status=response.status_code)








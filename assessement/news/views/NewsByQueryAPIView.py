import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from news.helpers.helper import process_api_request

# Retrieve the News API key from the environment variables
api_key = os.getenv('NEWS_API_KEY')

class NewsByQueryAPIView(APIView):
    def get(self, request, format=None):
        # Retrieve the 'q' parameter from the query parameters
        search_query = request.query_params.get('q', '')

        # Check if the 'q' parameter is missing
        if not search_query:
            return Response({'error': 'missing q parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for any additional query parameters other than 'q', 'pageSize', and 'page'
        additional_params = set(request.query_params.keys()) - {'q', 'pageSize', 'page'}
        if additional_params:
            return Response({'error': f'Invalid query parameters: {", ".join(additional_params)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract 'pageSize' and 'page' parameters from the query parameters, defaulting to 20 and 1 respectively
        page_size = int(request.query_params.get('pageSize', 20))
        page = int(request.query_params.get('page', 1))

        # Construct the URL for fetching top headlines based on the provided search query
        url = f'https://newsapi.org/v2/top-headlines?q={search_query}&pageSize={page_size}&page={page}&apiKey={api_key}'

        # Delegate the API request processing to a helper function
        # The helper function handles making the request, checking for errors, and returning the response
        return process_api_request(url, page_size, page)
   
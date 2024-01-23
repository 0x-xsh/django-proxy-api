import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from news.helpers.helper import process_api_request

# Retrieve the News API key from the environment variables
api_key = os.getenv('NEWS_API_KEY')

class NewsBySourceAPIView(APIView):
    def get(self, request, format=None):
        # Retrieve the 'id' parameter from the query parameters
        source_id = request.query_params.get('id', '')

        # Check if the 'id' parameter is missing
        if not source_id:
            return Response({'error': 'missing id parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for any additional query parameters other than 'id', 'pageSize', and 'page'
        additional_params = set(request.query_params.keys()) - {'id', 'pageSize', 'page'}
        if additional_params:
            return Response({'error': f'Invalid query parameters: {", ".join(additional_params)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract 'pageSize' and 'page' parameters from the query parameters, defaulting to 20 and 1 respectively
        page_size = int(request.query_params.get('pageSize', 20))
        page = int(request.query_params.get('page', 1))

        # Construct the URL for fetching top headlines from the News API
        url = f'https://newsapi.org/v2/top-headlines?sources={source_id}&pageSize={page_size}&page={page}&apiKey={api_key}'

        # Delegate the API request processing to a helper function
        # The helper function handles making the request, checking for errors, and returning the response
        return process_api_request(url, page_size, page)

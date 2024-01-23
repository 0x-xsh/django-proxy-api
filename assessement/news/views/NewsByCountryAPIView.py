import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from news.helpers.helper import process_api_request

# Retrieve the News API key from the environment variables
api_key = os.getenv('NEWS_API_KEY')

class NewsByCountryAPIView(APIView):
    # List of allowed country codes for the 'id' parameter
    ALLOWED_COUNTRY_CODES = [
        'ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co',
        'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie',
        'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng',
        'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se',
        'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za'
    ]

    def get(self, request, format=None):
        # Retrieve the 'id' parameter (country code) from the query parameters
        country_code = request.query_params.get('id', '')

        # Check if the 'id' parameter (country code) is missing
        if not country_code:
            return Response({'error': 'missing id parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the provided country code is in the list of allowed country codes
        if country_code not in self.ALLOWED_COUNTRY_CODES:
            return Response({'error': 'Invalid country code id', 'ALLOWED_Country_CODES' : self.ALLOWED_COUNTRY_CODES}, status=status.HTTP_400_BAD_REQUEST)

        # Check for any additional query parameters other than 'id', 'pageSize', and 'page'
        additional_params = set(request.query_params.keys()) - {'id', 'pageSize', 'page'}
        if additional_params:
            return Response({'error': f'Invalid query parameters: {", ".join(additional_params)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract 'pageSize' and 'page' parameters from the query parameters, defaulting to 20 and 1 respectively
        page_size = int(request.query_params.get('pageSize', 20))
        page = int(request.query_params.get('page', 1))

        # Construct the URL for fetching top headlines based on the provided country code
        url = f'https://newsapi.org/v2/top-headlines?country={country_code}&pageSize={page_size}&page={page}&apiKey={api_key}'

        # Delegate the API request processing to a helper function
        # The helper function handles making the request, checking for errors, and returning the response
        return process_api_request(url, page_size, page)
 
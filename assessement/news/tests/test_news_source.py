import django
import pytest
from rest_framework.test import APIClient

# Set up Django for testing
django.setup()

# Create an instance of the API client and specify the URL for the news source API endpoint
client = APIClient()
url = '/api/v1/news/source'

# Test for the scenario where the 'id' parameter is missing
def test_missing_id_parameter():
    response = client.get(url)
    assert response.status_code == 400
    assert response.json() == {'error': 'missing id parameter'}

# Test for the scenario where a valid source ID is provided
def test_valid_source_id():
    response = client.get(f'{url}?id=bbc-news')
    assert response.status_code == 200

# Test for the scenario where additional parameters are included in the request
def test_additional_parameters():
    response = client.get(f'{url}?id=bbc-news&invalid_param=1')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid query parameters: invalid_param'}

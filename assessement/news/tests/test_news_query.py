import django
import pytest
from rest_framework.test import APIClient

# Set up Django for testing
django.setup()

# Create an instance of the API client and specify the URL for the news query API endpoint
client = APIClient()
url = '/api/v1/news/query'

# Test for the scenario where the 'q' parameter is missing
def test_missing_q_parameter():
    response = client.get(url)
    assert response.status_code == 400
    assert response.json() == {'error': 'missing q parameter'}

# Test for the scenario where a valid query is provided
def test_valid_query():
    response = client.get(f'{url}?q=palestine')
    assert response.status_code == 200

# Test for the scenario where additional parameters are included in the request
def test_additional_parameters():
    response = client.get(f'{url}?q=bitcoin&invalid_param=1')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid query parameters: invalid_param'}

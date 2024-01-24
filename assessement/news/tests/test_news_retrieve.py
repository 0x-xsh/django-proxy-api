import django
import pytest
from rest_framework.test import APIClient
from news.models import Article

# Set up Django for testing
django.setup()

# Create an instance of the API client and specify the URL for the RetrieveNewsAPIView endpoint
client = APIClient()
url = '/api/v1/news'

# Test for the scenario where the 'sourceid' parameter is missing
def test_missing_sourceid_parameter():
    response = client.get(url)
    assert response.status_code == 400
    assert response.json() == {'error': 'missing sourceid parameter'}



# Test for the scenario where a valid source_id is provided
def test_valid_source_id():
    # Create a test article
    Article.objects.create(source_id='test', title='Test Article')
    response = client.get(f'{url}?sourceid=test')
    assert response.status_code == 200
    assert 'articles' in response.json()

# Test for the scenario where an invalid source_id is provided
def test_invalid_source_id():
    response = client.get(f'{url}?sourceid=invalid')
    assert response.status_code == 200
    assert response.json()['articles'] == []
    

# Test for the scenario where additional parameters are included in the request
def test_additional_parameters():
    response = client.get(f'{url}?sourceid=test&invalid_param=1')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid query parameters: invalid_param'}

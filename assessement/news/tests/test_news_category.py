# Import necessary modules from Django and third-party libraries
import django
from django.conf import settings
import pytest
from rest_framework.test import APIClient

# Set up Django for testing
django.setup()

# Create an instance of the API client
client = APIClient()

# Test for the scenario where the 'id' parameter is missing
def test_missing_id_parameter():
    # Make a GET request to the category endpoint without the required 'id' parameter
    response = client.get('/api/v1/news/category')
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Assert that the response JSON matches the expected error message for missing 'id' parameter
    assert response.json() == {'error': 'missing id parameter'}

# Test for different valid categories using pytest's parametrize
@pytest.mark.parametrize("category", ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'])
def test_valid_category(category):
    # Make a GET request to the category endpoint with a valid category parameter
    response = client.get(f'/api/v1/news/category?id={category}')
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

# Test for the scenario where an invalid category is provided
def test_invalid_category():
    # Make a GET request to the category endpoint with an invalid category parameter
    response = client.get('/api/v1/news/category?id=invalid')
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Assert that the response JSON contains the expected error message and allowed categories
    assert response.json() == {'error': 'Invalid category id', 'ALLOWED_CATEGORIES': ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']}

# Test for the scenario where additional parameters are included in the request
def test_additional_parameters():
    # Make a GET request to the category endpoint with additional invalid parameters
    response = client.get('/api/v1/news/category?id=business&invalid_param=1')
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Assert that the response JSON matches the expected error message for additional parameters
    assert response.json() == {'error': 'Invalid query parameters: invalid_param'}

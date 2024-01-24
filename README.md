# Django Proxy API

Django Proxy API is a simple Django application that serves as a proxy to NEWS API, allowing you to make HTTP requests to it while adding flexibility and customization.


## Prerequisites
- Docker installed on your machine.

## How to Run
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/0x-xsh/django-proxy-api.git
    cd django-proxy-api
    ```
2. **Adjust Environment Variables**:
    Open the existing .env file and configure the following variables as needed:
    - `NEWS_API_KEY`: Your News API Key
    - PostgreSQL Docker Variables:
        - `POSTGRES_DB`: Set to `newsdb`.
        - `POSTGRES_USER`: Set to `nazim`.
        - `POSTGRES_PASSWORD`: Set to `nazim`.
    - Django App SQL Variables:
        - `SQL_HOST`: Set to `db`.
        - `SQL_PORT`: Set to `5432`.
    

3. **Run Docker Compose**:
    ```bash
    docker compose up --build
    ```
    This will build and start the Django Proxy API service defined in the docker-compose.yml file.
    ## Run Periodic News Fetch Job

    Open a new terminal and execute the following commands to enter the web container and run the periodic job fetching news data every 10 seconds, Use it to Fill up the DB to later query the data:
      
      ```bash
      docker exec -it news-app-web-1 /bin/bash
      python manage.py shell < ./news/views/news_fetch_latest_job.py
      ```
    ## Run Tests
    
    Open a new terminal and execute the following commands to enter the web container, set the Django settings module, and run tests using pytest:
    
    ```bash
    docker exec -it news-app-web-1 /bin/bash
    export DJANGO_SETTINGS_MODULE=assessement.settings
    pytest
    ```


 # API Usage

## 1. Get News by Country
- **Endpoint**: `/api/v1/news/country`
- **Method**: `GET`
- **Description**: Retrieve news articles based on the specified country.
- **Query Parameters**:
    - `id` (required): The country code. Allowed country codes: 'ae', 'ar', 'at', 'au', ... (complete list available in the code).
- **Example**:
    ```bash
    GET /api/v1/news/country?id=us
    ```

## 2. Get News by Category
- **Endpoint**: `/api/v1/news/category`
- **Method**: `GET`
- **Description**: Retrieve news articles based on the specified category.
- **Query Parameters**:
    - `id` (required): The category. Allowed categories: 'business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology'.
- **Example**:
    ```bash
    GET /api/v1/news/category?id=technology
    ```

## 3. Get News by Source
- **Endpoint**: `/api/v1/news/source`
- **Method**: `GET`
- **Description**: Retrieve news articles from a specific news source.
- **Query Parameters**:
    - `id` (required): The source ID. Available source IDs can be found on NewsAPI, e.g., 'google-news', 'cbs-news', etc.
- **Example**:
    ```bash
    GET /api/v1/news/source?id=google-news
    ```

## 4. Get News by Query
- **Endpoint**: `/api/v1/news/query`
- **Method**: `GET`
- **Description**: Retrieve news articles based on a custom query.
- **Query Parameters**:
    - `q` (required): The query string.
- **Example**:
    ```bash
    GET /api/v1/news/query?q=Django
    ```

## 5. Retrieve All News by A Source Id
- **Endpoint**: `/api/v1/news/`
- **Method**: `GET`
- **Description**: Retrieve all news articles.
- **Query Parameters**:
    - `sourceid` (required): The identifier for the source.
- **Example**:
    ```bash
    GET /api/v1/news?sourceid=google-news
    ```

**Note**: The above examples assume that the Django app is running on `http://localhost:8000`. Adjust the base URL accordingly if your deployment differs.

## Status Codes
- `200 OK`: Successful retrieval of news articles.
- `400 Bad Request`: Invalid or missing query parameters.
- `500 Internal Server Error`: Unexpected error on the server side.




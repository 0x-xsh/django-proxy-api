from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from news.serializers.ArticleSerializer import ArticleSerializer

from django.core.cache import cache
from news.models import Article

class RetrieveNewsAPIView(APIView):
    
    def get(self, request, format=None):
        
        
        source_id = request.query_params.get('sourceid', '')

        # Check if the 'id' parameter is missing
        if not source_id:
            return Response({'error': 'missing sourceid parameter'}, status=status.HTTP_400_BAD_REQUEST)

        # Check for any additional query parameters other than 'id', 'pageSize', and 'page'
        additional_params = set(request.query_params.keys()) - {'sourceid'}
        if additional_params:
            return Response({'error': f'Invalid query parameters: {", ".join(additional_params)}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Define the source_id you want to retrieve news for
        source_id = source_id
        
        # Check if the data is in the cache
        cached_articles = cache.get(source_id)
        
        if cached_articles is not None:
            # If data is in the cache, return it
            return Response({'articles': cached_articles}, status=status.HTTP_200_OK)
        
        # If data is not in the cache, retrieve it from the database
        articles = Article.objects.filter(source_id=source_id)
        
        # Serialize the data
        serializer = ArticleSerializer(articles, many=True)
        
        # Cache the data for future requests (set an appropriate timeout)
        cache.set(source_id, serializer.data, timeout=60)
        
        return Response({'articles': serializer.data}, status=status.HTTP_200_OK)

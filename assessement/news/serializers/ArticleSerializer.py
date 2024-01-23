from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    source_id = serializers.CharField(allow_null=True)
    source_name = serializers.CharField(allow_null=True)
    author = serializers.CharField(allow_null=True)
    title = serializers.CharField(allow_null=True)
    description = serializers.CharField(allow_null=True)
    url = serializers.CharField(allow_null=True)
    url_to_image = serializers.CharField(allow_null=True)
    published_at = serializers.DateTimeField(allow_null=True)
    content = serializers.CharField(allow_null=True)

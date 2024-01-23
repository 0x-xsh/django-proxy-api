from django.db import models


class Article(models.Model):
    source_id = models.TextField(null=True, db_index=True)
    source_name = models.TextField(null=True)
    author = models.TextField(null=True)
    title = models.TextField(null=True)
    description = models.TextField(null=True, max_length=255)
    url = models.TextField(null=True)
    url_to_image = models.TextField(null=True)
    published_at = models.DateTimeField(null=True)
    content = models.TextField(null=True)
   
    

    

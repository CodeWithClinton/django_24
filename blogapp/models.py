from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    title = models.CharField(max_length=50, unique=True)
    slug=models.SlugField(blank=True, null=True)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to="img")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.body
    
    
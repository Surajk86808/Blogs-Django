from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Catergory(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Catergory"
        verbose_name_plural = "Catergories" 
        
    def __str__(self):
        return  self.category_name   
    
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    catergory = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    sort_description = models.CharField(max_length=300)
    blog_body = models.TextField() 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs" 
        
    def __str__(self):
        return  self.title
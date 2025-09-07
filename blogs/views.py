from django.shortcuts import redirect, render
from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    # fetching posts by category logic here
    posts_new = Blog.objects.filter(status="published",category = category_id).order_by('-created_at')
    try:
        category_id = Category.objects.get(pk = category_id)
    except:
        return  ('home')
        
    context = {
        'post_new' : posts_new,
        'category_id' : category_id,
    }
    return render(request,"posts_by_category.html",context)
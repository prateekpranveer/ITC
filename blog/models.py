from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    meta = models.TextField(max_length=1000)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    header_img = models.ImageField(upload_to='images/', default=None)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
    
    
    def __unicode__(self):
       return '%s' % self.title


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(max_length=1000, blank=True)



    def __unicode__(self):
       return '%s' % self.title

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(max_length=1000, blank=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE)



    def __unicode__(self):
       return '%s' % self.title

    def __str__(self):
        return self.title

from django.urls import reverse
from organizer.models import Team, Tag
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=31,
        unique_for_month='pub_date',
        help_text='A label for URL config')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='blog_posts')
    teams = models.ManyToManyField(
        Team,
        blank=True,
        related_name='blog_posts')

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'

    def __str__(self):
            return "{}:{}".format(
                self.title, self.pub_date.strftime('%Y-%m-%d'))
    
    
    def get_absolute_url(self):
        return reverse(
            'blog_post_detail',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_delete_url(self):
        return reverse(
            'blog_post_delete',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'blog_post_update',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})
    
    

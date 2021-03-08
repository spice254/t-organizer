from django.urls import reverse
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.')
    
    class Meta:
            ordering = ['name']

    def __str__(self):
            return self.name.title()
    
    def get_absolute_url(self):
        return reverse('organizer_tag_detail',
                       kwargs={'slug': self.slug})
    
    def get_update_url(self):
        return reverse('organizer_tag_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('organizer_tag_delete',
                       kwargs={'slug': self.slug})

    

class Team(models.Model):
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField()
    tags = models.ManyToManyField(Tag, blank=True)
    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def __str__(self):
            return self.name.title()
    
    def get_absolute_url(self):
        return reverse('organizer_team_detail',
                       kwargs={'slug': self.slug})
    def get_update_url(self):
        return reverse('organizer_team_update',
                       kwargs={'slug': self.slug})
    def get_delete_url(self):
        return reverse('organizer_team_delete',
                       kwargs={'slug': self.slug})
    
class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=63)
    
    def __str__(self):
            return "{}:{}".format(
                self.team, self.title)
    
    def get_absolute_url(self):
        return self.team.get-absolute_url()
    
    def get_update_url(self):
        return reverse(
            'organizer_newslink_update',
            kwargs={'pk': self.pk}
        )
    def get_delete_url(self):
        return reverse('organizer_newslink_delete',
                       kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        unique_together= ('slug','team')
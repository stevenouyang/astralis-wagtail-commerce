from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

class NewsEmail(models.Model):
    email   = models.EmailField()
    
    panels = [
        FieldPanel("email")
    ]
    
    def __str__(self):
        return self.email
    
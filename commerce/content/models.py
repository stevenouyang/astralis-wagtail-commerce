from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

class SliderContent(models.Model):
    title           = models.CharField(max_length=40, blank=True, null=True)
    subtitle        = models.CharField(max_length=80, blank=True, null=True)
    image           = models.ImageField(upload_to="slider", blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image_1200x540  = ImageSpecField(
                    source="image",
                    processors=[ResizeToFill(1200, 540)],
                    format="WebP",
                    options={"quality": 80},
                    )

    panels = [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.title
    
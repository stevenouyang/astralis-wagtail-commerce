from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

@register_setting
class FeaturesFlag(BaseSiteSetting):
    api_store = models.BooleanField(default=True)
    
    panels = [
        FieldPanel("api_store"),
    ]

@register_setting
class SiteSetting(BaseSiteSetting):
    site_name               = models.CharField(max_length=20, blank=True, null=True)
    site_icon               = models.ImageField(blank=True, upload_to="branding")
    site_logo               = models.ImageField(blank=True, upload_to="branding")
    site_description        = models.CharField(max_length=100, blank=True, null=True)
    site_company            = models.CharField(max_length=100, blank=True, null=True)
    
    site_logo_270x63        = ImageSpecField(
                            source="site_logo",
                            processors=[ResizeToFill(270, 63)],
                            format="PNG",
                            options={"quality": 90},
                        ) 
    
    panels = [
        FieldPanel("site_name"),
        FieldPanel("site_icon"),
        FieldPanel("site_logo"),
        FieldPanel("site_description"),
        FieldPanel("site_company"),
    ]
    
    
@register_setting
class SiteContact(BaseSiteSetting):
    phone_number            = models.CharField(max_length=20, blank=True, null=True)
    phone_number_display    = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_number         = models.CharField(max_length=20, blank=True, null=True)
    whatsapp_link           = models.URLField(blank=True, null=True)
    address                 = models.CharField(max_length=100, blank=True, null=True)
    gmaps_link              = models.URLField(blank=True, null=True)
    email                   = models.EmailField(max_length=50, blank=True, null=True)
    working_hours           = models.CharField(max_length=30, blank=True, null=True)
    
    panels = [
        FieldPanel("phone_number"),
        FieldPanel("phone_number_display"),
        FieldPanel("whatsapp_number"),
        FieldPanel("whatsapp_link"),
        FieldPanel("address"),
        FieldPanel("gmaps_link"),
        FieldPanel("email"),
        FieldPanel("working_hours"),
    ]
    
@register_setting
class GeneralImage(BaseSiteSetting):
    login_banner            = models.ImageField(blank=True, upload_to="generalimages")
    register_banner         = models.ImageField(blank=True, upload_to="generalimages")

    # utility: image processing
    login_banner_495x580    = ImageSpecField(
                            source="login_banner",
                            processors=[ResizeToFill(495, 580)],
                            format="WebP",
                            options={"quality": 80},
                            )
    register_banner_495x580 = ImageSpecField(
                            source="register_banner",
                            processors=[ResizeToFill(495, 580)],
                            format="WebP",
                            options={"quality": 80},
                            )
    
    
    
    panels = [
        FieldPanel("login_banner"),
        FieldPanel("register_banner"),
    ]
    

@register_setting
class SocialMediaLink(BaseSiteSetting):
    instagram_link  = models.URLField(blank=True, null=True)
    twitter_link    = models.URLField(blank=True, null=True)
    youtube_link    = models.URLField(blank=True, null=True)
    facebook_link   = models.URLField(blank=True, null=True)
    github_link     = models.URLField(blank=True, null=True)
    
    panels = [
        FieldPanel("instagram_link"),
        FieldPanel("twitter_link"),
        FieldPanel("youtube_link"),
        FieldPanel("github_link"),
    ]
    

@register_setting
class AppLink(BaseSiteSetting):
    is_showed           = models.BooleanField(default=False)
    playstore_link      = models.URLField(blank=True, null=True)
    appstore_link       = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("is_showed"),
        FieldPanel("playstore_link"),
        FieldPanel("appstore_link"),
    ]
    
class FooterPaymentIcon(ClusterableModel):
    
    # utility: image processing

    pass


class HeaderTop(ClusterableModel):
    
    pass


class HeaderTopText(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    
    panels = [
        FieldPanel("text"),
    ]
    
    def __str__(self):
        return self.text


class HeaderMain(ClusterableModel):
    pass

class FooterSiteHighlight(ClusterableModel):
    pass



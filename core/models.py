from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile/originals/', blank=True, default='/media/default_user.jpg')
    open_for_design = models.BooleanField(default=True)
    phone_number = models.CharField(blank = True, null = True, verbose_name='Contact Number', max_length="300")
    profile_scores =  models.TextField(null=True, blank=True) # {"score":xxx,"loves":xxx,"views":xxx,"aotd":xxx,"aotm":xxx}
    #profile_skills = TaggableManager()
    profile_social =  models.TextField(null=True, blank=True) #{"facebook_url":xxx,"twitter_url":xxx,"twitter_url":xxx,
                      #"youtube_url":xxx,"linkedin_url":xxx,"pinterest_url":xxx}	
    def __unicode__(self):
        return self.user.username


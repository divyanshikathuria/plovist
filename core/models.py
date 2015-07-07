from django.db import models
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True)
    image = models.ImageField(upload_to='profile/originals/') 
    open_for_design = models.BooleanField(default=True)
    phone_number = models.CharField(blank = True, null = True, verbose_name='Contact Number', max_length="300")
    profile_scores =  models.TextField(null=True, blank=True) 
    #profile_skills = TaggableManager()
    



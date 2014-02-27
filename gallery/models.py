from django.db import models

import os


class Image(models.Model):
    
    item_picture  = models.ImageField(upload_to = 'Images/')
    title = models.CharField(max_length=30 , blank=True)       
        
    def __unicode__(self):
        return u'%s' % (os.path.basename(self.item_picture.name) , )
       
    
    def Title(self):
        if not self.title:
            return "Untitled"
        return self.title
    
    Title.short_description = 'Title'
    
    def image_short_name(self):
        return self.__unicode__()
        
    image_short_name.short_description = 'Name'
   
    @property
    def pictureURL(self):
        return self.item_picture.url
    
        
from django.contrib import admin
from models import Image

class ImageAdmin(admin.ModelAdmin):
    
    list_display = ('Title',
                    'image_short_name' , 
                    'pictureURL',

          )
    fields = ('item_picture' , 
                'title',
          )
          
         

admin.site.register(Image, ImageAdmin)

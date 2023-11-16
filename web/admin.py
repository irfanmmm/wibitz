from django.contrib import admin
from web.models import Creators,Subscribe,Futiuersection,Creatvedeo,Partners,Marketting,Solution,Resources,Contact


class CreatorsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'files_image')
 
admin.site.register(Creators,CreatorsAdmin)

admin.site.register(Subscribe)

admin.site.register(Futiuersection)

admin.site.register(Creatvedeo)

admin.site.register(Partners)

admin.site.register(Marketting)

admin.site.register(Solution)

admin.site.register(Resources)

admin.site.register(Contact)








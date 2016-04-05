from django.contrib import admin


# Register your models here.
from ComplaintSystem.models import Users, Complaints, AuthorityWorker, Comments

admin.site.register(Users)
admin.site.register(Complaints)
admin.site.register(AuthorityWorker)
admin.site.register(Comments)
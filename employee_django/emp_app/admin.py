from django.contrib import admin

# Register your models here.
from emp_app.models import ( User,
                        University,
                        Academic,
                        Company,
                        Experience
                             )

admin.site.register(User)
admin.site.register(University)
admin.site.register(Academic)
admin.site.register(Company)
admin.site.register(Experience)
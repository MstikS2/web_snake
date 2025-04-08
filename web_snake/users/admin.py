from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()

# include_parents=False does not work for SnakeUser model cause
# User fields are considered as local, not parent.
# So we need to slice the list manually:
extra_fields = [field.name for field in User._meta.get_fields()][12:-2]

UserAdmin.fieldsets += (('Extra Fields', {'fields': extra_fields}),)

admin.site.register(User, UserAdmin)

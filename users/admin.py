from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', 'email', 'is_superuser']
    search_fields = ['username']

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'position_title')


class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ('username', 'email','first_name', 'last_name')
        add_fieldsets = (
            (None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')}
             ),
        )

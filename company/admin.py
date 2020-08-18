from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import EmployeeChangeForm, EmployeeCreationForm
from .models import Employee, Branch


class SimpleTextFilter(admin.SimpleListFilter):
    # Inherited from
    # https://hakibenita.com/how-to-add-a-text-filter-to-django-admin
    template = 'admin/input_filter.html'

    def lookups(self, request, model_admin):
        # Stub, need to show the filter.
        return (
            (None, None),
            (None, None),
        )

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class FirstNameFilter(SimpleTextFilter):
    title = 'First name'
    parameter_name = 'first_name'

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(first_name__icontains=value)


class LastNameFilter(SimpleTextFilter):
    title = 'Last name'
    parameter_name = 'last_name'

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(last_name__icontains=value)


class EmployeeAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_filter = (FirstNameFilter, LastNameFilter)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'position_title',
                     'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    # Change by taste
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2')}
    #      ),
    # )


class BranchAdmin(admin.ModelAdmin):
    model = Branch


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Branch, BranchAdmin)

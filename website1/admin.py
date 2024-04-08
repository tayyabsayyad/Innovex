from django.contrib import admin
from website1.models import Project
from website1.models import UserModel
from website1.models import Feedback
import csv
from django.http import HttpResponse
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_id', 'proj_title', 'proj_category', 'dept')
    search_fields = ['proj_title', 'proj_id']
    list_filter = (
        # for ordinary fields
        # ('project_dept', DropdownFilter),
        # for choice fields
        ('dept', ChoiceDropdownFilter),
        # for related fields
        # ('project_dept', RelatedDropdownFilter),
    )


class UserModelAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = [field.name for field in UserModel._meta.fields if True]
    search_fields = ['user_email', 'user_name']
    list_filter = (
        # for ordinary fields
        ('user_dept', DropdownFilter),
        # for choice fields
        # ('user_dept', ChoiceDropdownFilter),
        # for related fields
        # ('project_dept', RelatedDropdownFilter),
    )
    actions = ["export_as_csv"]

class FeedbackAdmin(admin.ModelAdmin,ExportCsvMixin):
    list_display = [field.name for field in Feedback._meta.fields if True]
    list_filter = (
        # for ordinary fields
        # ('project_dept', DropdownFilter),
        # for choice fields
        ('project_dept', ChoiceDropdownFilter),
        # for related fields
        # ('project_dept', RelatedDropdownFilter),
    )
    actions = ["export_as_csv"]


admin.site.register(UserModel, UserModelAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Feedback, FeedbackAdmin)


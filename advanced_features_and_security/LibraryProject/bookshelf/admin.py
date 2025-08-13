from django.contrib import admin
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from relationship_app.models import Book

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)



class Command(BaseCommand):
    help = 'Set up default groups and permissions'

    def handle(self, *args, **kwargs):
        permissions = Permission.objects.filter(content_type__app_label='relationship_app')

        # Create groups
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        editors_perms = permissions.filter(codename__in=['can_create', 'can_edit'])
        viewers_perms = permissions.filter(codename__in=['can_view'])
        admins_perms = permissions.all()

        editors.permissions.set(editors_perms)
        viewers.permissions.set(viewers_perms)
        admins.permissions.set(admins_perms)

        self.stdout.write(self.style.SUCCESS('Groups and permissions set up successfully.'))

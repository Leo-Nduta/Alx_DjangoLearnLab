from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

#from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate

class RelationshipAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "relationship_app"

    def ready(self):
        post_migrate.connect(create_groups_and_permissions, sender=self)


def create_groups_and_permissions(sender, **kwargs):
    from django.contrib.contenttypes.models import ContentType
    from .models import UserProfile

    # Get content type for UserProfile
    content_type = ContentType.objects.get_for_model(UserProfile)

    # Permissions
    perms = ['can_view', 'can_create', 'can_edit', 'can_delete']
    for perm in perms:
        Permission.objects.get_or_create(codename=perm, name=f"Can {perm.replace('_', ' ')}", content_type=content_type)

    # Groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    # Assign permissions
    editors.permissions.set(Permission.objects.filter(codename__in=['can_create', 'can_edit']))
    viewers.permissions.set(Permission.objects.filter(codename__in=['can_view']))
    admins.permissions.set(Permission.objects.filter(codename__in=perms))

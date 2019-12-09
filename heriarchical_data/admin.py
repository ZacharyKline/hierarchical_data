from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from heriarchical_data.models import File

admin.site.register(
    File,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

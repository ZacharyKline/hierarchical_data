from mptt.admin import DraggableMPTTAdmin
from heriarchical_data.models import File
from django.shortcuts import render


class FileView(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        html = 'index.html'
        item = File.objects.all()
        ancestors = item.get_ancestors(ascending=False, include_self=False)
        children = item.get_children()
        return render(request, html, {
            'item': item,
            'ancestors': ancestors,
            'children': children
        })


def homeview(request):
    html = 'index.html'
    data = File.objects.all()
    return render(request, html, {'data': data})

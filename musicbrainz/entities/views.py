from django.http import HttpResponse
from django.views.generic.list import ListView

class IndexView(ListView):
    template_name = 'entities/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, **kwargs):
        return []

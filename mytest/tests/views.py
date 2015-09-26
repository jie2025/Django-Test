from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from .models import Key


def index(request):
    latest_key_list = Key.objects.order_by('-pub_date')[:5]
    template = loader.get_template('tests/index.html')
    context = RequestContext(request, {
        'latest_key_list': latest_key_list,
    })
    return HttpResponse(template.render(context))

def detail(request, key_id):
    key = get_object_or_404(Key, pk=key_id)
    return render(request, 'tests/detail.html', {'key': key})

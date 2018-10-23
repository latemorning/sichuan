from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse
from memo.models import StageComptTime
import json

class IndexView(generic.ListView):
    template_name = 'memo/index.html'
    context_object_name = 'stage_list'

    def get_queryset(self):
        return StageComptTime.objects.all().order_by('-stage_no')[:100]


class DetailView(generic.DetailView):
    model = StageComptTime
    template_name = 'memo/detail.html'


def update(request, stage_id):

    selected_stage = get_object_or_404(StageComptTime, pk=stage_id)

    selected_stage.compt_time = request.POST.get('compt_time')
    selected_stage.save()

    message = "성공"
    isSuccess = True

    context = {'message': message,
               'isSuccess': isSuccess}

    return HttpResponse(json.dumps(context), content_type="application/json")

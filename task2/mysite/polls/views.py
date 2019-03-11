from .models import Question as Q
from .models import QuestionForm as QF

from django.shortcuts import render as rd
from django.utils import timezone as timer


def get_question(request):
    question_list = Q.objects.order_by('-pub_date')
    if request.method == 'POST':
        form = QF(request.POST)
        if form.is_valid():
            currQ = Q(question_text=request.POST['question_text'], pub_date=timer.now())
            currQ.save()
    else:
        form = QF()

    return rd(request, 'polls/index.html', {'form': form, 'question_list': question_list})

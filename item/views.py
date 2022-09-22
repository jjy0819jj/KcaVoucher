from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.order_by('-create_date')
    context = {
        'item_list': item_list
    }
    return render(request, 'item/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Item, pk=question_id)
    context = {'question': question}
    return render(request, 'main/question_detail.html', context)


def create_item(request, question_id):
    return redirect('main:detail')
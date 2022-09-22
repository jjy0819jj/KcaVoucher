from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user_list = User.objects.order_by('-created_at')
    context = {'user_list': user_list}
    return render(request, 'user/index.html', context)


def create(request):
    """
    user 등록
    """
    form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})
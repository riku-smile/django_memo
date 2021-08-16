from memo.app.forms import MemoForm
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import MemoForm
from .models import Memo

# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, 'app/detail.html', {'memo': memo})


def new_memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MemoForm
    return render(request, 'app/new_memo.html', {'form': form})


@require_POST
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('app:index')


def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'app/edit_memo.html', {'form': form, 'memo': memo})

from django.forms import ModelForm, fields
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'text']

# formで使える便利な機能をインポート
from django import forms
from .models import Todo

# 検索する用のクラスを作成
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'detail', 'started_at', 'ended_at')


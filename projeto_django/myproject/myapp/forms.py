from django.forms import ModelForm
from .models import Reporter, Article


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['name']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

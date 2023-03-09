from django import forms
from django.forms import widgets
from webapp.models import Tasks, Project
from webapp.validators import CustomTitleValidator, CustomDescriptionValidator


class TasksForm(forms.ModelForm):
    summary = forms.CharField(validators=(CustomTitleValidator(),))
    description = forms.CharField(widget=widgets.Textarea(), validators=(CustomDescriptionValidator(),))

    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Кратоке описание',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип',
        }


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=widgets.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), label='Дата начала')
    expiration_date = forms.DateField(widget=widgets.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), label='Дата окончания')
    name = forms.CharField(validators=(CustomTitleValidator(),))
    description = forms.CharField(widget=widgets.Textarea(), validators=(CustomDescriptionValidator(),))
    class Meta:
        model = Project
        fields = ('start_date', 'expiration_date', 'name', 'description')
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'start_date': 'Дата начала',
            'expiration_date': 'Дата окончания'
        }


class SearchView(forms.Form):
    search = forms.CharField(max_length=90, required=False, label='Найти')

from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields ="__all__"
        # fields = ['title', 'completed']
    
    def clean_title(self):
        title=self.cleaned_data.get('title')

        if 'x' in title:
            raise forms.ValidationError('Title should not  contain x')
        return title










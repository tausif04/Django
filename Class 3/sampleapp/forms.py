from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    # title=forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder':'Enter the title',
    #             'class':'form-control'                    
    #         }
    #     ),
    # )
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label='New Title'
        self.fields['title'].widget.attrs.update({'placeholder':'Enter the title'})

        self.fields['completed'].label='New Completed'
        self.fields['completed'].widget.attrs.update({'class':'form-check-input'})
    class Meta:
        model = Task
        fields ="__all__"
        # fields = ['title', 'completed']
    
    def clean_title(self):
        title=self.cleaned_data.get('title')

        if 'x' in title:
            raise forms.ValidationError('Title should not  contain x')
        return title










from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(label='write the software description',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
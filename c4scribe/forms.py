from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(label='Input Text',
                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
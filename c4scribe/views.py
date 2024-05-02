from django.shortcuts import render
from .models import Generator
from .forms import PromptForm
from .util import md2html

def generate_text(request):
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            text_input = form.cleaned_data['prompt']
            generator = Generator(text_input)
            html_file = md2html( generator.generate())
            return render(request, html_file)
    else:
        form = PromptForm()
    return render(request, 'index.html', {'form': form})
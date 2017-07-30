from django import forms
from .models import Standard

class PostForm(forms.ModelForm):
	class Meta:
		model = Standard
		fields = ('title', 'text',)
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'focus-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'focus-input', "placeholder": "email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'focus-input'}))

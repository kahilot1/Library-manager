
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class add_book(forms.Form):
    title = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=100)
    id = forms.CharField(max_length=100)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            'title',
            'summary',
            'author',
            'id',
            Submit('submit', 'Submit', css_class='btn-success')
        )
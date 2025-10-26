from django import forms
from .models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

"""class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
"""


# 🎉 Django 5.0 allows options to be defined as a mapping. 🎉
"""
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday"
}


class BootstrapForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(max_length=50)
    appointment_date = forms.ChoiceField(
        choices=days,
        widget=forms.RadioSelect(),
        help_text="Select which day you would like your appointment. We're only open Monday-Wednesday."
    )
    attachment = forms.FileField(
        required=False,
        help_text="Please provide any files you wish us to review prior to your appointment.",
    )
"""

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Task', css_class='btn btn-primary'))
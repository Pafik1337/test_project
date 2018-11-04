from django import forms
from .models import *

class SubscribersForm(forms.ModelForm):
    class meta:
        # models = Subscriber
        exclude = [""]
    
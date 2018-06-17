from django.forms import ModelForm
from demo.models import DemoModel


class DemoForm(ModelForm):
    class Meta:
        model = DemoModel
        fields = '__all__'

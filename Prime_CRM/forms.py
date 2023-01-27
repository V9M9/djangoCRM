from django.forms import ModelForm, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Client, Address, Contract
from betterforms.multiform import MultiModelForm


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save client'))


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['address']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save address'))


class MultiForm(MultiModelForm):
    form_classes = {
        'client': ClientForm,
        'address': AddressForm,
    }
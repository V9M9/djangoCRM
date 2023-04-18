from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
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
        self.fields['name'].required = False
        self.fields['surname'].required = False
        self.fields['patronymic'].required = False


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ['address']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save address'))


class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save contract'))
        self.fields['status'].required = False
        self.fields['description'].required = False

        Field('Client_id', type="hidden")



class MultiForm(MultiModelForm):
    form_classes = {
        'client': ClientForm,
        'address': AddressForm,
    }

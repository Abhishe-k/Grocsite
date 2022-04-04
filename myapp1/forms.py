from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'qty_ordered']
        widgets = {
            'client': forms.RadioSelect,
        }

        labels = {
            'qty_ordered': 'Quantity',
            'client': 'Client Name'
        }


class InterestForm(forms.Form):
    # choices = (('Yes', 1), ('No', 0))
    choices = ((1, 'Yes'), (0, 'No'))
    interested = forms.ChoiceField(choices=choices, label='Are you Interested?', help_text='', widget=forms.RadioSelect)
    quantity = forms.IntegerField(min_value=1)
    comments = forms.CharField(label='Additional Comments', widget=forms.Textarea())



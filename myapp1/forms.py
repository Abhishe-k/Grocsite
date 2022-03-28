from django import forms
from myapp1.models import OrderItem


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        widgets = {
            'client': forms.RadioSelect,
        }

        labels = {
            'item_ordered': 'Quantity',
            'client': 'Client Name'
        }


class InterestForm(forms.Form):
    choices = (('Yes', 1), ('No', 0))
    interested = forms.ChoiceField(choices=choices, label='', help_text='', widget=forms.RadioSelect)
    quantity = forms.IntegerField(default=1, min_value=1)
    comments = forms.Textarea(label='Additional Comments')

from django import forms
from myapp1.models import OrderItem

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'client', 'items_ordered']
        widgets = {
            'client': forms.RadioSelect(attrs={'class': 'Users'})
        }
        labels = {
            'items_ordered': 'Quantity',
            'client': 'Client Name'
        }

class InterestForm(forms.Form):
    CHOICE = [('Yes', 1), ('No', 0)]
    interested = forms.RadioSelect(attrs=CHOICE)
    quantity = forms.IntegerField(default=1,min_value=1)
    comments = forms.Textarea(label='Additional Comments', required=false)



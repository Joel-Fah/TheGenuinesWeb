from django import forms
from .models import *
# Create your views here.

# Possible prodcut choices
CHOICES = (
    ('Advanced Level',
        (
            ('Computer Science 1 & 2 - Advanced Level', 'Computer Science 1 & 2 - Advanced Level'),
            ('Computer Science 3 - Advanced Level', 'Computer Science 3 - Advanced Level'),
            ('Both Advanced Level Pamphlets', 'Both Advanced Level Pamphlets'),
        )
    ),
    ('Ordinary Level',
        (
            ('Computer Science 1 & 2 - Ordinary Level', 'Computer Science 1 & 2 - Ordinary Level'),
        ('Computer Science 3 - Ordinary Level', 'Computer Science 3 - Ordinary Level'),
        ('Both Ordinary Level Pamphlets', 'Both Advanced Level Pamphlets'),
        )
    ),
)

# Creation of form using Form class method
class OrderForm(forms.Form):
    Name = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'name',
                    'id': 'name',
                    'placeholder': 'Your Name...'
                }
            )
        )
    
    
    Phone = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'name': 'organization',
                'id': 'organization',
                'placeholder': 'Your phone number...'
            }
        )
    )
    
    
    Email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Your Email address...'
            }
        )
    )
    
    
    AdditionalInfo = forms.CharField(
        required=False,
        max_length=3000,
        widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'id': 'message',
                    'rows': '7',
                    'cols': '30',
                    'placeholder': 'Provide some extra information if any e.g. Your address (precisely), observations, Do you need delivery?, etc'
                }
            )
    )
    
    
    Product = forms.CharField(
        required=True,
        label= 'Product',
        widget=forms.Select(
                choices= CHOICES,
                attrs={
                    'class': 'custom-select',
                    'id': 'budget',
                    'name': 'budget'
                }
            )
        )
    
    
    Amount = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'name': 'date',
                'id': 'date',
                'placeholder': 'Number of copies...'
            }
        )
    )


# Creation of form using Model Form method
class MyOrderForm(forms.ModelForm):

   #Metadata
   class Meta:
       model = MyOrderInfo
       fields = [
           'Name',
           'Phone',
           'Email',
           'AdditionalInfo',
           'Product',
           'Amount',
       ]
    
  
    # Definition of widgets
       widgets = {
           'Name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'name',
                    'id': 'name',
                    'placeholder': 'Your Name...'
                }
            ),
           
           'Phone':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'name': 'organization',
                    'id': 'organization',
                    'placeholder': 'Your phone number...'
                }
            ),
           
           'Email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'name': 'email',
                    'id': 'email',
                    'placeholder': 'Your Email address...'
                }
            ),
           
           'AdditionalInfo': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'id': 'message',
                    'rows': '7',
                    'cols': '30',
                    'placeholder': 'Provide some extra information if any e.g. Your address (precisely), observations, Do you need delivery?, etc'
                }
            ),
           
           'Product': forms.Select(
                choices= CHOICES,
                attrs={
                    'class': 'custom-select',
                    'id': 'budget',
                    'name': 'budget'
                }
            ),
           
           'Amount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'name': 'date',
                    'id': 'date',
                    'placeholder': 'Number of copies...'
                }
            )
       }
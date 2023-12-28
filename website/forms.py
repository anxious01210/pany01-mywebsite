from django import forms
# from phonenumber_field.modelfields import PhoneNumberField

class ContactForm(forms.Form):
    """docstring for ContactForm."""
    name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(max_length=100,widget= forms.EmailInput(attrs={'placeholder':'E-mail'}))
    # email = forms.EmailField(label='E-mail')
    # phone_number = PhoneNumberField()
    # phone_number = models.CharField(max_length=15, widget=forms.Textarea(attrs={'placeholder':'Enter your Phone Number'}), label="Your Phone Number")
    phone_number = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Phone Number'}))
    city = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'City'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your message'}), label="Your comment")

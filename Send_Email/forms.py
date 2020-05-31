from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=10000,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': 'Type Your Subject Here'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 50, 'rows': 30, 'class': 'form-control', 'placeholder': 'Type Your Message Here'}))

    from_mail = forms.EmailField(max_length=300,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'From @Email'}))
    to_mail = forms.EmailField(max_length=300,widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : 'To @Email'}))


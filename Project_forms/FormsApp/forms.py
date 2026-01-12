from django import forms

class SupportTicketForm(forms.Form):

    CATEGORY_CHOICES = [
        ('login', 'Login problem'),
        ('payment', 'Payment'),
        ('bug', 'Bug report'),
        ('other', 'Other'),
    ]

    name = forms.CharField(label="Full name", max_length=100)
    email = forms.EmailField(label="Email")
    text = forms.CharField(
        label="Message",
        widget=forms.Textarea,
        min_length=20
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        required=False
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        words = name.strip().split()

        if len(words) < 2:
            raise forms.ValidationError(
                "Please enter at least first and last name."
            )

        return name

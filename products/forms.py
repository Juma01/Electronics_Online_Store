from django import forms


class ProductCreateForm(forms.Form):
    brand = forms.CharField(min_length=2, max_length=255)
    phone_model = forms.CharField(min_length=1, max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    memory = forms.CharField(min_length=2, max_length=30)
    color = forms.CharField(min_length=2, max_length=50)
    price = forms.FloatField()
    rate = forms.FloatField(min_value=1, max_value=5)
    commentable = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'checked': True}),
        required=False)


class CommentCreateForm(forms.Form):
    text = forms.CharField(min_length=2)
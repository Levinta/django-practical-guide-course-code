from django import forms

from .models import Review


# class ReviewForm(forms.Form):

#     name = forms.CharField(label='Your name', max_length=100, required=True,
#                            error_messages={'required': 'Your name must not be empty',
#                                            'max_length': 'Please enter a shorter name'})

#     review_text = forms.CharField(
#         label='Your review', widget=forms.Textarea, max_length=2000, required=True,
#         error_messages={'required': 'Your review must not be empty',
#                         'max_length': 'Please enter a shorter review'})
#     rating = forms.IntegerField(min_value=1, max_value=5, required=True)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        widgets = {
            'review_text': forms.Textarea(attrs={'cols': 40, 'rows': 15})
        }
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your review',
            'rating': 'Your rating'
        }

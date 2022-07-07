from django import forms
from .models import Course


class CourseModelForm(forms.ModelForm):
    banned_words = [
        "penis",
        "pussy"
    ]

    class Meta:
        model = Course
        fields = [
            'title',
            'content',
            'active',
        ]

    def clean_title(self):
        title = self.cleaned_data['title']
        for banned_word in self.banned_words:
            if banned_word in title.lower():
                raise forms.ValidationError("Bad word")
        return title

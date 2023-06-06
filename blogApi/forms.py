from django import forms
from .models import Post, Category, Profile, Comments
from django.contrib.auth.models import User


cats = [(object.name, object.name) for object in Category.objects.all()]


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body', 'category', 'snippet', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cats, attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostFormSecond(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'title_tag','category', 'body', 'snippet', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=cats, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'portfolio_url', 'linkedin_url']

        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'portfolio_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),

        }


class AddCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"rows":5, "cols":20}))

    class Meta:
        model = Comments
        fields = ['comment']

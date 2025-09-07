from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Post
from .models import Comment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class PostForm(forms.ModelForm):
    """Form used for creating/updating posts. Author is set in the view."""
    tags_field = forms.CharField(
        required=False,
        help_text="Add tags separated by commas (e.g. django,python,testing)"
    )

    class Meta:
        model = Post
        fields = ["title", "content"]  # author & published_date handled automatically

    def __init__(self, *args, **kwargs):
        # If editing an existing instance, pre-fill tags_field
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['tags_field'].initial = ", ".join([t.name for t in instance.tags.all()])

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title
    
    def clean_tags_field(self):
        raw = self.cleaned_data.get('tags_field', '')
        # sanity: split and strip, ignore empty
        tags = [t.strip() for t in raw.split(',') if t.strip()]
        return tags

    def save(self, commit=True):
        # Save Post first, then assign tags
        post = super().save(commit=commit)
        tags_list = self.cleaned_data.get('tags_field', [])
        # convert names to Tag instances
        tag_objs = []
        for tag_name in tags_list:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
            tag_objs.append(tag_obj)
        # set many-to-many relation
        post.tags.set(tag_objs)
        if commit:
            post.save()
        return post



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write a comment…"})
        }



    

    
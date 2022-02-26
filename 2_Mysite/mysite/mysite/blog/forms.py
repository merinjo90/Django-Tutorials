from django.forms import ModelForm
from .models import Post

# Create the form class.
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['head', 'description']

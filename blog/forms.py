from django import forms 
from .models import Post,Comment 
 
class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = ["title", "body", "image"] 
        widgets = { 
            'title': forms.TextInput(attrs={ 
                'class': 'input-field', 
                'placeholder': 'عنوان پست' 
            }), 
            'body': forms.Textarea(attrs={ 
                'class': 'input-field', 
                'placeholder': 'متن پست' 
            }), 
        } 
 
class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = ['name', 'body'] 
 
        widgets = { 
            'name': forms.TextInput(attrs={ 
                'placeholder': 'نام شما', 
                'style': 'width:100%; padding:10px; border-radius:10px; border:1px solid #ccc; margin-bottom:10px;' 
            }), 
            'body': forms.Textarea(attrs={ 
                'placeholder': 'متن نظر...', 
                'style': 'width:100%; padding:10px; border-radius:10px; border:1px solid #ccc; height:120px;' 
            }), 
        } 
 
from django import forms
from .models import Task, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class TaskForm(forms.ModelForm):
    new_category = forms.CharField(
        max_length=100,
        required=False,
        label='Создать новую категорию'
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'is_completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'priority': forms.Select(choices=Task.PRIORITY_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].required = False

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(
                name=new_category_name
            )
            instance.category = category
        
        if commit:
            instance.save()
        
        return instance
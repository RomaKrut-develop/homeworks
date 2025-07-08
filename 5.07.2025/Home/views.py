from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from django.utils import timezone
from .models import Task, Category
from .forms import TaskForm, CategoryForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Фильтрация по категории
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Фильтрация по статусу выполнения
        is_completed = self.request.GET.get('is_completed')
        if is_completed == '1':
            queryset = queryset.filter(is_completed=True)
        elif is_completed == '0':
            queryset = queryset.filter(is_completed=False)
        
        # Поиск по названию
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        
        # Сортировка
        sort = self.request.GET.get('sort')
        if sort == 'priority':
            queryset = queryset.order_by('-priority', 'created_at')
        elif sort == 'created_at_asc':
            queryset = queryset.order_by('created_at')
        else:
            queryset = queryset.order_by('-created_at')
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = self.request.GET.get('category')
        context['search_query'] = self.request.GET.get('search', '')
        context['sort_option'] = self.request.GET.get('sort', '-created_at')
        context['is_completed_filter'] = self.request.GET.get('is_completed')
        return context

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def toggle_task_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')
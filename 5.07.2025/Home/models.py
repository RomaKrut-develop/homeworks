from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Низкий'),
        (2, 'Средний'),
        (3, 'Высокий'),
    ]

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата выполнения')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнено')
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        verbose_name='Категория'
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=2,
        verbose_name='Приоритет',
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-priority', 'created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_completed and not self.completed_at:
            self.completed_at = timezone.now()
        elif not self.is_completed and self.completed_at:
            self.completed_at = None
        super().save(*args, **kwargs)
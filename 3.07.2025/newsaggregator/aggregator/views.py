from django.shortcuts import render
from .models import NewsItem, NewsSource
import requests
from bs4 import BeautifulSoup
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    news_items = NewsItem.objects.all().order_by('-published_at')
    return render(request, 'aggregator/index.html', {'news_items': news_items})

def update_news(request):
    # Предварительно добавьте источники через админку
    sources = NewsSource.objects.filter(active=True)
    
    for source in sources:
        try:
            response = requests.get(source.url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Пример для BBC News (нужно адаптировать под конкретный сайт)
            if 'bbc.com' in source.url:
                articles = soup.find_all('h3', class_='gs-c-promo-heading__title')
                for article in articles[:10]:  # Берем первые 10 статей
                    title = article.get_text().strip()
                    link = article.find_parent('a')['href']
                    if not link.startswith('http'):
                        link = 'https://www.bbc.com' + link
                    
                    if not NewsItem.objects.filter(url=link).exists():
                        NewsItem.objects.create(
                            title=title,
                            url=link,
                            source=source
                        )
            
            # Пример для другого сайта (можно добавить дополнительные условия)
            
        except Exception as e:
            print(f"Error parsing {source.url}: {e}")
            continue
    
    return HttpResponseRedirect(reverse('index'))
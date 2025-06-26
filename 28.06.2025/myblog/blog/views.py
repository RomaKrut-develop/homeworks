from django.shortcuts import render

def index(request):
    posts = [
        {
            'id': 1,
            'title': 'Microsoft contiune to support Windows XP in 2026',
            'text': 'In this post we are going to look about Satia Nadella tell journalist about...',
            'pub_date': '2018-05-15',
            'short_text': 'In this post we are...'
        },
        {
            'id': 2,
            'title': 'Apple announce Iphone 19!',
            'text': 'Today Steve Jobs announce new iphone. We can explore apple pressenation to...',
            'pub_date': '2023-05-20',
            'short_text': 'Steve and Apple...'
        },
        {
            'id': 3,
            'title': 'Linux are going to have big update',
            'text': 'Linus Torvalds about to rebuild core api for more safety...',
            'pub_date': '2024-05-25',
            'short_text': 'Linux'
        },
    ]
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    posts = [
        {
            'id': 1,
            'title': 'Microsoft contiune to support Windows XP in 2026',
            'text': 'In this post we are going to look about Satia Nadella tell journalist about...',
            'pub_date': '2018-05-15',
            'short_text': 'In this post we are...'
        },
        {
            'id': 2,
            'title': 'Apple announce Iphone 19!',
            'text': 'Today Steve Jobs announce new iphone. We can explore apple pressenation to...',
            'pub_date': '2023-05-20',
            'short_text': 'Steve and Apple...'
        },
        {
            'id': 3,
            'title': 'Linux are going to have big update',
            'text': 'Linus Torvalds about to rebuild core api for more safety...',
            'pub_date': '2023-05-25',
            'short_text': 'Linux'
        },
    ]
    
    post = next((p for p in posts if p['id'] == post_id), None)
    return render(request, 'blog/post_detail.html', {'post': post})
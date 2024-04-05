from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import ForumTopic, ForumComment, Like
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# def index(request):
#     return render(request, 'index.html')

def welcome(request):
    return render(request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Form submitted")  
            return redirect('login')  
        else:
            print("Form is not valid")  
            print(form.errors)
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm(request, initial={'username': ''})  

    return render(request, 'login.html', {'form': form})


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        topics = ForumTopic.objects.all()
        context = {'username': username, 'topics': topics}
        return render(request, 'index.html', context)
    else:
        return redirect('login')


@login_required
def create_topic(request):
    if request.method == 'POST':
        title = request.POST.get('topicTitle')  # Retrieve 'topicTitle' from POST data
        description = request.POST.get('topicDescription')  # Retrieve 'topicDescription' from POST data
        author = request.user
        topic = ForumTopic.objects.create(title=title, description=description, author=author)
        return redirect('index')  # Redirect to forum index or topic detail page
    return render(request, 'create_topic.html')


@login_required
def add_comment(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(ForumTopic, id=topic_id)
        comment_text = request.POST.get('commentText')
        author = request.user
    
        # Print statement to debug
        print(f'Received comment_text: {comment_text}')

        if not comment_text:
            return JsonResponse({'success': False, 'message': 'Comment text is required.'}, status=400)

        try:
            comment = ForumComment.objects.create(topic=topic, comment_text=comment_text, author=author)
            return JsonResponse({'success': True, 'message': 'Comment added successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


def get_comments(request, topic_id):
    comments = ForumComment.objects.filter(topic_id=topic_id)
    comments_data = [{'content': comment.comment_text} for comment in comments]
    return JsonResponse({'success': True, 'comments': comments_data})

@login_required
def like_topic(request, topic_id):
    if request.method == 'POST':
        topic = ForumTopic.objects.get(id=topic_id)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, topic=topic)
        if not created:
            like.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def like_comment(request, comment_id):
    if request.method == 'POST':
        comment = ForumComment.objects.get(id=comment_id)
        user = request.user
        like, created = Like.objects.get_or_create(user=user, comment=comment)
        if not created:
            like.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def full_list(request):
	pageslist = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/standard_list.html', {'pages': pages})

def standard_detail(request, pk):
    page = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/standard_detail.html', {'page': page})

def standard_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			page.author = request.user
			page.published_date = timezone.now()
			page.save()
			return redirect('standard_detail', pk=page.pk)
	else:
		form = PostForm()
	return render(request, 'blog/standard_edit.html', {'form': form})
	
def standard_edit(request, pk):
    page = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.published_date = timezone.now()
            page.save()
            return redirect('standard_detail', pk=page.pk)
    else:
        form = PostForm(instance=page)
    return render(request, 'blog/standard_edit.html', {'form': form})	
	

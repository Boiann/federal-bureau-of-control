from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Event
from .forms import CommentForm


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by('created_on')
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if event.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        return render(
            request,
            "event-detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if event.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = event
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "event-detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "liked": liked,
                "disliked": disliked,
            },
        )


class EventApprove(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))


class EventDisprove(View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.dislikes.filter(id=request.user.id).exists():
            event.dislikes.remove(request.user)
        else:
            event.dislikes.add(request.user)

        return HttpResponseRedirect(reverse('event_detail', args=[slug]))

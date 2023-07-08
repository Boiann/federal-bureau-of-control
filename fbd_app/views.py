from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Event
from .forms import CommentForm, EventForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


def splash(request):
    # raise Exception('This is a test error')      # ==> Error 500 test.
    return render(request, "index.html")


def logout(request):
    return render(request, 'logout.html')


def home(request):
    return render(request, "home.html")


def handler404(request, exception):
    context = {}
    response = render(request, "404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "500.html", context=context)
    response.status_code = 500
    return response


class EventList(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'reports.html'
    paginate_by = 6


class EventDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.all()
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
            comment.approved = True
            comment_form = CommentForm()
            comment.save()
            messages.success(request, 'Your comment has been submitted.')
            return HttpResponseRedirect(request.path_info)

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


class AddEvent(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'add-event.html'
    success_url = reverse_lazy('home')
    form_class = EventForm
    success_message = 'Report submitted for approval by the Director.'

    def form_valid(self, form):
        if self.request.POST.get('status'):
            form.instance.status = int(self.request.POST.get('status'))
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateEvent(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'update-event.html'
    success_url = reverse_lazy('home')
    success_message = 'Report successfully updated'


class DeleteEvent(LoginRequiredMixin, generic.DeleteView):
    model = Event
    form_class = EventForm
    template_name = 'delete-event.html'
    success_url = reverse_lazy('home')
    success_message = 'Report successfully deleted'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message, 'danger')

        return super(DeleteEvent, self).delete(request, *args, **kwargs)


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


class UserEventList(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'user-events.html'

    def get_queryset(self):
        return Event.objects.filter(author=self.request.user)


class EventsByOwner(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'user-events.html'

    def get_queryset(self):
        return Event.objects.filter(author__id=self.kwargs['owner_id']).order_by('-created_on')

from django.urls import reverse_lazy
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View

from .forms import TagForm, TeamForm, NewsLinkForm
from .models import Team, Tag
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

class TeamCreate(ObjectCreateMixin, View):
    form_class = TeamForm
    template_name = 'organizer/team_form.html'

class TeamUpdate(ObjectUpdateMixin, View):
    form_class = TeamForm
    model = Team
    template_name = 'organizer/team_form_update.html'


def team_detail(request, slug):
    startup = get_object_or_404(
        Team, slug__iexact=slug)
    return render(
        request,
        'organizer/team_detail.html',
        {'team': team})

class TeamDelete(ObjectDeleteMixin, View):
    model = Team
    success_url = reverse_lazy(
        'organizer_team_list'
    )
    template_name = 'organizer/team_confirm_delete.html'


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

class NewsLinkDelete(View):

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        return render(
            request,
            'organizer/'
            'newslink_confirm_delete.html',
            {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        team = newslink.team
        newslink.delete()
        return redirect(team)

class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form_update.html'

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk
        )
        bound_form = self.form_class(
            request.POST, instance=newslink
        )
        if bound_form.is_valid():
            new_newslink = bouund_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': form,
                'newslink': newslink,
            }
            return render(
                request,
                self.template_name,
                context
            )

def team_list(request):
    return render(
        request,
        'organizer/team_list.html',
        {'team_list': Team.objects.all()})


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = 'organizer/tag_form_update.html'

def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list'
    )
    template_name = 'organizer/tag_confirm_delete.html'




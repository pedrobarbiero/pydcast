from typing import Any

from django.shortcuts import render
from django.views.generic import ListView

from podcasts.models import Episode


class HomePageView(ListView):
    template_name = "homepage.html"
    model = Episode

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs) 
        context["episodes"] = Episode.objects.order_by("-publication_date")[:10]
        return context

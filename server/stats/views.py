from django.views.generic import TemplateView

from .stats import get_toilet_stats


class ToiletStatsView(TemplateView):
    template_name = 'toilet_stats.html'

    def get_context_data(self, **kwargs):
        context = super(ToiletStatsView, self).get_context_data(**kwargs)
        days = self.request.GET.get('days')
        context['stats'] = get_toilet_stats(days)
        context['days'] = days
        return context

from django.shortcuts import render
from .models import Theme
# Create your views here.

def index(request):
    return render(request, 'index.html')

def popular_themes(request):
    """
    There should be a route get_popular_themes that returns the list of themes (id and name),
    ordered by their success on the channel. For each theme, its score will be given by the
    sum of the scores of all videos that contain that theme.
    """
    themes = Theme.objects.all()
    for theme in themes:
        theme.update_sum_score()

    # need to order by sum_score descending
    order_by_sum_score = Theme.objects.order_by('-sum_score')

    return render(request, 'popular_themes.html', {'themes': order_by_sum_score})

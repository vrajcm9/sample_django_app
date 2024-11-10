from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from nvd3 import lineChart


@login_required
def chart_view(request):
    # Sample chart data
    xdata = [0, 1, 2, 3, 4, 5]
    ydata = [3, 12, 5, 18, 45, 8]
    chart = lineChart(name="lineChart", x_is_date=False, x_axis_format="AM_PM")
    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()
    return render(request, "../templates/charts/chart.html", {"chart": chart})

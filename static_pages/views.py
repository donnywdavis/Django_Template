from django.shortcuts import render


def index(request):
    """
    This is the route for the home page of the site.

    :param request: Data passed in from the browser
    :return: Render the template to the browser.
    """

    return render(request, 'static_pages/index.html', {})

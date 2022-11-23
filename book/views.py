from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from book.models import Publisher


def index(request):
	# queryset = Publisher.objects.filter(name="Voonyx").filter(email="msaice7@hexun.com")
	# queryset = Publisher.objects.filter(website__startswith="https")
	# queryset = Publisher.objects.filter(id__in=(1, 2, 5))
	queryset = Publisher.objects.filter(id__range=(5, 8))
	return render(request, "book/index.html", context={"publishers": list(queryset)})
	# return HttpResponse("Hello World")


def publisher_details(request, pk):
	publisher = get_object_or_404(Publisher, pk=pk)
	return render(request, "book/publisher-detail.html", context={"publisher": publisher})


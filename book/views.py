from django.db.models import Count, Avg, Q, F, ExpressionWrapper, DecimalField
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from book.models import Publisher, Book


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


def book_list(request):
	# queryset = Book.objects.all()
	# queryset = Book.objects.order_by("-title", "price")
	# queryset = Book.objects.order_by("-title", "price")
	# queryset = Book.objects.select_related("publisher")[5:10]
	# queryset = Book.objects.select_related("publisher")
	queryset = Book.objects \
		.select_related('publisher') \
		.filter(title=F('slug')) \
		.annotate(discounted_price=ExpressionWrapper(F("price") * 0.8, output_field=DecimalField()))
		# .filter(Q(title__icontains="the") | Q(price__isnull=True))
		# .filter(price__gt=100)
	# books = list(queryset)
	result = queryset.aggregate(count=Count("id"), average=Avg("price"))
	# book = queryset[0]
	return render(request, "book/book-list.html", context={"books": list(queryset), "result":  result})
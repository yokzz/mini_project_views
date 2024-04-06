from django.shortcuts import render, redirect, HttpResponse
from views.models import *

def get_review_list(request):
    reviews = Review.objects.all()
    context = {
                'reviews': reviews,
    }
    return render(request, 'views/reviews_list.html', context)

def get_review_form(request):
    if request.method == "GET":
        return render(request, "views/review_form.html")
    else:
        product = request.POST.get("product")
        author = request.POST.get("author")
        text = request.POST.get("text")
        rating = request.POST.get("rating")
        
        try:
            product = Review.objects.get(product=product)
        except ValueError:
            return HttpResponse("Wrong product name", status=404)
        except Product.DoesNotExist:
            return HttpResponse("Product doesn't exist", status=404)
        review = Review.objects.create(
            product = product,
            author = author,
            text = text,
            rating = rating
        )
        return redirect("review-form", pk=review.id)
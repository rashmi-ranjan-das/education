from django.shortcuts import render, redirect
from .models import Books, Python, Cplusplus, MLAI, Reviews, Arduino, Quotes, WebDev
from django.core.mail import send_mail
import random
from django.contrib import messages
from datetime import datetime
# Create your views here.
def home(request):
    total = len(Quotes.objects.all())
    r_id = random.randint(0,total-1) + 1
    quote = Quotes.objects.get(pk=r_id)
    all_review = Reviews.objects.all()
    rating = 0
    for ele in all_review:
        rating = rating + int(ele.rating)
    avg = rating/len(Reviews.objects.all())
    avg = float("{:.2f}".format(avg))
    number = len(Reviews.objects.all())
    top_reviews = Reviews.objects.filter(rating=5)[0:3]
    return render(request, 'main/home.html', {'quote': quote, 'reviews':top_reviews, 'avg':avg, 'number':number})

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def explore(request): 
    return render(request, 'main/explore.html')

def resources(request):
    pythons = Python.objects.all()
    cplusplus = Cplusplus.objects.all()
    mlai = MLAI.objects.all()
    arduino = Arduino.objects.all()
    webdev = WebDev.objects.all()
    others = Books.objects.all()
    return render(request, 'main/resources.html', {'pythons':pythons, 'cplusplus': cplusplus, 'mlai':mlai,'arduino':arduino, 'webdev':webdev, "others":others})

def articles(request): 
    return render(request, 'main/articles.html')

def team(request):
    return render(request, 'main/team.html')

def privacy(request):
    return render(request, 'main/privacy.html')

def pi1001(request):
    return render(request, 'main/Articles/Python/1001.html')

def pi1002(request):
    return render(request, 'main/Articles/Python/1002.html')

def pi1003(request):
    return render(request, 'main/Articles/Python/1003.html')

def ci1001(request):
    return render(request, 'main/Articles/C++/1001.html')

def ci1002(request):
    return render(request, 'main/Articles/C++/1002.html')

def ci1003(request):
    return render(request, 'main/Articles/C++/1003.html')

def mli1001(request):
    return render(request, 'main/Articles/MLAI/1001.html')

def mli1002(request):
    return render(request, 'main/Articles/MLAI/1002.html')

def mli1003(request):
    return render(request, 'main/Articles/MLAI/1003.html')

def webi1001(request):
    return render(request, 'main/Articles/WebDev/1001.html')

def webi1002(request):
    return render(request, 'main/Articles/WebDev/1002.html')

def webi1003(request):
    return render(request, 'main/Articles/WebDev/1003.html')

def mail(request):
    persons = ['Bhabatosh Mohanta', 'Rashmi Ranjan Das', 'Smita Kumari Jha', 'Shovna Panda', 'Suman Patra']
    num = random.randint(0,4)
    success = 1
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        study = request.POST['study']
        feedback = request.POST['feedback']
        subject1 = 'Feedback Submission Successful'
        subject2 = 'New Feedback from ' + name
        message = 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Address: ' + address + '\n' + 'Contact Number: ' + phone + '\n' +"Education: " + study + '\n' + "Message: " + feedback
        reply = 'This is an autogenerated email.\n\n Your Feedback has been submitted successfully. Our team will reach to you within 24 hours.\n\n Thankyou for your valuable time and support.\n\n Important: Do not reply to this mail.'
        try:
            send_mail(subject1, 'Submission Details: \n\n' + message + '\n\n' + reply + '\n', 'in.pathapadha@gmail.com', [email], fail_silently=False)
            send_mail(subject2, message + '\n\n Assigned Person: ' + persons[num], 'in.pathapadha@gmail.com', ['in.pathapadha@gmail.com'], fail_silently=False)
        except:
            success = 0
        print(success)
        if success == 1:
            messages.info(request, 'Feedback Submitted Successfully. Please Check your email.')
            return redirect("contact")
        else:
            messages.info(request, 'Error Submitting Feedback. Please try again after sometime.')
            return redirect("contact")
    else:
        return redirect("/contact")

def exam(request):
    return render(request, 'main/exam.html')

def donation(request):
    return render(request, 'main/donation.html')

def review_page(request):
    reviews = Reviews.objects.order_by('-id')
    top_reviews = Reviews.objects.filter(rating=5)[0:2]
    latest_reviews = Reviews.objects.order_by('-time')[0:3]
    return render(request, 'main/reviews.html', {'reviews':reviews, 'top_reviews':top_reviews, 'latest_reviews':latest_reviews})

def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        review = request.POST['review']
        rating = request.POST['rating']
        time = datetime.now()
        r = Reviews(name=name, email=email,city=city, review=review, rating=rating, time=time)
        r.save()
        return redirect('review_page')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .form  import FeedBackForm

# Create your views here.
def thanks(request):
    return render(request,'feedbackapp/thanku.html')

def feedbackform1(request):
    form = forms.FeedBackForm()
    return render(request, 'feedbackapp/feedback.html',{'form':form})

def feedbackview(request):
    form = FeedBackForm()
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            print("form validation is successful printing the feedback info.")
            print('student name :',form.cleaned_data['name'])
            print('student rollno :', form.cleaned_data['rollno'])
            print('student email :', form.cleaned_data['email'])
            print('student feedback :', form.cleaned_data['feedback'])
            return thanks(request)
    return render(request,'feedbackapp/feedback.html',{'form':form})
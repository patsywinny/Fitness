from django.shortcuts import render,redirect
from fitnessapp.models import member,login,contact
from fitnessapp.forms import memberForm,contactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        if member.objects.filter(
            email = request.POST['email'],
            password = request.POST['password']
        ).exists():
            return render(request,'home.html')
        else:
            return render(request, 'log_in.html')

    else:
        return render(request, 'home.html')


# function for join us
def sign_up(request):
    if request.method == 'POST':
        mymember=member(
            fullname = request.POST['fullname'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
            repeat_password=request.POST['repeat-password']
        )
        mymember.save()
        return redirect('/log_in')
    else:
        return render(request, 'sign_up.html')
  


#   function for log in 
def log_in(request):
    return render(request, 'log_in.html')
     
    


def nutrition(request):
    return render(request,template_name='nutrition.html')

def training(request):
    return render(request,template_name='training.html')

def review_us(request):
    return render(request,template_name='review_us.html')


# contact us 
def contact_us(request):
    if request.method == 'POST':
        mycontact=contact(
           
            username = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message=request.POST['message']
        )
        mycontact.save()
        return redirect('/display')
    else:
        return render(request, 'contact_us.html')
    
# for showing members
def show(request):
    allmembers = member.objects.all()
    return render(request, 'show.html',{'member':allmembers})


# for displaying join us
def display(request):
    allcontacts = contact.objects.all()
    return render(request, 'display.html',{'contact':allcontacts})


# delete for join us
def delete(request, id):
    person = member.objects.get(id=id)
    person.delete()
    return redirect('/show')


# delete for contact us
def delete_1(request, id):
    cont = contact.objects.get(id=id)
    cont.delete()
    return redirect('/display')


# editing member

def edit(request, id):
   editmember = member.objects.get(id=id)
   return render(request, 'edit.html', {'member':editmember})


# update memmbers
def update(request, id):
    updateinfo = member.objects.get(id=id)
    form = memberForm(request.POST, instance=updateinfo)
    print(form.data)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html' )


def edit2(request, id):
   editcontact = contact.objects.get(id=id)
   return render(request, 'edit2.html', {'contact':editcontact})


# update contact
def update_1(request, id):
    updatedata = contact.objects.get(id=id)
    form = contactForm(request.POST, instance=updatedata)
    print(form.data)
    print(form.errors)
    if form.is_valid():
        form.save()
        return redirect('/display')
    else:
        return render(request, 'edit2.html')

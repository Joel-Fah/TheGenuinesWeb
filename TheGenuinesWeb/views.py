from django.http.response import BadHeaderError
from django.shortcuts import redirect, render, HttpResponse
from .forms import MyOrderForm
from django.contrib import messages
from django.core.mail import send_mail
import re



# Create your views here.
def Home(request):
    return render(request, 'blog.html')


def Order(request):
    
    context = {
        'modelform': MyOrderForm
    }
    
    return render(request, 'index_order.html', context)


def GetOrder(request):
    # phone and email format extract
    phone_pattern = r"^6........"
    email_pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.-]+)"
    if request.method == 'POST':   
        form = MyOrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Name']
            phone = form.cleaned_data['Phone'] 
            email = form.cleaned_data['Email']
            product = form.cleaned_data['Product']
            amount = form.cleaned_data['Amount']
            # if re.match(phone_pattern, str(phone)) == True and re.match(email_pattern, email) == True:
            message = form.cleaned_data['AdditionalInfo'] #+ ' ' + "|| Senders email: " + f'{email}'
            msg = "Congratulations if you receive this email, then your order is already in treatment by the Genuines corp. Below are the order information..." + "\n\nName : " + name + "\nPhone Number : " + str(phone) + "\nEmail Address : " + f'{email}' + "\nAdditional Information : " + message + "\nOrdered pamphlet : " + product + "\nNumber of copies ordered : " + str(amount) + ' copies' + "\n\n\nThanks for trusting us. Hope to see you soon.\nTel : 656997810\nEmail : joefah2003@gmail.com\nWrite us anywhen you want about anything!"
            subject = 'Order Credentials/Information from ' + name
            try:
                send_mail(
                    subject, #subject
                    msg, #message
                    email, #from email
                    ['joelfah2003@gmail.com', email], #to email
                    )
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            # Save in DB
            form.save()
            
            # Flash message to confirm order placement.
            messages.success(request, f'Thanks {name}! We received your email and will respond shortly... A copy will be sent to you in the meantime!') 
            return redirect('Order') 
            # else:
            #     # Flash message for send email error.
            #     messages.error(request, f'Sorry {name}! There was an error while sending the email. Verify you entered it correctly or try to refresh the page ang try again')
            #     return HttpResponse('index_order.html')
    else:
        form = MyOrderForm()        
    return render(request, 'index_order.html', {'modelform': MyOrderForm})

def Developer(request):
    return render(request, 'index_developer.html')


def PortfolioDetails(request):
    return render(request, 'portfolio-details.html')
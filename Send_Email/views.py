from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from .forms import EmailForm
from .models import EmailModel, Users
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage


# Create your views here.

def index(request):
    email = EmailForm()
    context = {'email': email}
    return render(request, 'index.html', context=context)


@require_POST
def Send(request):
    mails = None
    upload_file = None
    file = None
    mail = None
    try:
        subform = EmailForm(request.POST)
        if subform.is_valid():
            sub_mes = EmailModel(sub=request.POST['subject'], mes=request.POST['message'])
            sub_mes.save()
            sent = Users(from_mail=request.POST['from_mail'], to_mail=request.POST['to_mail'])
            sent.save()
    except:
        raise EnvironmentError('Invalid Form')
    try:
        if request.method == 'POST':
            upload_file = request.FILES.get('document', False)
            fs = FileSystemStorage()
            file = fs.save(upload_file)
            sub_mes = EmailModel.objects.values_list().last()
            sent_add = Users.objects.values_list().last()
            sub = sub_mes[1]
            mes = sub_mes[2]
            frommail = sent_add[1]
            tomail = sent_add[2]
            mail = EmailMessage(sub, mes, frommail, [tomail])
            mail.attach(upload_file.name, upload_file.read(), upload_file.content_type)
            mail.send()

    except:
        if upload_file is None:
            sub_mes = EmailModel.objects.values_list().last()
            sent_add = Users.objects.values_list().last()
            sub = sub_mes[1]
            mes = sub_mes[2]
            frommail = sent_add[1]
            tomail = sent_add[2]
            mail = EmailMessage(sub, mes, frommail, [tomail])
            mail.send()

    if mail.send() == 1:
        return redirect('result')
    else:
        return HttpResponse('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css'
                            '/bootstrap.min.css" '
                            'integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" '
                            'crossorigin="anonymous"><div class="alert alert-danger" role="alertdialog">Mail '
                            'Unsent</div>')


def result(request):
    return render(request, 'result.html')

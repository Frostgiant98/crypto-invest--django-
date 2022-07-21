from re import template
from django.shortcuts import render
from django.test import RequestFactory
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponsePermanentRedirect
from django.urls.base import reverse
from myapp.forms import SignUpForm, profile_form, user_profile_form, admin_profile_form, admin_user_profile_form, deposits_form, withdrawal_form
from django.shortcuts import get_object_or_404
from myapp.models import Profile, User, deposits_table, notifications_table, wallet_table, withdrawal_table, history_table
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import  staff_member_required

# Create your views here.

def homepage(request):
    template_name = 'index.html'
    return render(request , template_name)

@login_required
def dashboard(request):
    hist = history_table.objects.all()
    context = { 'history' : hist }

    template_name = 'dashboard.html'
    return render(request , template_name, context)  


@login_required
def profile_edit(request):

    if request.method == 'POST': 
        useredit = get_object_or_404(User, id = request.user.id)
        userform = user_profile_form(request.POST, instance=useredit)
        profileform = profile_form(request.POST or None, instance=useredit.profile)
        if(userform.is_valid) and (profileform.is_valid):
            userform.save()
            profileform.save()
            return newdash(request)
        return HttpResponsePermanentRedirect(reverse('profile_edit'))
    else:
        useredit = get_object_or_404(User, id = request.user.id)
        userform = user_profile_form(request.POST, instance=useredit)
        profileform = profile_form(request.POST or None, instance=useredit.profile)
    template_name = 'dash/dash_user_edit_profile.html'
    return render(request , template_name , context={"form1":profileform, 'form2':userform})

@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def admin_profile_delete(request, User_id):
    User.objects.filter(id = User_id).delete()
    return user_list(request)

@login_required
def newdash(request):

    allusers = deposits_table.objects.filter(user_id = request.user.id)
    allnotif = notifications_table.objects.filter(user_id = request.user.id)
    allwith = withdrawal_table.objects.filter(user_id = request.user.id)

    context =  {
        'deposits' : allusers,
        'notifs' : allnotif,
        'withdr' : allwith
        }
    template_name = 'dash/new_dash.html'
    return render(request , template_name, context)

def user_list(request):
    allusers = User.objects.all()
    template_name = 'dash/dash_admin_manage_users.html'
    context =  {
        'allusers' : allusers
        }
    return render(request, template_name, context)

def deposit_list(request):

    allusers = deposits_table.objects.all()
    template_name = 'dash/dash_admin_manage_deposits.html'
    context =  {
        'deposits' : allusers
        }
    return render(request, template_name, context)


@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def admin_user_edit(request, user_id):

    if request.method == 'POST': 
        useredit = get_object_or_404(User, id = user_id)
        userform = admin_user_profile_form(request.POST, instance=useredit)
        profileform = admin_profile_form(request.POST or None, instance=useredit.profile)
        if(userform.is_valid) and (profileform.is_valid):
            userform.save()
            profileform.save()
            return user_list(request)
        return HttpResponsePermanentRedirect(reverse('admin_user_edit', user_id))
    else:
        useredit = get_object_or_404(User, id = user_id)
        userform = admin_user_profile_form(request.POST, instance=useredit)
        profileform = admin_profile_form(request.POST or None, instance=useredit.profile)
    template_name = 'dash/dash_user_edit_profile.html'
    return render(request , template_name , context={"form1":profileform, 'form2':userform})


def notif(request):
    template_name = 'dash_admin_manage_notifications.html'
    return render(request , template_name)

@staff_member_required
@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, user_id):

    User.objects.filter(id=user_id).delete()    
    return user_list(request)

@login_required
def deposits2(request):
    

    template_name = 'dash/dash_deposits2.html'
    return render(request , template_name )


@login_required
def deposits(request):
    if request.method == "POST":
        searched = request.POST['depo']
        post = deposits_table(user_id = request.user.id, amount = searched)
        post.save()        
        context = {'amount':searched}
        template_name = 'dash/dash_deposits2.html'
        return render(request, template_name, context)
    else:
        template_name = 'dash/dash_deposits.html'
        return render(request , template_name )


@login_required
def withdraw(request):
    if request.method == "POST":
        amount = request.POST['amount']
        wallet = request.POST['wallet']
        coin = request.POST['customRadio-1']
        post = withdrawal_table(user_id = request.user.id, amount = amount, withdrawal_wallet = wallet, withdrawal_account = coin)
        post.save()
        return newdash(request)
        
    else:
        withdr = withdrawal_form()        
    context =  {'withdrawal' : withdr}
    template_name = 'dash/dash_withdrawal.html'
    return render(request , template_name, context )


@login_required
def upgrade(request):
    
    template_name = 'dash/dash_Upgrade.html'
    return render(request , template_name )


class SignUpView(generic.CreateView):
    
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
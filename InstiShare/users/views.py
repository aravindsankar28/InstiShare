from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from models import UserProfile
def login(request):
    return render_to_response('users/login.html', locals(), context_instance = RequestContext(request)) 

def register(request):
	UserFormset = modelformset_factory(User,fields=('username','first_name','last_name','password'),extra=1)
	UserProfileFormset = modelformset_factory(UserProfile,fields=('nick','hostel','phone_number','email'),extra=1)
	UserItem = UserFormset(queryset= None)
	UserProfileItem = UserProfileFormset(queryset= None)
	return render_to_response('users/register.html', locals(), context_instance = RequestContext(request)) 
	
	

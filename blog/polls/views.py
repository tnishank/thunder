import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response

from django.http import HttpResponse,request, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from models import MyUser, Posts
from django.contrib.auth.decorators import login_required

@csrf_exempt
def post(request):
	if request.method == 'POST' and request.session['username']==\
								request.POST.get('username'):
		try:
			author_id=request.POST.get('author_id')
			u = MyUser.objects.get(id=author_id)
			body = request.POST.get('body')
			pp=Posts.objects.create(body=body,author_id=u)
			pp.save()
			return HttpResponse("post successfully published")
		
		except Exception:
			return HttpResponse("User does not exist")
	else:
		return HttpResponse("please signin first")

def comment(request):
	# if request.method == 'POST' and request.session['username']==\
	# 							request.POST.get('username'):
	# 	try:
	# 		author_id=request.POST.get('author_id')
	# 		post_id=request.POST.get('post_id')
	# 		body = request.POST.get('body')
	# 		u = MyUser.objects.get(id=author_id)
	# 		pp=Comments.objects.create(body=body,author_id=u,post_id=post_id )
	# 		pp.save()
	# 		return HttpResponse("comment successfully published")
	# 	except Exception:
	# 		return HttpResponse("User does not exist")
	# else:
	# 	return HttpResponse("please signin first")
	pass
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse,request, HttpResponseRedirect

from rest_framework.decorators import api_view

from dbapi import create_user, create_user_profile, get_user
from blog.response import send_200, send_409, send_400

@api_view(["POST"])
def signup(request):
	"""
	Creates new fresh userprofile
	"""
	username = request.POST.get('username')
	password = request.POST.get('password')
	email = request.POST.get('email')
	user = get_user(username=username)
	if user:
		return send_409({"error":"user already exist with this username"})
	user = create_user(username=username, password=password, email=email)
	location = request.POST.get('location')
	about_me = request.POST.get('about_me')
	create_user_profile(user=user,location=location,about_me=about_me)

	return send_200({"message":"profile successfuly created"})

@api_view(["POST"])
def signin(request):
	"""
	Login view
	"""
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = get_user(username=username)
	if not user:
			return send_400({"error":"username or password is wrong"})
	user=authenticate(username=username, password=password)
	login(request, user)
	return send_200({"message":"logged in successfully"})


@api_view(["POST"])
def signout (request):
	"""
	Logout view
	"""
	logout(request)
	return send_200({"message":"logged out successfully"})



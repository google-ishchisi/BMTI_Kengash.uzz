from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from django.contrib import messages
from .models import Post, Azolar,  Carusel
from .forms import  CommentForm
from django.core.paginator import Paginator

from twilio.rest import Client

def index(request):
	posts = Post.objects.order_by('-id')[:]
	azo = Azolar.objects.all()
	carusel = Carusel.objects.all()

	p = Paginator(posts, 6)
	page = request.GET.get('page')
	post = p.get_page(page)

	nums = 's' * post.paginator.num_pages
	if request.method == "POST":
		user = request.user
		text = request.POST['taklif']
		if text:
			account_sid = 'ACeb49f1f93e6a3dfe22303309a7da8399'
			auth_token = 'df1b1fa3d74c973b2117a494c86dadda'
			client = Client(account_sid, auth_token)

			message = client.messages.create(
				body = 'Dasturchi Ruslanbek aka !!! ' + " Taklif matni- " + text,
				from_='+18287053058',
				to='+998914162582'
			)
			messages.success(request, "Fikringiz yuborildi. Tez orada javob olishingiz mumkin !")
			redirect('/')
		else:
			redirect('/')
	context = {
		'azo': azo,
		'carusel': carusel,
		'p': p,
		'post': post,
		'nums': nums,
	}
	return render(request, 'index.html', context)


def detail(request,id):
	post = Post.objects.get(id=id)
	form = CommentForm()
	user = request.user
	if request.method=='POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.post_id = post.id
			f.name_id = user.id
			f.save()	

	context = {
		'p': post,
		'form': form,
	}
	return render(request, 'detail.html', context)




def register(request):
	if request.method=='POST':
		username = request.POST.get('username')
		ism = request.POST.get('ism')
		familya = request.POST.get('firstname')
		password1 = request.POST.get('parol1')
		password2 = request.POST.get('parol2')

		
		if password1==password2 and password1!="" and len(username)>8:
			if not User.objects.filter(username=username).exists():
				user = User.objects.create_user(username=username, first_name=familya, last_name =ism, password=password1)
				user.save()
				messages.success(request, "Siz royhatdan muvaffaqiyatli otdingiz")

				return redirect('/')
			else:
				messages.info(request, 'Bu nomli foydalanuvchi bor !!!')
		else:
			messages.info(request, 'Parollar bir xilmas yoki username 8 tadan kichik !!!')
	return render(request, 'register.html')


def login_user(request):
	if request.method=='POST':
		username = request.POST.get('login')
		password = request.POST.get('parol')

		user = authenticate(username=username, password=password)
		if user:
			print('Tizimga kirdiz')
			messages.success(request, 'Tizimga kirdingiz !!!')
			login(request, user)
			return redirect('index')
		else:
			print('Tizimga kirolmadiz')			
			messages.error(request, 'Login/parol xato terildi !!!')
			return redirect('login')
	return render(request, 'login.html')

def logout_user(request):
	logout(request)
	messages.info(request, 'Tizimdan chiqdingiz !!!')

	return redirect('login')
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .forms import * 
from pusher import Pusher 
import json 

pusher = Pusher(app_id=u'796493', key=u'627edbfb8e96c901960e', secret=u'b2274d773cc6e5c4b25b', cluster=u'us2')

def index(request):
	all_documents=Feed.objects.all().order_by('-id')
	return render(request, 'index.html', {'all_documents': all_documents})
# Create your views here.

def pusher_authentication(request):
	channel = request.GET.get('channel_name', None)
	socket_id = request.GET.get('socket_id', None)
	auth = pusher.authenticate(
		channel = channel, 
		socket_id = socket_id
	)
	return JsonResponse(json.dumps(auth), safe=False)

def push_feed(request):
	if request.method == 'POST': 
		form = DocumentForm(request.POST, request.FILES)
		if Feed.objects.filter(description= request.POST['description']).count() != 0 :
			return HttpResponse('Descriptor already in use, please select a new descriptor')
		if form.is_valid():
			f = form.save()
			pusher.trigger(u'a_channel',u'an_event', {u'description': f.description, u'document': f.document.url})
			return HttpResponse('ok')
		else:
			return HttpResponse('form not valid')
	else: 
		return HttpResponse('error, please try again')

def delete_all(request):
	if request.method == "POST":
		all_documents = Feed.objects.all().delete()
	return HttpResponse('delete completed')


def delete_one(request):
	# print(data)
	if request.method == "POST":
		all_documents = Feed.objects.filter(description=request.POST['id']).delete()
	return HttpResponse('delete completed')


def share_pic(request, pic_id):
	doc = get_object_or_404(Feed, description=pic_id)
	return render(request, 'trial.html', {'all_documents': doc})

def get_share_url(request): 
	#Generate shareable links, hardcoding for now 
	# print(request.POST)
	id = request.POST['id']
	# print(id)
	doc = "localhost:8080/share_pic/"+str(id)
	# print(pic_id)
	return HttpResponse(doc)
	# return JsonResponse({'res':doc})

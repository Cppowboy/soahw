from django.http import HttpResponse
from django.shortcuts import render_to_response
import requests

client_id='3223538172'
client_secret='b73de5b91fdfeb12e7201547a41bcd48'
base_url='http://101.200.81.62'

def hello(request):
    return HttpResponse("Hello World!")

def home(request):
    dic={'client_id':client_id,'response_type':'code','redirect_uri':base_url+'/access'}
    return render_to_response('home.html',dic)

def users(request):
    return HttpResponse("Users Page")

def access(request):
    if request.GET.has_key('code'):
        code=request.GET['code']
        data={'grant_type':'authorization_code', 'redirect_uri':'http://101.200.81.62/access','code':code}
        url='https://api.weibo.com/oauth2/access_token'
        headers={'client_id':client_id,'client_secret':client_secret)
        resp=requests.post(url,data=data,headers=headers)
        return HttpResponse(resp.json())
    else:
        return HttpResponse('can not find code')

def posts(request):
    return HttpResponse('Post Page')

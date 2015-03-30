#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import socket,urllib,urllib2,httplib,json

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
        data={'client_id':client_id, 'client_secret':client_secret,\
                 'grant_type':'authorization_code', 'redirect_uri':'http://101.200.81.62/access/',\
                 'code':request.GET['code']}
        host='api.weibo.com'
        url='/oauth2/access_token'
        para=urllib.urlencode(data)
        headers={'Content-type':'application/x-www-form-urlencoded','Accept':'text/plain'}
        addr=socket.gethostbyname(host)
        con=httplib.HTTPConnection(addr)
        con.request('POST',url,para,headers)
        response=con.getresponse()
        return HttpResponse(response.status)
    else:
        return HttpResponse('can not find code')

def posts(request):
    return HttpResponse('Post Page')

#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import socket,urllib,httplib,json

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
        burl='api.weibo.com'
        surl="/oauth2/access_token"
        para=urllib.urlencode(data)
        #headers={"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "text/json"}
        addr=socket.gethostbyname(burl)
        connection=httplib.HTTPConnection(addr,80,timeout=3)
        connection.request('post',surl,body=para)
        response=connection.getresponse()
        return HttpResponse(response.read())
    else:
        return HttpResponse('can not find code')

def posts(request):
    return HttpResponse('Post Page')

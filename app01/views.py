from django.shortcuts import render,HttpResponse

# Create your views here.
def set_session(request):
    request.session["username"] = "123"
    request.session["password"] = "456"
    return HttpResponse("保存session数据成功")
# jkg4wduptrnjm8rulkfe1o2y7cvqqnjv
# jkg4wduptrnjm8rulkfe1o2y7cvqqnjv
# jkg4wduptrnjm8rulkfe1o2y7cvqqnjv
def get_session(request):
    username = request.session.get("username")
    password = request.session.get("password")
    info = username+"   "+password
    return HttpResponse(info)
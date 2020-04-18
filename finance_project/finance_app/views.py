from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import authenticate, login


class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'finance_app/home_page.html'

    def get(self, request):
        return Response({'msg' : 'welcome'})

class LoginPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'finance_app/login_page.html'

    def post(self, request):
        print(request.POST['username'], request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)

        print(user.email)
        return Response({'msg' : 'Redirected to Login Page'})


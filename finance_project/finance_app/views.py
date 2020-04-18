from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth import authenticate, login
from .forms import RolesForm, LendingDetailForm, BorrowingDetailForm
from .models import Roles, LendingHistory, BorrowingHistory


class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'finance_app/home_page.html'

    def get(self, request):
        return Response({'msg' : 'welcome'})

class LoginPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'finance_app/logged_in_landing_page.html'

    def post(self, request):
        print(request.POST['username'], request.POST['password'])
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            RolesQuerySet = Roles.objects.all()
            LendingHistoryQuerySet = LendingHistory.objects.all()
            BorrowingHistoryQuerySet = BorrowingHistory.objects.all()
            return Response({'RolesForm' : RolesForm,
                             'LendingDetailForm':LendingDetailForm,
                             'BorrowingDetailForm' : BorrowingDetailForm,
                             'RolesQuerySet' : RolesQuerySet,
                             'LendingHistoryQuerySet' : LendingHistoryQuerySet,
                             'BorrowingHistoryQuerySet' : BorrowingHistoryQuerySet})

        return Response({'msg' : 'Redirected to Login Page'})


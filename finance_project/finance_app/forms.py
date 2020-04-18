from django.forms import ModelForm
from .models import Roles, LendingDetail, BorrowingDetail

class RolesForm(ModelForm):

    class Meta:
        model = Roles
        fields = ['role']

class LendingDetailForm(ModelForm):

    class Meta:
        model = LendingDetail
        fields = ['leneded_to', 'lending_amount', 'lending_date', 'interest_rate', 'interest_period',
                  'expected_return_date', 'comments']

class BorrowingDetailForm(ModelForm):

    class Meta:
        model = BorrowingDetail
        fields = ['borrowed_to', 'borrowed_amount', 'borrowed_date', 'interest_rate', 'interest_period',
                  'expected_return_date', 'comments']
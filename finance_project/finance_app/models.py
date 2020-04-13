from django.db import models

class Roles(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    role = models.CharField(db_column='role', max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'roles'
        ordering = ['id']

class PersonalDetail(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    tenant_id = models.IntegerField(db_column='tenant_id', blank=False, null=False)
    name = models.CharField(db_column='name', max_length=255, blank=False, null=False)
    dob = models.DateField(db_column='dob', blank=False, null=False)
    age = models.IntegerField(db_column='age', blank=False, null=False)
    phone_number = models.IntegerField(db_column='phone_number', blank=False, null=False)
    address = models.TextField(db_column='address', blank=False, null=False)
    role = models.ForeignKey(db_column='role', to=Roles, on_delete=models.CASCADE)
    created_time = models.DateTimeField(db_column='created_time', blank=False, null=False)
    modified_time = models.DateTimeField(db_column='modified_time', blank=False, null=False)
    deleted_time = models.DateTimeField(db_column='deleted_time', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'personal_detail'
        ordering = ['id']

class Tenant(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, blank=False, null=False)
    created_time = models.DateTimeField(db_column='created_time', blank=False, null=False)
    status = models.BooleanField(db_column='status', default=True, blank=False, null=False)
    modified_time = models.DateTimeField(db_column='modified_time', blank=False, null=False)
    deleted_time = models.DateTimeField(db_column='deleted_time', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'tenant'
        ordering = ['id']

class LendingDetail(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    leneded_to = models.ForeignKey(db_column='lended_to', to=PersonalDetail, on_delete=models.CASCADE)
    lending_amount = models.FloatField(db_column='lending_amount', null=False, blank=False)
    lending_date = models.DateTimeField(db_column='lending_date', blank=False, null=False)
    interest_rate = models.FloatField(db_column='interest_rate', blank=False, null=False)
    interest_period = models.CharField(db_column='interest_period', max_length=255, blank=False, null=False)
    expected_return_date = models.DateTimeField(db_column='expected_return_date', null=True, blank=False)
    comments = models.TextField(db_column='comments', null=True, blank=True)


    class Meta:
        managed = True
        db_table = 'lending_detail'
        ordering = ['id']

class LendingHistory(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    lended_by = models.ForeignKey(db_column='lended_by', to=PersonalDetail, on_delete=models.CASCADE)
    lended_detail = models.ForeignKey(db_column='lended_detail', to=LendingDetail, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'lending_history'
        ordering = ['id']

class BorrowingDetail(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    borrowed_to = models.ForeignKey(db_column='borrowed_to', to=PersonalDetail, on_delete=models.CASCADE)
    borrowed_amount = models.FloatField(db_column='borrowed_amount', null=False, blank=False)
    borrowed_date = models.DateTimeField(db_column='borrowed_date', blank=False, null=False)
    interest_rate = models.FloatField(db_column='interest_rate', blank=False, null=False)
    interest_period = models.CharField(db_column='interest_period', max_length=255, blank=False, null=False)
    expected_return_date = models.DateTimeField(db_column='expected_return_date', null=True, blank=False)
    comments = models.TextField(db_column='comments', null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'borrowing_detail'
        ordering = ['id']


class BorrowingHistory(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    borrowed_from = models.ForeignKey(db_column='borrowed_from', to=PersonalDetail, on_delete=models.CASCADE)
    borrowed_detail = models.ForeignKey(db_column='borrowed_detail', to=BorrowingDetail, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'borrowing_history'
        ordering = ['id']
from django.db import models
import django
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from datetime import datetime as dt


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None,commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """


        user = self.model(
            email=self.normalize_email(email),
            username = username
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        print("creating super user....")
        user = self.create_user(

            username=username,
            password=password,
            email = email,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Roles(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    role = models.CharField(db_column='role', max_length=255, blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'roles'
        ordering = ['id']

class PersonalDetail(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(db_column='id', primary_key=True)
    username = models.CharField(db_column='username', max_length=20, unique=True, blank=False, null=False)
    email = models.EmailField(db_column='email', blank=True, null=False)
    tenant_id = models.IntegerField(db_column='tenant_id', blank=False, null=True)
    name = models.CharField(db_column='name', max_length=255, blank=False, null=True)
    dob = models.DateField(db_column='dob', blank=False, null=True)
    age = models.IntegerField(db_column='age', blank=False, null=True)
    phone_number = models.IntegerField(db_column='phone_number', blank=False, null=True)
    address = models.TextField(db_column='address', blank=False, null=True, )
    role = models.ForeignKey(db_column='role', to=Roles, on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(db_column='is_staff', blank=True, null=True, default=False)
    created_time = models.DateTimeField(db_column='created_time', blank=False, null=False, default=django.utils.timezone.now)
    modified_time = models.DateTimeField(db_column='modified_time', blank=False, null=False, default=django.utils.timezone.now)
    deleted_time = models.DateTimeField(db_column='deleted_time', blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'personal_detail'
        ordering = ['id']

    def __str__(self):
        return self.username

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
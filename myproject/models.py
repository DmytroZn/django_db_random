# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppOneAgregat(models.Model):
    n_zag = models.CharField(max_length=40)
    n_agr = models.IntegerField()
    n_zone = models.ForeignKey('AppOneZone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_one_agregat'


class AppOneCorpus(models.Model):
    name_corpus = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'app_one_corpus'


class AppOneZone(models.Model):
    n_zone = models.IntegerField()
    corpus = models.ForeignKey(AppOneCorpus, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_one_zone'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoPlotlyDashDashapp(models.Model):
    instance_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)
    base_state = models.TextField()
    creation = models.DateTimeField()
    update = models.DateTimeField()
    save_on_change = models.BooleanField()
    stateless_app = models.ForeignKey('DjangoPlotlyDashStatelessapp', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_dashapp'


class DjangoPlotlyDashStatelessapp(models.Model):
    app_name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=110)

    class Meta:
        managed = False
        db_table = 'django_plotly_dash_statelessapp'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MainAgregate(models.Model):
    number_of_controller = models.IntegerField(blank=True, null=True)
    t_delta = models.IntegerField(blank=True, null=True)
    t_input = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    t_output = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    auto_hand = models.CharField(max_length=30, blank=True, null=True)
    capacity = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    capacity_warm = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    capacity_current = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    pressure = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    digital_input = models.IntegerField(blank=True, null=True)
    digital_output = models.IntegerField(blank=True, null=True)
    parameters = models.IntegerField(blank=True, null=True)
    w_accumulate = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    w_current = models.DecimalField(max_digits=1000, decimal_places=1, blank=True, null=True)
    zdate = models.DateField(blank=True, null=True)
    ztime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_agregate'

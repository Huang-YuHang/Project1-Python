# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class College(models.Model):
    id = models.AutoField(primary_key=True,db_column='collid')
    name = models.CharField(max_length=50,db_column='collname')
    intro = models.CharField(max_length=500,db_column='collintro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_college'



class Student(models.Model):
    id = models.IntegerField(primary_key=True,db_column='stuid')
    name = models.CharField(max_length=20,db_column='stuname')
    sex = models.IntegerField(blank=True, null=True,db_column='stusex')
    birth = models.DateField(blank=True, null=True,db_column='stubirth')
    addr = models.CharField(max_length=255, blank=True, null=True,db_column='stuaddr')
    college = models.ForeignKey(College, models.PROTECT, db_column='collid')

    class Meta:
        managed = False
        db_table = 'tb_student'


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True,db_column='teaid')
    name = models.CharField(max_length=20,db_column='teaname')
    title = models.CharField(max_length=10,db_column='teatitle', blank=True, null=True)
    college = models.ForeignKey(College, models.PROTECT, db_column='collid')

    class Meta:
        managed = False
        db_table = 'tb_teacher'

class Course(models.Model):
    id = models.AutoField(primary_key=True,db_column='couid')
    name = models.CharField(max_length=31,db_column='couname')
    credit = models.IntegerField(db_column='coucredit')
    teacher = models.ForeignKey(Teacher, models.PROTECT, db_column='teaid')

    class Meta:
        managed = False
        db_table = 'tb_course'

class Record(models.Model):
    id = models.AutoField(primary_key=True,db_column='recid')
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='sid')
    course = models.ForeignKey(Course, models.PROTECT, db_column='cid')
    seldate = models.DateTimeField(blank=True, null=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_record'
        unique_together = (('student','course'),)
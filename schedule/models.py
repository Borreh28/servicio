from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.description


class Evidence(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.description


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    no_employee = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    career = models.CharField(max_length=250)
    level_of_study = models.CharField(max_length=250)
    speciality = models.CharField(max_length=250)

    def __str__(self):
        return '%s - %s %s' % (self.no_employee, self.name, self.last_name)


class SchoolSubject(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    theoretical_hours = models.IntegerField()
    practical_hours = models.IntegerField()
    credits = models.IntegerField()
    units = models.IntegerField()
    areas = models.ManyToManyField(Area)

    def __str__(self):
        return '%s - %s' % (self.code, self.name)


class Career(models.Model):
    name = models.CharField(max_length=250)
    school_subjects = models.ManyToManyField(SchoolSubject)

    def __str__(self):
        return '%s' % self.name


class Profile(models.Model):
    description = models.CharField(max_length=250)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    evidence = models.ForeignKey(Evidence, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s (%s): %s' % (self.teacher.name, self.teacher.last_name, self.area.description, self.description)


class Schedule(models.Model):
    period = models.CharField(max_length=250)
    year = models.IntegerField()
    weekday = models.IntegerField()
    start = models.IntegerField()
    end = models.IntegerField()
    return_date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s %d:00 - %d:00' % (self.teacher.name, self.weekday, self.start, self.end)


class SchoolSubjectLog(models.Model):
    period = models.CharField(max_length=250)
    year = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    school_subject = models.ForeignKey(SchoolSubject, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s (%s, %d)' % (self.teacher.name, self.school_subject.name, self.period, self.year)

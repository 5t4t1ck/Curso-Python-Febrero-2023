from django.db import models

class Course(models.Model):

    course_title = models.CharField(max_length=70)
    course_description = models.TextField()
    course_date = models.DateTimeField("Date of Publication")

    def __str__(self):
        return self.course_title
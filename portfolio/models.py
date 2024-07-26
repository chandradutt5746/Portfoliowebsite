from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

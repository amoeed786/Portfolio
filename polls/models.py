from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # For project pictures
    link = models.URLField(blank=True, null=True)  # Link to the project (if applicable)

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField()

    def __str__(self):
        return self.title
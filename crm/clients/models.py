from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

# Creating users is very important in a website unless the website is an open website and doesn't need user's
# personalization

# Django has a built-in user model that helps to handle anything a user is creating in the website

class User(AbstractUser):
    pass


# ----------------------------------------------------------------

class Client(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # so what this means is that every Client created will be assigned to an Agent
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# ----------------------------------------------------------------

class Agent(models.Model):
    # so what this is doing is that
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email}'


# Understanding Model manager
''' to access a model we use the dot notation (.) + objects
to create a client for instance we say 
Client.objects.create(firstname="person_name", lastname="person_lastname", age="person_age", 
agent="agent assigned to")
'''

'''
how to filter with query

Client.objects.all(firstname="person_name")

 so what this will do is that it will filter all objects with firstname = "person_name"
'''

'''
How to filter for age greater than 19 years of age

Client.objects.filter(age__gt=19)
'''

'''
How to get a specific object with specific value of data

Client.object.get(firstname="Asuquo")

so what this will do is that it only "Asuquo" just as the query name implies "get"
'''

''' Normally 
Data like the agent is to be displayed it on the python shell is displayes like this [Agent:Agent object(1)]
but in order to avoid that you use:

def __str__(self):
    return self.agent

'''

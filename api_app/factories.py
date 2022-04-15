import datetime
import factory
from faker import Faker
from .models import User


fake = Faker()


def generate_username(*args):
    """ returns a random username """
    return fake.profile(fields=['username'])['username']


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.LazyAttribute(generate_username)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda o: f'{o.username}@email.com')
    password = factory.PostGenerationMethodCall('set_password', 'defaultpassword')
    is_active = False
    # date_joined = datetime.datetime.now()
    is_superuser = False


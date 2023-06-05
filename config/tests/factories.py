import factory
from factory.django import DjangoModelFactory
from factory import SubFactory
from django.contrib.auth.models import User

from blog.models import Post


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    password = "test"
    username = "test"
    is_superuser = True
    is_staff = True


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = "x"
    subtitle = "y"
    slug = "x"
    author = SubFactory(UserFactory)
    content = "x"
    status = "published"

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.tags.add(*extracted)

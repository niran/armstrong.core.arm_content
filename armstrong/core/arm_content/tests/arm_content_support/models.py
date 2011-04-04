from django.contrib.auth.models import User
from django.db import models
from polymorphic import PolymorphicModel

from ...authorship.models import AuthorshipMixin
from ...publication.models import PublicationMixin


class BaseContent(PolymorphicModel, AuthorshipMixin, PublicationMixin):
    title = models.CharField(max_length=255)


class Article(BaseContent):
    body = models.TextField()


class Video(BaseContent):
    youtube_id = models.CharField(max_length=30)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def get_absolute_url(self):
        return '/users/%d/' % self.user.id

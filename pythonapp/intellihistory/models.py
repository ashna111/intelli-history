from django.db import models

# Create your models here.
class SessionUrl(models.Model):
    url = models.URLField(_(""), max_length=200)
    page_title = models.CharField(_(""), max_length=50)

class UserSession(models.Model):
    session_id = models.CharField(blank=True, unique=True, default=uuid.uuid4)
    session_urls = ArrayField(
        models.ForeignKey(SessionUrl, verbose_name=_(""), on_delete=models.CASCADE)
    )
from django.db import models


class Key(models.Model):
    key_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.key_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Desc(models.Model):
    key = models.ForeignKey(Key)
    desc_text = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.desc_text

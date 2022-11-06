from django.db import models

class Novel(models.Model):
    # title = models.CharField(max_length = 20)
    pub_date = models.DateTimeField(auto_now_add = True)
    body = models.TextField(default='', null=True, blank=True)
    tmp_body = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return self.pub_date
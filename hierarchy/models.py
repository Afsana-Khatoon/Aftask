from django.db import models


class Relation(models.Model):
    sl_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    parent_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Sl No. -  {self.sl_no} Title -  {self.title} Parent ID - {self.parent_id}'

    class Meta:
        verbose_name_plural = 'Relations'

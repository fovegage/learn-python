from django.db import models


# Create your models here.

class Category(models.Model):
    cate_name = models.CharField(verbose_name='文章分类', max_length=20)
    cate_desc = models.TextField(verbose_name='分类描述', null=True, blank=True, default='')
    is_banner = models.BooleanField(verbose_name='是否栏目', default=False)
    objects = models.Manager()
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cate_name




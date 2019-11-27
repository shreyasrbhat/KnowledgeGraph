from django.db import models

import os


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """default string"""
        return os.path.basename(self.file.name)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()


class GraphConfig(models.Model):
    noun = models.BooleanField(default=False)
    pronoun = models.BooleanField(default=False)
    adjective = models.BooleanField(default=False)
    window = models.IntegerField(default=1)
    file = models.ForeignKey(File, on_delete=models.CASCADE,
                             related_name='configs')

    def __str__(self):
        """default string"""
        return os.path.basename(self.file.file.name)

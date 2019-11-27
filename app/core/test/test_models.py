from django.test import TestCase
from django.core.files import File
from core import models

import os


class TestModels(TestCase):
    def setUp(self):
        with open('core/test/files/test_file.txt') as f:
            file = File(f)
            self.file_obj = models.File.objects.create(
                file=file,
                remark='intro to react'
            )

    def test_file_model(self):
        """Test default return string"""
        self.assertEqual(str(self.file_obj),
                         os.path.basename(self.file_obj.file.name))
        self.file_obj.delete()

    def test_file_delete(self):
        """Test file deletion on instance delete"""
        file_name = self.file_obj.file.name
        self.file_obj.delete()
        self.assertFalse(os.path.isfile(file_name))

    def test_graphconfig_model(self):
        """Test default return string"""
        gc_obj = models.GraphConfig.objects.create(
            file=self.file_obj

        )
        self.assertEqual(str(gc_obj), os.path.basename(gc_obj.file.file.name))
        self.file_obj.delete()

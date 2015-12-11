# -*- coding: utf-8 -*-

import pkgutil
import unittest
import pyception
import importlib


class PyceptionModuleTest(unittest.TestCase):

    def test_if_string_exceptions_and_classes_are_the_same(self):

        kwargs = {'path': pyception.__path__, 'onerror': lambda x: None}

        for importer, modname, ispkg in pkgutil.walk_packages(**kwargs):

            if modname == 'wrapper':
                continue
            mod = importer.find_module(modname).load_module(modname)

            for class_definition in mod.exceptions.keys():
                klass = getattr(mod, class_definition.strip())
                self.assertEqual(klass.__name__, class_definition.strip())

    def test_if_raise_can_be_caught(self):

        with self.assertRaises(pyception.configuration.ConfigurationException):
            raise pyception.configuration.ConfigurationException('ooops')

        with self.assertRaises(IOError):
            raise pyception.io.StorageException('ops!')

    def test_correct_inheritance(self):

        expected = pyception.data.exceptions['DataMisalignedException'][0]
        klass = pyception.data.DataMisalignedException
        self.assertTrue(issubclass(klass, expected))

    def test_import___all__(self):

        self.assertEqual(
            len(pyception.data.__all__),
            len(pyception.data.exceptions.keys())
        )

    def test___name__(self):

        self.assertEqual('pyception.data', pyception.data.__name__)
        self.assertEqual('pyception.io', pyception.io.__name__)

    def test_if_raises_attribute_error_when_a_class_does_not_exists(self):

        with self.assertRaises(AttributeError):
            raise pyception.io.DummyExceptions('ops!')

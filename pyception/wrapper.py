# -*- encoding: utf-8 -*-


class PyceptionModule(object):

    def __init__(self, module_name, exceptions):

        self.exceptions = exceptions or []
        self.module_name = module_name
        self.types = {}

    def __getattr__(self, name):

        class_path = '%s.%s' % (self.module_name, name)

        if name == '__all__':
            return self.exceptions.keys()

        if name == '__name__':
            return self.module_name

        if name not in self.exceptions:
            raise AttributeError("pyception has no attribute '%s'" % name)

        if class_path in self.types:
            return self.types[class_path]

        klass = self._create(name)
        self.types[class_path] = klass

        return self.types[class_path]

    def _create(self, name):

        base, doc = self.exceptions[name]
        properties = {'__doc__': doc,
                      '__module__': self.module_name}

        inheritance = (base, )
        return type(name, inheritance, properties)

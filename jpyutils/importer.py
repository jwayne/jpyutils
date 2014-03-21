import os


def list_modules(dirname):
    """
    """
    dirname = os.path.abspath(dirname)
    names = []
    for root, _, files in os.walk(dirname):
        for file in files:
            if file.endswith('.py') and file == '__init__.py':
                name = os.path.join(root, file)[len(dirname)+1:].replace('/','.')
                names.append(name[:-3])
    return sorted(names)


def get_module(parent, name):
    """
    """
    try:
        module = __import__("%s.%s" % (parent, name), fromlist=['x'])
    except (ImportError, AttributeError), e:
        raise ImportError("%s: %s.%s does not exist." % (e, parent, name))
    return module


def get_module_cls(parent, name):
    """
    Get the appropriate class from the module `parent`.`name`.
    If `name` is 'your_module', then the class 'your_module.YourModule'
    will be returned.
      >>> cls = get_module_cls('your_lib', 'your_module')
      >>> cls.__module__
      your_lib.your_module
      >>> cls.__name__
      YourModule
    """
    try:
        module = __import__("%s.%s" % (parent, name), fromlist=['x'])
        module_clsname = "".join(s.capitalize() for s in name.split('.')[-1].split('_'))
        module_cls = getattr(module, module_clsname)
    except (ImportError, AttributeError), e:
        raise ImportError("%s: %s.%s.%s does not exist." % (e, parent, name, module_clsname))
    return module_cls


def get_module_obj(parent, name, *args, **kwargs):
    """
    Instantiate the appropriate object from the module `parent`.`name`.
    If `name` is 'your_module', then this will return an object of
    class 'your_module.YourModule' instantiated with `args` and `kwargs`.
    """
    module_cls = get_module_cls(name)
    module_obj = module_cls(*args, **kwargs)
    return module_obj

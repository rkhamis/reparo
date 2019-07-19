import lazy_import 
import os
import importlib
import jumpscale
import pkgutil


__all__ = []

loaded = False

import sys
import importlib.util

def lazy(fullname):
  try:
    return sys.modules[fullname]
  except KeyError:
    spec = importlib.util.find_spec(fullname)
    module = importlib.util.module_from_spec(spec)
    loader = importlib.util.LazyLoader(spec.loader)
    # Make module with proper locking and get it inserted into sys.modules.
    loader.exec_module(module)
    return module

def load():
    global loaded
    if loaded:
        return 
    print(jumpscale.__path__)
    for jsnamespace in jumpscale.__path__:
        # print("js namespace: ", jsnamespace)
        for root, dirs, files in os.walk(jsnamespace):
            for d in dirs:
                if d == "__pycache__":
                    continue
                if os.path.basename(root) == "jumpscale":
                    continue
                # print("root: {} d: {}".format(root, d))
                rootbase = os.path.basename(root)
                pkgname = d
                importedpkgstr = "jumpscale.{}.{}".format(rootbase, pkgname)
                __all__.append(importedpkgstr)
                print("import: ", importedpkgstr)
                globals()[importedpkgstr] = lazy_import.lazy_module(importedpkgstr)

    loaded = True

    print([x for x in globals() if "jumpscale." in x])

load()

class J:
    def __getattr__(self, name):
        return getattr(jumpscale, name)

j = J()

for m in [x for x in globals() if "jumpscale." in x]:
    parts = m.split(".")[1:]
    obj = jumpscale
    while parts:
        p = parts.pop(0)
        obj = getattr(obj, p)
        print(obj)
    try:
        for attr in dir(obj):
            try:
                print("getting attr {} from obj {}".format(attr, obj))
                getattr(obj, attr)
            except Exception:
                pass
    except:
        print("can't dir object: ", obj)            


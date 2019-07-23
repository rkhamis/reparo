
A global j object for easy access to components and functionalities (e.g. god object anti-pattern).

* Should allow auto-completions (without the need to evaluate!)
* Easy to register objects/components.

## Use modules

Utilize code structure to get the idea of a global j object, by simply arranging modules like:

```
jumpscale
  mod
    submod
      impl.py
```


impl.py

```

class CoreImpl:
  ....
  
  
core = CoreImpl()
```


Accessing from other places

```
import jumpscale as j

j.mod.submod.impl.core
```

Other principles like state management need to be discussed (also make sure it would cover actual jumpscale usescaes).


```toml
@url = myschema.user

id = 0 (I)
name = "defaultname" (S)
emails = (LO) # myschema.email


@url = myschema.email

email = "default@gmail.com" (S)
```

Investigate usage of dataclasses as better alternative for schemas and you will get static typing gurantees in our code instead of manually parsing/type checking toml data.


```python

@dataclass
class Email:
    email : str


@dataclass
class User:
    id: int
    name: str
    emails: List[Email]


    def to_capnp(self): 
        pass

    def from_capnp(self):
        pass

```
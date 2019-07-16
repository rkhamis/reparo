from jumpscale.clients.base import SecureClient


class Github(SecureClient):
    def __init__(self, instance_name='myinstance'):
        self.instance_name = instance_name
        super().__init__(self)

if __name__ == "__main__":
    g = Github('xmon')
    print(g.config.data)
    g.config.data = {"a": "1", "__pass": "abce"}

    print(g.config.data)

    gogs = Gogs('main')
    print(gogs.config.data)
    gogs.config.data = {"user":"ahmed", "__tok":"ghijk"}
    print(gogs.config.data)
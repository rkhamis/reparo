class Gogs:
    pass


def get_gogs(username, password):
    import jumpscale
    jumpscale.tools.sync.sync()
    print("getting gogs client with {} {}".format(username, password))
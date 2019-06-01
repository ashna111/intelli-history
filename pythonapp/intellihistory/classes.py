


class SessionUrl(object):
    def __init__(self, url, title):
        self.url = url
        self.title = title

    def to_dict(self):
        return self.to_dict()

    def __repr__(self):
        return(u'SessionUrl(url={}, title={})'.format(self.url, self.title))


class UserSession(object):
    def __init__(self, id, urls=[]):
        self.id = id
        self.urls = urls

    def __repr__(self):
        return(u'UserSession(id={}, urls={})'.format(self.id, self.urls))
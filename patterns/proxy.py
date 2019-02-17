class SubjectInterface:

    def request(self):
        pass


class Proxy(SubjectInterface):

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy may be doing something, like controlling request access")
        self._real_subject.request()


class RealSubject(SubjectInterface):

    def request(self):
        print("The real thing is dealing with the request")


if __name__ == '__main__':
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    proxy.request()

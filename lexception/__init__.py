# -*- coding: utf-8 -*-


class BaseError(Exception):
    def __init__(self, code=0, msg='', **kwargs):
        self.code = code
        self.msg = msg
        self.kwargs = kwargs

    def __str__(self):
        return 'Error Type:[%s], Error Codo:[%d], %s, %s' % (self.__class__.__name__, self.code, self.msg, str(self.kwargs))

    def __repr__(self):
        return self.__str__(self)


if __name__ == '__main__':
    class E(BaseError):
        pass
    e = E(*(32, '31231'), ds=2,das=1)
    raise e
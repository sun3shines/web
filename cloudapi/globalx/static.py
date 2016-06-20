# -*- coding: utf-8 -*-

#from cloudlib.globalx.config import API_CLOUD_PLATFORM_HOST,API_CLOUD_PLATFORM_PORT,API_HTTP_TIMEOUT
#
#CLOUD_PLATFORM_HOST = API_CLOUD_PLATFORM_HOST
#CLOUD_PLATFORM_PORT = API_CLOUD_PLATFORM_PORT
#
#HTTP_TIMEOUT = API_HTTP_TIMEOUT

CLOUD_PLATFORM_HOST = '127.0.0.1'
CLOUD_PLATFORM_PORT = 7012

HTTP_TIMEOUT = 30

X_ADMIN_TOKEN=None




class Config(object):
    def __init__(self, *args, **kwargs):
        self._config = dict(*args, **kwargs)
        self._cb_config = {}    # to store config whose value is calculated from a callback

    def __getitem__(self, key):
        if self._config.has_key(key):
            return self._config[key]
        else:
            return self._cb_config[key]()

    def __setitem__(self, key, value):
        self._cb_config.pop(key, None)
        self._config[key] = value

    def __delitem__(self, key):
        self._config.pop(key, None)
        self._cb_config.pop(key, None)

    def __getattr__(self, key):
        return self.__getitem__(key)

    def set_config(self, **kwargs):
        #self._config.update(kwargs)
        for key, value in kwargs.iteritems():
            self._config[key] = value
            self._cb_config.pop(key, None)

    def set_callback_config(self, **kwargs):
        """
            the only interface to set a callback config
        """
        #self._cb_config.update(kwargs)
        for key, value_cb in kwargs.iteritems():
            assert callable(value_cb)
            self._config.pop(key, None)
            self._cb_config[key] = value_cb



config = Config(
    CLOUD_PLATFORM_HOST='127.0.0.1',
    CLOUD_PLATFORM_PORT=7012,
    HTTP_TIMEOUT=30,
    X_ADMIN_TOKEN=None
)

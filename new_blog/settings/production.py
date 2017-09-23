from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

SECRET_KEY = '^k$@uscev^^vx1f3k)b-nwu8gu^y7fg&r$ns3xhwj)dd%%^s4e'

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('cityblack1','cityblack2@sina.com'),
)


#非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

EMAIL_SUBJECT_PREFIX = 'cityblack1' #为邮件标题的前缀,默认是'[django]'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'cityblack2@sina.com'
EMAIL_HOST_PASSWORD = 'suyue123'
EMAIL_USE_TLS = False
EMAIL_FROM = 'cityblack2@sina.com'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {#日志格式
       'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {#过滤器
    },
    'handlers': {#处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'debug': {#输出到文件
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log",'debug.log'),#日志输出文件
            'maxBytes':1024*1024*5,#文件大小
            'backupCount': 5,#备份份数
            'formatter':'standard',#使用哪种formatters日志格式
        },
        'console':{#输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {#logging管理器
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


try:
    from .local import *
except ImportError:
    pass

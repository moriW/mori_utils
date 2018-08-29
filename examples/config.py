#!/usr/bin/env python
"""
@author: Mori
@contact: moridisa@moridisa.com
@file: config
@time: 2018/8/29 10:37 AM
@desc: Code By Mori
"""

from mori_utils import *

# use this to read config
print(read_config('test'))

# redirect config path
load_config('that_config/')

# generator a logger
logger = gen_logger(__name__)
logger.info('')
logger.warning('')
logger.error('')

# generator a mail handler for logger
mail_handler = MailHandler(read_config('log_by_mail'))
logger.addHandler(mail_handler)

# if read some config did not exist
try:
    print(read_config('config'))
except ConfigNoFound as e:
    print(e)

# if some config parameter not in config
try:
    print(get_zookeeper_host('test'))
except AttributeNotFound as e:
    print(e)

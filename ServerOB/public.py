import logging
from functools import wraps


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)
log_info = logging.info


def log_printer(_message):
    def m_decorator(func):
        @wraps(func)
        def call_it(*args, **kwargs):
            log_info(_message)
            _result = func(*args, **kwargs)
            return _result
        return call_it
    return m_decorator

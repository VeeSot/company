import logging
from functools import lru_cache

from company.models import Branch


@lru_cache()
def get_branch_facade_image_url_prefix():
    try:
        storage = Branch.facade_image.field.storage
        url = f'{storage.url_protocol}//'
        url += f'{storage.custom_domain}/'
        url += f'{storage.location}/'
    except Exception as e:
        url = ''
        logging.exception(e)
    return url

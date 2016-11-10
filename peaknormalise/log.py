"""Logging functionality for peaknormalise."""

import logging


log = logging.getLogger('peaknormalise')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s %(message)s'))
log.addHandler(handler)
log.setLevel(logging.DEBUG)

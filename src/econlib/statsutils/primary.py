import logging
import attrs

log = logging.getLogger(__name__) 

def get_primary_stats(ccy):
    log.info("Running Primary Stats for Fiat %s", ccy)
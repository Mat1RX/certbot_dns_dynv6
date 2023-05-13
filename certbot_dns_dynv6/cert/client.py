from certbot import errors
from certbot.plugins import dns_common

from certbot_dns_dynv6.dynv6.client import DynV6


class Authenticator(dns_common.DNSAuthenticator):
    """
    Authenticator class to handle dns-01 challenge for DynV6 domains.
    """

    description = "Obtain certificates using a DNS TXT record for DynV6 domains"

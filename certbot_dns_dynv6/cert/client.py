from certbot.plugins import dns_common

from certbot_dns_dynv6.dynv6.client import DynV6


class Authenticator(dns_common.DNSAuthenticator):
    """
    Authenticator class to handle dns-01 challenge for DynV6 domains.
    """

    description = "Obtain certificates using a DNS TXT record for DynV6 domains"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):
        super(Authenticator, cls).add_parser_arguments(
            add, default_propagation_seconds=60
        )
        add("credentials", help="DynV6 credentials INI file.")

    def more_info(self):
        return (
            "This plugin configures a DNS TXT record to respond to a dns-01 challenge using "
            + "the DynV6 API."
        )

    def _setup_credentials(self):
        self.credentials = self._configure_credentials(
            "credentials",
            "DynV6 credentials INI file",
            {
                "api_token": "DynV6 API Token from 'https://dynv6.com/keys'",
            },
        )

    def _perform(self, domain, validation_name, validation):
        self.api = DynV6(self.credentials.conf("api_token"))
        self.zone_details = self.api.get_zone_details_by_name(domain)
        self.record = self.api.add_txt_record(self.zone_details['id'], "_acme-challenge", validation)

    def _cleanup(self, domain, validation_name, validation):
        self.api.del_record(zone_id=self.zone_details['id'], record_id=self.record['id'])

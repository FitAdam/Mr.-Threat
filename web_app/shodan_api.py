import shodan

import os


class Shodan_API:
    """The class is used to check the IP with Shodan"""

    def __init__(self, the_ip):
        self.the_ip = the_ip
        self.api = shodan.Shodan(os.getenv("SHODAN_API_KEY"))
        self.host = self.check_ip_with_shodan()

    def check_ip_with_shodan(self):

        try:
            # Lookup the host
            host = self.api.host(self.the_ip)
            return host
        except shodan.APIError as error:
            pass
        else:
            pass

    def get_general_info(self):
            if self.host:
                    # Print general info
                    general_info = """
                                IP: {}
                                Organization: {}
                                Operating System: {}
                        """.format(self.host['ip_str'], self.host.get('org', 'n/a'), self.host.get('os', 'n/a'))
                    return general_info.replace("\x00", "\uFFFD")
            else:
                return 'No data available'

    def get_all_banners(self):
            if self.host:
                all_banners = ''
                for item in self.host['data']:
                        all_banners += """
                                        Port: {}
                                        Banner: {}

                                """.format(item['port'], item['data'])
                return all_banners.replace("\x00", "\uFFFD")
            else:
                return 'No data available'

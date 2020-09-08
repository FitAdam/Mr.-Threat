import shodan

from .keys import SHODAN_API_KEY


class Shodan_API:
        """The class is used to check the IP with Shodan"""
        def __init__(self, the_ip):
                self.the_ip = the_ip
                self.api = shodan.Shodan(SHODAN_API_KEY)
                self.host = self.check_ip_with_shodan()


        def check_ip_with_shodan(self):
                # Lookup the host
                host = self.api.host(self.the_ip)
                return host

        def get_general_info(self):
                # Print general info
                general_info = """
                        IP: {}
                        Organization: {}
                        Operating System: {}
                """.format(self.host['ip_str'], self.host.get('org', 'n/a'), self.host.get('os', 'n/a'))
                return general_info

        def get_all_banners(self):
                all_banners = ''
                for item in self.host['data']:
                        all_banners+="""
                                Port: {}
                                Banner: {}

                        """.format(item['port'], item['data'])
                return all_banners



host = Shodan_API("118.24.149.248")

print(host.get_general_info())
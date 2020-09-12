import ipaddress


def check_if_ip_is_private(the_ip):
    return ipaddress.ip_address(the_ip).is_private


print(check_if_ip_is_private('127.0.0.1'))



import re

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    boolean = False
    if octet.isdigit():
        octet = int(octet)
        if octet <= 255:
            boolean = True
    return boolean

def is_valid_IPv4(ip):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    if not ip:
        return False 
    boolean = False
    split_ipv4 = ip.split('.')
    if len(split_ipv4) == 4:
        for numbers in split_ipv4:
            print(numbers)
            boolean = is_valid_IPv4_octet(numbers)
            if boolean == False:
                return boolean
    return boolean
    
def is_valid_IPv6_hextet(hextet):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    if len(hextet) > 4:
        return False
    if len(hextet) == 0:
        return False
    stripped_hextet = hextet.lstrip('0')
    count_zeros = len(hextet) - len(stripped_hextet)
    if len(stripped_hextet) + count_zeros > 4:
        return False
    elif len(stripped_hextet) == 0:
        return True
    else:
        idx = len(stripped_hextet)
        pattern = rf'^([0-9a-fA-F]{{1,{idx}}}$)'
        if re.match(pattern, stripped_hextet):
            return True
    return False

def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    if not ip:
        return False 
    boolean = False
    split_ipv6 = ip.split(':')
    if len(split_ipv6) == 8:
        for numbers in split_ipv6:
            boolean = is_valid_IPv6_hextet(numbers)
            if boolean == False:
                return boolean
    return boolean

def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    if is_valid_IPv4(ip) or is_valid_IPv6(ip):
        return True
    else:
        return False

# You should look at task/test.py and extend the test suite we provided!

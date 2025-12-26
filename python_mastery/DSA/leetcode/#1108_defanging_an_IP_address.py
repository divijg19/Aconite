# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/

def defangIPaddr(address):
    result = []
    for ch in address:
        if ch == ".":
            result.append("[.]")
        else:
            result.append(ch)
    return "".join(result)

# def defangIPaddr(address):
#     return address.replace('.', '[.]')
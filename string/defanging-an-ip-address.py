class Solution:
    def defangIPaddr(self, address: str) -> str:
        l1 = address.split(".")
        new_address = "[.]".join(l1)
        return new_address
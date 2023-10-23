class My_list(list):
    def __sub__(self, other):
        result = My_list()
        for item in self:
            try:
                if item not in other:
                    result.append(item)
            except TypeError:
                result.append(item)
        return result

    def __truediv__(self, divisor):
        result = My_list()
        for item in self:
            try:
                result.append(item / divisor)
            except TypeError:
                result.append(item)
        return result

    def __repr__(self):
        return f"My_list({super().__repr__()})"


l1 = My_list([1, 2, 3])
l2 = My_list([3, 4, 5])
l3 = l2 - l1
l4 = l1 - l2
print(l1 / 5)
print(l3)
print(l4)

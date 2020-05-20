print("good morning")
print("Naveen is a good boy")
if 5 > 2:
    print("Five greater than two")

    # this is a comment
    """
    testing
    """
    print("good evening")
    x = 4
    # is the same as
    x = 5
    print(type(x))

x = frozenset(("apple", "banana", "cherry"))
print(x)
print(type(x))
x = bytes(5)
print(x)
x = dict(name="John", age=36)
print(x)


def remove_duplicate(lista) -> object:
    lista2 = []
    if lista:
        for item in lista:
            if item not in lista2:
                lista2.append(item)
            else:
                #print("lista" + lista2)
                return lista
            #print("lista" + lista2)
            return lista2


print(x)
remove_duplicate([2,3,4,3])
print(x)

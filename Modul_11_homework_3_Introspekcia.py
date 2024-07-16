import inspect

def introspection_info(obj):
    print({"Type": type(obj)})
    print()
    print({"Attributes": dir(obj)})
    print()
    print({"Methods": inspect.getmembers(obj)})
    print()
    print({"Module": inspect.getmodule(obj)})
    print()
    print({"Isinstance": isinstance(obj, list)})
    print()
    print({"Id": id(obj)})

number_info = introspection_info(42)
print(number_info)
import types


def fn():
    pass


print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
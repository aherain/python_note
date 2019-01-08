import pkgutil
py_code = pkgutil.get_data("test", 'nihao.html')

print(py_code)
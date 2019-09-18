import sys
class DataItem(object):
    __slots__ = ['name', 'age', 'address'] #可大大的减少内存开销。
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


d1 = DataItem('Alex', 42, '--')
print("sys.getsizeof(d1)", sys.getsizeof(d1))

d2 = DataItem('Boris', 24, 'In the middle of nowhere')
print("sys.getsizeof(d2)", sys.getsizeof(d2))


def dump(obj):
    for attr in dir(obj):
        print(" obj.%s = %s" % (attr, getattr(obj, attr)))

dump(d1)


def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(v, seen) for v in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

d1 = DataItem('Alex', 42, '--')
print("get_size(d1):", get_size(d1))

d2 = DataItem("Boris", 24, "In the middle of nowhere")

print("get_size(d2):", get_size(d2))

# 列表解析生成整个列表，会对大量数据的迭代产生负面作用。而生成器表达式不会。
# 生成器表达式不会创建一个列表，相反返回一个生成器，在需要的时候生成具体值（延迟的），
# 这种方式对内存友好。

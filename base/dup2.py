import os

f = open('txt', 'w')

print('cxxxxxx',f.fileno())
f.close()

fn = open('txtp','w')

print('vvvvvv', fn.fileno())

# os.dup2(f.fileno(), 1)
# print('nihao1111')
# print('hhhh,ddd')
# f.close()


# import fileinput
# with fileinput.input('/etc/passwd') as f:
#     for line in f:
#         print(f.filename(), f.lineno(), line, end)
#
# import shutil
# shutil.unpack_archive('Python-3.3.0.tgz')
# shutil.make_archive('py33', 'zip', 'Python-3.3.0')
#
# import signal
# import resource
# import os
#
#
# def time_exceeded(signo, frame):
#     print("Time's up!")
#     raise SystemExit(1)
#
#
# def set_max_runtime(seconds):
#     # Install the signal handler and set a resource limit
#     soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
#     resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
#     signal.signal(signal.SIGXCPU, time_exceeded)

#
# if __name__ == '__main__':
#     set_max_runtime(15)
#     while True:
#         pass




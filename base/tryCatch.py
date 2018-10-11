import time
class Test(object):
    def dothis(self):
        while True:
            try:
                a = 100 / 0
                time.sleep(2)

            # except ZeroDivisionError:
            #     time.sleep(3)
            #     print('有錯誤')
            except Exception:
                print('www')
        return

if __name__ == '__main__':
    ts = Test()
    ts.dothis()
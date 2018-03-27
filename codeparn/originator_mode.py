class Originator:
    def __init__(self):
        self.state = ""
    def Show(self):
        print(self.state)
    def CreateMemo(self):
        return Memo(self.state)
    def SetMemo(self,memo):
        self.state = memo.state

class Memo:
    state= ""
    def __init__(self,ts):
        self.state = ts

class Caretaker:
    memo = ""

if __name__ == "__main__":
    on = Originator()
    on.state = "on"
    on.Show()
    c = Caretaker()
    c.memo=on.CreateMemo()
    on.state="off"
    on.Show()
    on.SetMemo(c.memo)
    on.Show()


# curl --location-trusted -utatooine2:tatooine2.Midas.W6.huayingjuhe.com -T add2014wan.csv "http://127.0.0.1:8030/api/Bestine/stt_boxoffice/_load?label=boxoffice_dump2014_2951&column_separator=,"
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class Robot:
    """This class knows how to perform the operations associated with carrying out a 
    request. 
    """

    def Move(self, direction, step):
        print("I am robot,now " + direction + " by:%d step" % step)
        pass


class Command(object):
    """This class declares an interface for executing an operation. 
    """
    m_Robot = Robot()

    def __init__(self, direction="None", step="None"):
        self.direction = direction
        self.step = step
        pass

    def Execute():
        pass


class GoAhead(Command):
    """This class (a) defines a binding between a Receiver object and an action, and 
    (b) implements Execute by invoking the corresponding operation(s) on Receiver. 
    """

    def __init__(self, direction='GoAhead', step=1):
        super(GoAhead, self).__init__(direction, step)
        pass

    def Execute(self):
        # receiver->Action();
        Command.m_Robot.Move(self.direction, self.step)

        pass


class GoBack(Command):
    """This class (a) defines a binding between a Receiver object and an action, and 
    (b) implements Execute by invoking the corresponding operation(s) on Receiver. 
    """

    def __init__(self, direction='GoBack', step=1):
        super(GoBack, self).__init__(direction, step)
        pass

    def Execute(self):
        # receiver->Action();
        Command.m_Robot.Move(self.direction, self.step)

        pass


class GoLeft(Command):
    """This class (a) defines a binding between a Receiver object and an action, and 
    (b) implements Execute by invoking the corresponding operation(s) on Receiver. 
    """

    def __init__(self, direction='GoLeft', step=1):
        super(GoLeft, self).__init__(direction, step)
        pass

    def Execute(self):
        # receiver->Action();
        Command.m_Robot.Move(self.direction, self.step)

        pass


class GoRight(Command):
    """This class (a) defines a binding between a Receiver object and an action, and 
    (b) implements Execute by invoking the corresponding operation(s) on Receiver. 
    """

    def __init__(self, direction='GoRight', step=1):
        super(GoRight, self).__init__(direction, step)
        pass

    def Execute(self):
        # receiver->Action();
        Command.m_Robot.Move(self.direction, self.step)

        pass


class Controller(object):
    """This class asks the command to carry out the request. 
    """
    m_Command = Command()

    def __init__(self):
        self.ls = list()
        pass

    def AddOperation(self, command):
        self.ls.append(command)
        pass

    def Execute(self):
        for i in range(len(self.ls)):
            item = self.ls.pop(0)
            item.Execute()

        pass


# 客户端
class Client:
    """This class creates a ConcreteCommand object and sets its receiver. 
    """

    m_Controller = Controller()

    m_Controller.AddOperation(GoAhead(step=12))
    m_Controller.AddOperation(GoBack(step=4))
    m_Controller.AddOperation(GoLeft(step=3))
    m_Controller.AddOperation(GoRight(step=5))
    m_Controller.Execute()

    print("\n")
    m_Controller.AddOperation(GoAhead(step=20))
    m_Controller.AddOperation(GoBack(step=44))
    m_Controller.AddOperation(GoLeft(step=34))
    m_Controller.AddOperation(GoRight(step=50))
    m_Controller.Execute()
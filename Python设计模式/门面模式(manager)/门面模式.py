# https://www.cnblogs.com/lizhitai/p/4464971.html

class LoadMemory:
    def memory(self):
        print('memory init')


class LoadCpu:
    def cpu(self):
        print('cpu init')


class LoadDisk:
    def disk(self):
        print('disk init')


class ComputerManager:
    def __init__(self):
        self.cpu = LoadCpu()
        self.disk = LoadDisk()
        self.memory = LoadMemory()

    def start(self):
        self.cpu.cpu()
        self.disk.disk()
        self.memory.memory()


class You:
    def operate(self):
        computer = ComputerManager()
        computer.start()


if __name__ == '__main__':
    """
    思想  将 不同的类进行统一   一块调用
    """
    you = You()
    you.operate()

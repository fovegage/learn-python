class Del:
    def __del__(self):
        print(1)


"""

相当于 析构方法   注意和 __exit__  这个用于  as 句柄的 析构
推出的时候自动调用  可以清理 gc 等
"""

if __name__ == '__main__':
    del_ = Del()

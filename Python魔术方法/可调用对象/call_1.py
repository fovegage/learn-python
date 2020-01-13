class Text:
    print(1)
    a = 1
    def __call__(self, *args, **kwargs):
        print('call')


class Hello:
    Text()


Hello()
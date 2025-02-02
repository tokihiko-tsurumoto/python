class C:
    # 暗黙の第一引数としてクラスオブジェクトが渡される
    @classmethod
    def f(cls, arg1, arg2):
        print("classmethod:", cls, arg1, arg2)


C.f(1, 2)
C().f(1, 2)

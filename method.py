from dataclasses import dataclass
from typing import ClassVar


@dataclass
class C:
    # インスタンス変数
    arg1: int
    arg2: int

    # クラス変数
    arg3: ClassVar[int] = 3

    # 暗黙の第一引数としてクラスオブジェクトが渡される
    @classmethod
    def f_classmethod(cls, arg4):
        print("classmethod:", cls, cls.arg3, arg4)

    # 暗黙の第一引数を受け取らない
    @staticmethod
    def f_staticmethod(arg4):
        print("staticmethod:", C.arg3, arg4)

    # 暗黙の第一引数としてインスタンスオブジェクトが渡される
    def f_instancemethod(self, arg4):
        # self.__class__.arg3でもクラス変数にアクセスできる
        print("instance method:", self, self.arg1, self.arg2, C.arg3, arg4)


# クラスメソッドを呼び出す
C.f_classmethod(4)
C(1, 2).f_classmethod(4)

# スタティックメソッドを呼び出す
C.f_staticmethod(4)
C(1, 2).f_staticmethod(4)

# インスタンスメソッドを呼び出す
c = C(1, 2)
c.f_instancemethod(4)

C(1, 2).f_instancemethod(4)

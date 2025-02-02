# dataclassesモジュールは、__init__()などのスペシャルメソッドを自動で生成するデコレータを提供する
from dataclasses import dataclass
from typing import ClassVar


# frozen=Trueにすることでインスタンス変数を変更できないようにできる
# インスタンス変数を変更しようとするとオーバーライドされた__setattr__()がFrozenInstanceErrorを送出する
# 自動生成されるコンストラクタの中では、オーバーライドされた__setattr__()ではなく、object.__setattr__()が使われる
@dataclass(frozen=True)
class C:
    # インスタンス変数
    i: int = 0
    # クラス変数
    j: ClassVar[int] = 0
    # クラス変数
    k = 0

    def show(self) -> str:
        return f"i: {self.i}, j: {self.j}, k: {self.k}"


# インスタンス変数であるiに1を代入してインスタンスを生成
c = C(1)

# frozen=Trueにしている場合、以下のようにインスタンス変数は変更できない
# c.i = 2
# 例外として、object.__setattr__()を使うことで変更できる（コンストラクタでもobject.__setattr__()が使われている）
object.__setattr__(c, "i", 2)


# C.jに代入することでクラス変数を変更できる
# c.jやC().jに代入した場合、インスタンス変数として新たにjが生成される（この例ではfrozen=Trueにしているので代入できない）
C.j = 1


print(c.show())

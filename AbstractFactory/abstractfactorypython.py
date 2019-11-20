#インスタンスの生成を専門に行うクラスを用意することで、間違いないように（複雑な）オブジェクトをつくる
#クラス内クラスを作成してPythonらしく書く
'''
ピザは生地、ソース、トッピングからできます。
工場Aでは、生地に小麦、ソースにトマト、トッピングにコーンを使用します。
工場Bでは、生地に米粉、ソースにバジル、トッピングにチーズを使用します。
すべての素材に確認のためのメソッド（check）をもたせます。
'''

amount_dict = {"high": 1.2, "normal": 1.0, "low": 0.8}

def main():

  pizza1 = make_pizza(PizzaFactoryA,"high")
  pizza1.check_pizza()

  print("-----")

  pizza2 = make_pizza(PizzaFactoryB, "normal")
  pizza2.check_pizza()


def make_pizza(PizzaFactory, amount_str):
  #受け取ったピザファクトリークラスをインスタンス化
  pizza = PizzaFactory()
  amount = amount_dict[amount_str] #金額取得
  pizza.pizza_materials = []
  pizza.pizza_materials.append(pizza.add_dough(amount))
  pizza.pizza_materials.append(pizza.add_source(amount))
  pizza.pizza_materials.append(pizza.add_topping(amount))

  return pizza

#工場Aのクラス
class PizzaFactoryA:
  def __init__(self):
    pass

  def check_pizza(self):
    for pizza_material in self.pizza_materials:
      pizza_material.check()

  #クラスメソッドにしておくとインスタンス化しなくてもメソッドが使える。クラスメソッドの場合はselfじゃなくてClassが第一引数になる
  @classmethod
  def add_dough(Class, amount=1):
    return Class.WheatDough(amount)

  @classmethod
  def add_source(Class, amount=1):
    return Class.TomatoSource(amount)

  @classmethod
  def add_topping(Class,amount=1):
    return Class.CoanTopping(amount)

  #クラス内クラスとして生地、材料、トッピングを定義する
  class WheatDough:
    def __init__(self, amount=1):
      self.amount = amount
    
    def check(self):
      print("Wheat(amount: {})".format(self.amount))

  class TomatoSource:
    def __init__(self, amount=1):
      self.amount = amount

    def check(self):
      print("Tomato(amount: {})".format(self.amount))

  class CoanTopping:
    def __init__(self, amount=1):
      self.amount = amount

    def check(self):
      print("Coan(amount: {})".format(self.amount))

class PizzaFactoryB:
  def __init__(self):
    pass

  def check_pizza(self):
    for pizza_material in self.pizza_materials:
      pizza_material.check()

  @classmethod
  def add_dough(Class, amount=1):
    return Class.RiceFlourDough(amount)

  def add_source(Class,amount=1):
    return Class.BasilSource(amount)

  def add_topping(Class,amount=1):
    return Class.CheeseTopping(amount)

  class RiceFlourDough:
    def __init__(self, amount=1):
      self.amount = amount

    def check(self):
      print("FlourDough(amount: {})".format(self.amount))

  class BasilSource:
    def __init__(self,amount=1):
      self.amount = amount
    
    def check(self):
      print("Tomato(amount: {})".format(self.amount))

  class CheeseTopping:
    def __init__(self,amount=1):
      self.amount = amount
    def check(self):
      print("Cheese(amount: {})".format(self.amount))

if __name__ == "__main__":
  main()
    

    
    

  

  
  

# Python玩转设计模式（一）：策略模式

> 『策略模式』定义了算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化独立于使用算法的客户。

## 模拟鸭子

假如让你设计一个模拟鸭子的游戏，鸭子的种类繁多，每种鸭子都会游泳和呱呱叫，你会如何设计？我想，大部分人和我一样，首先想到的是使用继承。

![1555421796700](C:\Users\ethan\Pictures\ProcessOn\strategy\模拟鸭子.png)

这确实是一个不错的设计，使用了标准的OO（面向对象）技术，设计了一个鸭子基类，并让各种鸭子继承它，每种鸭子都会quack和swim，并实现各自的display方法。但是，软件开发有一个不变的真理，就是**改变**。一款软件，无论一开始设计得多好，过一阵子后，都需要迭代和更新。驱动改变的因素有很多，比如功能优化、新功能添加、软件兼容等等。

让我们回到模拟鸭子的游戏，用户觉得不过瘾，还想让鸭子能飞。嘿，能飞还不简单，这样不就行了：

![1555422244371](C:\Users\ethan\Pictures\ProcessOn\strategy\模拟鸭子(1).png)

我们忽略了一件事，并非所有鸭子都会飞。假设现在添加一个子类叫RubberDuck(橡皮鸭)，也继承自Duck，就会出现不符合逻辑的情况（会飞的橡皮鸭）。如果在RubberDuck里覆盖掉fly()方法呢？像这样：

```python
class RubberDuck(Duck):
    def display():
        print('黄色的橡皮鸭，喜欢在浴缸里游泳')
    
    def quack():
        print('吱吱吱') # 覆盖quack，因为橡皮鸭的叫声与正常鸭子的叫声有所不同
    
    def fly():
        pass # 覆盖fly，因为橡皮鸭不会飞，所以调用时啥也不干
```

这只能解决目前的问题，如果以后有个ModelDuck(模型鸭)，不会飞也不会叫；或者有个虽然会飞，但叫声跟橡皮鸭一样的类，又该怎么办？如果都用覆盖，代码就不能复用，以后维护起来就是恶梦。

## 解决方案

通过上面的例子，我们发现在基类中加上新的行为，会使得某些子类也具有这个不恰当的行为，如果在子类中覆盖该行为，又会导致代码重复且不能复用的情况。针对此情况，《Head First设计模式》给我们提供了解决方案：

![1555592204828](C:\Users\ethan\AppData\Roaming\Typora\typora-user-images\1555592204828.png)

从上图中我们看到，飞行和呱呱叫的行为都被抽象成了接口，再定义不同的飞行行为类和呱呱叫行为类来实现这个接口。在Duck基类中定义了两种行为的属性，并增加了performQuack、perfromFly、setFlyBehavior、setQuackBehavior四个方法。这样一来，Duck的子类只要在初始化时声明自己的行为就行了。而且可以调用setFlyBehavior和setQuackBehavior方法来动态改变行为。下面，我们用Python代码实现一下，看看这么做到底能给我们带来什么好处。

## 代码实现

### 飞行行为

```python
class FlyBehavior(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with my beautiful wings.")

class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly.")

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket.")
```



### 呱呱叫行为

```python
class QuackBehavior(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("quack,quack,quack.")

class Squeak(QuackBehavior):
    def quack(self):
        print("squeak,squeak,squeak.")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("silence.")
```

Python中使用抽象类来实现类似Java中的interface接口。`metaclass=ABCMeta`表示该类为抽象类(即接口)，`@abstractmethod`装饰的函数为抽象函数，该函数必须在所有继承了该类的子类中实现。

### 鸭子类
篇幅问题就不在此列出所有Duck子类。
```python
class Duck(metaclass=ABCMeta):
    fly_behavior = None
    quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self,fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self,quack_behavior):
        self.quack_behavior = quack_behavior

    def swim(self):
        print('All ducks float.')

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = fb.FlyWithWings()
        self.quack_behavior = qb.Quack()

    def display(self):
        print("I'm a mallard duck, my head color is Green")
```



### 测试代码

```python
def play_with_mallard_duck():
    mallard_duck = ducks.MallardDuck()
    mallard_duck.display()
    mallard_duck.perform_quack()
    mallard_duck.perform_fly()
 
def play_with_rubber_duck():
    rubber_duck = ducks.RubberDuck()
    rubber_duck.display()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()

def play_with_model_duck():
    model_duck = ducks.ModelDuck()
    model_duck.display()
    model_duck.perform_quack()
    model_duck.perform_fly()
    model_duck.set_fly_behavior(fb.FlyRocketPowered()) #动态设置飞行行为
    model_duck.perform_fly()
```

```python
if __name__ == '__main__':
    play_with_mallard_duck()
    play_with_rubber_duck()
    play_with_model_duck()

'''
运行结果：
-------------------mallard_duck-------------------
I'm a mallard duck, my head color is Green
quack,quack,quack.
I'm flying with my beautiful wings.
--------------------------------------------------

-------------------rubber_duck--------------------
I'm a rubber duck, I like swimming in the tub.
squeak,squeak,squeak.
I can't fly.
--------------------------------------------------

--------------------model_duck--------------------
I'm a model duck, I can do nothing. Try to change my behaviors.
silence.
I can't fly.
I'm flying with a rocket.
--------------------------------------------------
'''

```

### 总结
通过将**容易变化的行为（函数）**抽象为接口，再用一组类去实现，使我们在享受继承好处的同时又能避免继承所带来的缺点。这些行为在被抽象之后，已经完全独立于使用行为的客户（鸭子类）。举个栗子，以后如果你有鸡类或者鸟类，都能直接调用这些飞行行为。这种设计模式就叫做**策略模式**，它遵循了以下几个设计原则：

- **找出应用中可能需要变化之处 ，把它们独立出来，不要和那些不需要变化的代码混在一起。**

  （飞行和呱呱叫都属于需要变化的代码）

- **针对接口编程，而不是针对实现编程。**

  （将飞行和呱呱叫封装为接口）

- **多用组合，少用继承。**

  （飞行和呱呱叫不是由继承而来，而是和适当的行为对象组合而来，将这些行为委托给行为对象代为处理）

本文所有代码已上传至[Github]()。


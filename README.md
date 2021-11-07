# py-functional-chaining

## intro

你是否会对这种代码产生生理不适？

```python
universalSet = set(map(lambda cell: str.strip(cell.value), filter(lambda cell: cell.value != None, list(sheet.columns)[0])))
```

他本可以更优雅：

```python
universalSet = List(sheet.columns)[0] \
      .filter(lambda cell: cell.value != None) \
      .map(lambda cell: str.strip(cell.value)) \
      .toSet()
```

这个项目将为常用内建类型提供包装类，避免使用 Python 难读的函数式编程风格。

## usage

### List

```python
from funcChaining import Type

lst = Type.List([1, 2, 3])

# 函数式方法的链式调用
result = lst.filter(lambda num: num % 2 != 0) \
   .map(lambda num: num * 2) \
   .reduce(lambda total, num: total + num, 0)
print(result)
# > 18

# 函数式方法不会影响实例本身
print(lst)
# > [1, 2, 3, 4, 5]


# 原有修改器方法的链式调用包装
print(lst.append(6).insert(6, 7).pop().remove(6))
# > [1, 2, 3, 4, 5]

print(lst.clear().extend([4, 5, 6]))
# > [4, 5, 6]

print(lst.reverse().sort(key=lambda x: -x))
# > [6, 5, 4]


# 访问器方法
newlst = lst.copy()
print(newlst)
# > [6, 5, 4]

print(lst.index(5))
# > 1

print(lst.count(1))
# > 0


# 可靠地重载了运算符
print(lst + [3, 2, 1])
# > [6, 5, 4, 3, 2, 1]

print([7] + lst)
# > [7, 6, 5, 4, 3, 2, 1]

lst += [0]
print(lst)
# > [7, 6, 5, 4, 3, 2, 1, 0]

lst *= 2
print(lst)
# > [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 0]

print(isinstance((lst * 2), List))
# > True
print(isinstance((2 * lst), List))
# > True
print(isinstance((lst + [1]), List))
# > True
print(isinstance(([1] + lst), List))
# > True
```

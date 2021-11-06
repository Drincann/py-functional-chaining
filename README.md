# py-functional-chaining

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

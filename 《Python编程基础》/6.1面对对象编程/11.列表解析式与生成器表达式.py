列表解析式，一次性输出一个序列：[expr for iter_var in iterable if cond_expr]
例：生成一个list来保护50以内的所有奇数
[i for i in range(50) if i%2]



当序列过长，每次只需要获取一个元素时，当考虑使用生成器表达式
生成器表达式:(expr for iter_var in iterable if cond_expr)


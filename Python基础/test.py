import json
obj = dict(name='小明', age=20)
print(json.dumps(obj, ensure_ascii=False))
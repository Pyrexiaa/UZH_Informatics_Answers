def compress(data):
    keys = tuple(sorted(set(key for d in data for key in d.keys())))
    values = [tuple(d.get(key, None) for key in keys) for d in data]
    result = (keys, values)
    return result

# Example usage:
data = [
    {"a": 1, "b": 2, "c": 3},
    {"a": 4, "c": 6, "b": 5}
]

result = compress(data)
print(result)
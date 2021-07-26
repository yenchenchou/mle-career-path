"""

"""

books = ["Green form", "Green form edition1", "Green form reality", "Cooking book starter", "Cooking book", "Cook your meal edition1"]
res = []
for a in books:
    for b in books:
        if a.startswith(b) and a != b:
            res.append(a)
print(res)
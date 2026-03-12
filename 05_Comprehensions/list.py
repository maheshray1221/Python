# [expresions loop condition]

# example

items = [
    "pencil",
    "pen",
    "table",
    "book",
    "chair"
]

# result = [item for item in items if "pen" in item]

# print(result)


result = [item for item in items if len(item)>5 ]

print(result)
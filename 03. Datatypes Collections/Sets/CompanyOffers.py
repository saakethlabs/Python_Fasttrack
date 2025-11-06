company_x = {"Alice", "Bob", "Charlie"}
company_y = {"Charlie", "David", "Eve"}

exclusive = company_x.symmetric_difference(company_y)
print(exclusive)  # {'Alice', 'Bob', 'David', 'Eve'}

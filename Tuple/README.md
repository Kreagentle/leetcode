# Sum and Product

Write a function that calculates the sum and product of all elements in a tuple of numbers.

```sh
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24
```

# Elementwise Sum

Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

```sh
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
```

# Insert at the Beginning

Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

```sh
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
```
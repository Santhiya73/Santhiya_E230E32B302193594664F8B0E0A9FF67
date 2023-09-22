# 3.1  Write a function called linear_search_product that takes the list of products and a target product name as input.The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found ,or an empty list if the product is not found

def LinearSearchProduct(productlist, targetproduct):
    indices = []

    for index,product in enumerate(productlist):
        if product == targetproduct:
            indices.append(index)
    return indices 

products = ["apple", "banana", "orange", "apple", "grape","apple"]
target = "apple"
result = LinearSearchProduct(products, target)
print(result)
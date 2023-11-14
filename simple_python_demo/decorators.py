def AcessFunc(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(res)
    return wrapper


@AcessFunc
def GetoneProduct(products, index):
    if not index:
        raise NameError
    product = products[index]
    return product


@AcessFunc
def GetAllProducts(products, index, relations):
    relation = relations.get(index)
    if not relation:
        raise NameError
    print(relation)
    return [allProducts for allProducts in products if relation in allProducts]


# * call only one product
GetoneProduct(["Magazine", "Fruits", "Juice"], 2)

# * call all product with the product relation
GetAllProducts(["Banana", "Pineapple", "Apple", "Juice", "Banana", "Mango", "Apple"], "Second", {"First": "Pineapple",
               "Second": "Apple", "Third": "Banana"})

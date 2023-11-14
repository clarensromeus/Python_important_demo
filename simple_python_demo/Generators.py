
# ? when to use lists to print out data in a server ?
# TODO: when perfomance of displaying data is not of too much matter and there's no heavy data load
def list_of_users(lists):
    users = []
    for l in lists:
        users.append(l)
    return users


res = list_of_users(["clarens", "Attilot", "Angelita",
                    "Tamara", "hervelange", "Claudine"])


# TODO: the main advantage using generators is that it does not save or keep data in the computer memory
# TODO: even if the server is loading more than millions of records it takes no delay time to display them
def list_of_users_with_generator(lists):
    for lofusers in lists:
        yield lofusers


res_with_generators = list_of_users_with_generator(
    ["clarens", "Attilot", "Angelita"])

# * testing generators with the next method
# * this method of using generators raise an exception when there's more next call than expected
print("magic method __next__")
print(next(res_with_generators))
print(next(res_with_generators))
print(next(res_with_generators))
print("end display of the magic method")


# TODO: using this strategy to is better to display all data at once with a for loop and raise no exception
for user in res_with_generators:
    print(f"username: {user}")

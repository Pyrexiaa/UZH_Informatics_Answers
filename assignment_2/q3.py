# Change the function below to calculate the total price this
# order. Note that your implementation should work with any
# specific value, so you can't just add up the raw numbers,
# you MUST use the variables passed as parameters.
def get_price(price_cone,
        num_scoops_vanilla, price_per_scoop_vanilla,
        num_scoops_chocolate, price_per_scoop_chocolate):
    # Modify this return statement so that the correct result is returned
    cone_price = price_cone
    vanilla_price = num_scoops_vanilla * price_per_scoop_vanilla
    chocolate_price = num_scoops_chocolate * price_per_scoop_chocolate
    return cone_price + vanilla_price + chocolate_price


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below. You can try entering different values to ensure your
# implementation works correctly.
print(get_price(0.70, 1.00, 1.10, 1, 3))
from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum, difference, and product of the two secret integers
    sum_result = my_int1 + my_int2
    difference_result = my_int1 - my_int2
    product_result = my_int1 * my_int2

    # Conditional operation to check if my_int1 is greater than my_int2
    is_greater = If(my_int1 > my_int2, 1, 0)

    # Compute the average of the two integers
    average_result = (my_int1 + my_int2) / 2

    # Compute the absolute difference
    abs_difference = If(difference_result < 0, -difference_result, difference_result)

    # Return the results as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(product_result, "product_output", party1),
        Output(is_greater, "is_greater_output", party1),
        Output(average_result, "average_output", party1),
        Output(abs_difference, "abs_difference_output", party1)
    ]

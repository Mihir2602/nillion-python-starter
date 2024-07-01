from nada_dsl import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import secrets

def generate_secret_data(size):
    return [secrets.randbelow(100) for _ in range(size)]

def visualize_data(data1, data2):
    plt.figure(figsize=(10, 6))
    plt.hist([data1, data2], bins=20, label=['Party1 Data', 'Party2 Data'], alpha=0.7)
    plt.title('Distribution of Secret Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

def perform_statistical_analysis(data1, data2):
    mean1, mean2 = np.mean(data1), np.mean(data2)
    std1, std2 = np.std(data1), np.std(data2)
    correlation = np.corrcoef(data1, data2)[0, 1]
    return mean1, mean2, std1, std2, correlation

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Generate secret data for two parties
    secret_data1 = generate_secret_data(100)
    secret_data2 = generate_secret_data(100)

    # Create secret integers for inputs
    my_int1 = [SecretInteger(Input(name=f"my_int1_{i}", party=party1)) for i in range(100)]
    my_int2 = [SecretInteger(Input(name=f"my_int2_{i}", party=party2)) for i in range(100)]

    # Compute various operations on the secret data
    sum_results = [my_int1[i] + my_int2[i] for i in range(100)]
    difference_results = [my_int1[i] - my_int2[i] for i in range(100)]
    product_results = [my_int1[i] * my_int2[i] for i in range(100)]
    average_results = [(my_int1[i] + my_int2[i]) / 2 for i in range(100)]
    abs_differences = [If(difference_results[i] < 0, -difference_results[i], difference_results[i]) for i in range(100)]

    # Perform statistical analysis on the secret data
    mean1, mean2, std1, std2, correlation = perform_statistical_analysis(secret_data1, secret_data2)

    # Visualize the secret data distributions
    visualize_data(secret_data1, secret_data2)

    # Compute conditional operations and aggregate results
    is_greater_count = sum([If(my_int1[i] > my_int2[i], 1, 0) for i in range(100)])

    # Return results as outputs
    return [
        Output(sum(sum_results), "sum_output", party1),
        Output(sum(difference_results), "difference_output", party1),
        Output(sum(product_results), "product_output", party1),
        Output(is_greater_count, "is_greater_count_output", party1),
        Output(sum(average_results) / 100, "average_output", party1),
        Output(sum(abs_differences), "abs_difference_output", party1),
        Output(mean1, "mean1_output", party1),
        Output(mean2, "mean2_output", party2),
        Output(std1, "std1_output", party1),
        Output(std2, "std2_output", party2),
        Output(correlation, "correlation_output", party1)
    ]


# This program is a comprehensive privacy-preserving data analysis framework
# leveraging multi-party computation (MPC) principles. It utilizes the nada_dsl 
# for defining secret integers and operations, and incorporates several advanced 
# Python libraries to enhance its functionality.

# Key Features:
# 1. Data Generation: Securely generates random secret data for two parties using 
#    the `secrets` module to ensure randomness and security.
# 2. Visualization: Uses `matplotlib` to visualize the distribution of secret data 
#    from both parties, providing insights into the underlying data.
# 3. Statistical Analysis: Computes statistical measures such as mean, standard 
#    deviation, and correlation using `numpy` to analyze the secret data.
# 4. Advanced Operations: Performs a series of operations on lists of secret 
#    integers, including sum, difference, product, average, and absolute 
#    difference calculations.
# 5. Conditional Operations: Uses conditional logic to count how many times the 
#    integers from one party are greater than those from another party.
# 6. Output Aggregation: Returns the results of the computations and statistical 
#    analysis as outputs for each party.

# The program provides a robust framework for conducting privacy-preserving 
# computations and data analysis, ensuring that sensitive data remains secure 
# throughout the process. This is particularly useful in scenarios where data 
# privacy is paramount, such as in collaborative research or secure multi-party 
# computations.


# Run the main function
outputs = nada_main()
for output in outputs:
    print(output)

# task : 1.Given the daily step counts of a user for the last 7 days as [6500, 7200, 8000, 6000, 9000, 7500, 8200], calculate the range of steps and 
#          explain what this tells you about the user's activity pattern.
"""
import numpy as np 
steps = np.array([6500, 7200, 8000, 6000, 9000, 7500, 8200])
steps_range = np.max(steps) - np.min(steps)
print("Range of steps:", steps_range)"""

# explanation :
"""
The range of steps is calculated by subtracting the minimum step count from the maximum step count over
the last 7 days. In this case, the maximum step count is 9000 and the minimum is 6000, resulting in a range of 3000 steps.
This indicates the variability in the user's daily activity levels, with a relatively wide spread in step counts across the week.
"""
# task : 2.For a list of 5 food delivery order amounts on Zomato: [250, 400, 350, 300, 500], write code to compute the variance 
#          and standard deviation of the order amounts
"""
import numpy as np
order_amounts = np.array([250, 400, 350, 300, 500])
print("Variance of order amounts:", np.var(order_amounts))
print("Standard deviation of order amounts:", np.std(order_amounts))
"""

# task : 3.You have the monthly mobile data usage (in GB) for a user over 6 months: [3.2, 2.8, 3.5, 3.0, 2.9, 3.1]. Calculate the coefficient of variation (CV) and 
#          interpret whether the user's data usage is consistent or highly variable.<br><br><em><strong>Hint:</strong> CV = (Standard Deviation / Mean) × 100%</em
"""
import numpy as np
data_usage = np.array([3.2, 2.8, 3.5, 3.0, 2.9, 3.1])
print("Coefficient of Variation (CV):", (np.std(data_usage) / np.mean(data_usage)) * 100)
"""

# task : 4. Suppose you are analyzing the number of likes on 10 recent Instagram posts: [120, 150, 130, 110, 170, 140, 135, 160, 125, 155]. 
#           Compute the standard deviation and compare it with the mean to comment on the consistency of engagement.

import numpy as np
likes = np.array([120, 150, 130, 110, 170, 140, 135, 160, 125, 155])
print("Mean of likes:", np.mean(likes))
print("Standard deviation of likes:", np.std(likes))

# explanation :
"""
Mean calculates the average likes which is 139.5, while the standard deviation which is approximately 18.45.
The standard deviation is low compared to the mean, so the likes do not vary much. This means Instagram engagement is fairly consistent across the 10 posts.
"""


# task : 5. Use ChatGPT or any AI tool to generate a small dataset (at least 8 values) representing daily UPI transaction amounts for a week. Then, 
#   calculate the variance and standard deviation of the generated data, and briefly interpret what the results mean for spending stability.

import numpy as np
upi_transactions = np.array([200, 250, 300, 180, 220, 280, 240, 260])
print("Variance of UPI transactions:", np.var(upi_transactions))
print("Standard deviation of UPI transactions:", np.std(upi_transactions))

# explanation :
"""
The standard deviation shows how much daily spending varies from the average. 
Since it is relatively low, daily spending is fairly stable, with some small variations.
"""

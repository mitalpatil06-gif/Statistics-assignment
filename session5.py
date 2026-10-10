# task : 1. Given a list of delivery times (in minutes) for 20 Zomato orders, calculate the 25th, 50th, and 75th percentiles 
#           using Python's numpy.percentile function
"""
import numpy as np
delivery_times = np.array([30, 25, 40, 35, 20, 45, 50, 30, 25, 40, 35, 20, 45, 50, 30, 25, 40, 35, 20, 45])
q1 = np.percentile(delivery_times, 25)
q2 = np.percentile(delivery_times, 50)
q3 = np.percentile(delivery_times, 75)
print("25th percentile (Q1):", q1)
print("50th percentile (Q2):", q2)
print("75th percentile (Q3):", q3)
"""

# task : 2.Create a Python script that takes an array of IPL player scores and divides them into quartiles using 
#          numpy.quantile. Print the values for Q1, Q2 (median), and Q3
"""
import numpy as np
player_scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 84])
q1 = np.quantile(player_scores, 0.25)
q2 = np.quantile(player_scores, 0.5)    
q3 = np.quantile(player_scores, 0.75)

print("First quartile (Q1):", q1)
print("Second quartile (Q2 - Median):", q2)
print("Third quartile (Q3):", q3)
"""

# task : 3. Given a list of daily step counts from your fitness app for one month, calculate the Interquartile Range (IQR) in Python 
#           and explain what it tells you about your activity consistency.<br><br><em><strong>Hint:</strong> IQR = Q3 - Q1</em>
"""
import numpy as np
step_counts = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500])

q1 = np.quantile(step_counts, 0.25)
q3 = np.quantile(step_counts, 0.75)
iqr = q3 - q1
print("Interquartile Range (IQR):", iqr)
"""

# explanation:
"""
The Interquartile Range (IQR) is a measure of statistical dispersion that represents the range within which the middle 50% of the data falls. In this case, 
the IQR of the daily step counts indicates how consistent your activity levels are over the month. A smaller IQR suggests that your daily step counts are relatively consistent, while a larger IQR indicates more variability in your activity levels.
"""
# task : 4. Write a Python function to detect outliers in a list of Swiggy order amounts using the IQR method (any value below Q1 - 1.5*IQR or above Q3 + 1.5*IQR). Print the outlier values
"""
def detect_outliers(order_amounts):
    
    import numpy as np
    order_amounts = np.array(order_amounts)
    q1 = np.percentile(order_amounts, 25)   
    q3 = np.percentile(order_amounts, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = order_amounts[(order_amounts < lower_bound) | (order_amounts > upper_bound)]
    return outliers

orders = [100, 150, 200, 250, 300, 350, 400, 1500]

print(detect_outliers(orders))
""" 

# task : 5. Using matplotlib, create a boxplot of your weekly screen time (in hours) for the past 8 weeks. Label the axes and highlight any outliers
"""
import matplotlib.pyplot as plt

screen_time = [2, 3, 2.5, 4, 3.5, 2.5, 3, 4.5]
plt.boxplot(screen_time, patch_artist=True)
plt.xlabel("Weekly Screen Time (hours)")
plt.ylabel("Hours")
plt.title("Screen Time Distribution")
plt.show()
"""
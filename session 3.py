#  task: 1.Create an array of 7 daily step counts (e.g., from your phone's fitness app) and write code to calculate the mean (average) number of steps.
"""
import numpy as np
arr = np.array([5000, 7000, 8000, 6000, 7500, 9000, 6500])

print("Mean of daily step counts :", np.mean(arr))
"""

# Task : 2.Given this list of food delivery times in minutes for your last 9 Zomato/Swiggy orders: [32, 28, 29, 45, 30, 31, 60, 30, 29], write a function to find the median delivery time
"""
import numpy as np
def find_median(delivery_times):
    median = np.median(delivery_times)
    return median

delivery_times = np.array([32, 28, 29, 45, 30, 31, 60, 30, 29])
print("Median delivery time:", find_median(delivery_times))
"""
# task : 3.Imagine you tracked the genres of 12 YouTube videos you watched this week: ['Music', 'Vlog', 'Music', 'Tech', 'Music', 'Vlog', 'Tech', 'Music', 'Comedy', 'Vlog', 'Music', 'Comedy']. 
# Write code to determine the mode (most watched genre)
"""
def find_mode(genres):
  mode = genres[0]
  max_count = genres.count(mode)


  for genre in genres:
    count = genres.count(genre)

    if count > max_count:
      max_count = count
      mode = genre

    return mode
genres = ['Music', 'Vlog', 'Music', 'Tech', 'Music', 'Vlog', 'Tech', 'Music', 'Comedy', 'Vlog', 'Music', 'Comedy']
print("Most watched genre:", find_mode(genres))
"""
# task : 4.Take this array of daily UPI transaction amounts (in ₹): [100, 120, 105, 110, 5000, 115, 108]. Calculate both the mean and the median, then explain in 2-3 lines which is a better measure of your 'typical' 
# transaction and why.<br><br><em><strong>Hint:</strong> Consider the effect of the ₹5000 value.</em>
"""
import numpy as np

transactions = np.array([100, 120, 105, 110, 5000, 115, 108])

mean = np.mean(transactions)
median = np.median(transactions)

print("Mean:", mean)
print("Median:", median)
"""
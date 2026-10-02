Task : 1
"""Given the following columns from a mock Zomato restaurant dataset — Restaurant Name, Cuisine Type, Average Cost for Two, User Rating, 
City, and Open/Closed Status — classify each column as either Numerical (Continuous or Discrete) or Categorical (Nominal or Ordinal).

Restaurant Dataset :

          Column                     Data type            Measurement Scales     
  
Rastaurant Name : -         Categorical  --->          Nominal     
Cuisine Type :-                 Categorical  --->           Nominal
Average cost for two :-      Numerical   --->           Continuous
User Rating:-                    Numerical   --->           Continuous 
City :-                               Categorical  --->           Nominal
Open/closed Status:-       Categorical  --->           Nominal 
"""

Task : 2 
"""Create a table with 8 real-life examples (not from class) of data you might find in popular apps like Instagram, Flipkart, or IRCTC. For each, 
specify the measurement scale (Nominal, Ordinal, Interval, or Ratio) and briefly explain your choice.<br><br><em><strong>Hint:</strong>
 Think about things like 'Order Status', 'Train Departure Time', 'Number of Likes', or 'Payment Method'.</em>


Real -Life Examples of Measurement Scales:-

column                                  Data type           Measurment scales                     Explanation 

1.Order status                        Categorical               Ordinal                           meaningful order, such as Placed, Shipped and Delivered.
2.Train Department Time      Numerical                Interval                           times is meaningful, but there is no true zero.
3.Number of Likes                  Numerical                Ratio                               it has a true zero
4.Payment Method                 Categorical               Nominal                         Payment methods like UPI, Card and Cash have no natural order.
5.Number of Items                  Numerical                 Ratio                              it can be counted and zero means no items.
6.Product Rating                     Categorical               Ordinal                           ratings have a clear order from low to high.
7.Age of the customer             Numerical                 Ratio                              age has a true zero, and differences and ratios are meaningful.
8.City                                      Categorical                Nominal                        Cities like Ahmedabad, Mumbai and Delhi are names/categories with no order.
"""

Task : 3 
"""Given this time-series data from a Spotify user's listening history — Date, Song Name, Play Count per Day — identify which columns 
represent time-series, and which are categorical or numerical. Explain your reasoning.

Column                             Data type                              Explanation

Date                                  Time-Series                       Records data over time.
Song name                        Categorical(Nominal)        Names have no natural order.
Play count per day              Numerical(Discrete)        Represents a countable number of plays.
"""

Task : 4 

"""
Write a function or pseudocode that takes a column of data (array of values) from a Flipkart order history and automatically detects whether it is likely Nominal, Ordinal, Interval, or 
Ratio scale. Briefly describe the logic used for each type.<br><br><em><strong>Constraint:</strong> You do not need to write a perfect algorithm — focus on simple rules based on value types and patterns.
"""
def find_scale(data):

    if all(isinstance(x, str) for x in data):
        return "Nominal"

    elif all(x in [1, 2, 3, 4, 5] for x in data):
        return "Ordinal"

    elif all(isinstance(x, (int, float)) for x in data):
        if 0 in data:
            return "Ratio"
        else:
            return "Interval"

    return "Unknown"


data = ["Clothing", "Shoes", "Mobile"]

print(find_scale(data))


import math

# Mean
def mean_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return sum(lst) / len(lst)

# Median
def median_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[n // 2]

# Modus
def mode_own(lst):
    freq_map = {}
    for item in lst:
        if item in freq_map:
            freq_map[item] += 1
        else:
            freq_map[item] = 1
    
    max_freq = max(freq_map.values())
    mode = [key for key, value in freq_map.items() if value == max_freq]
    
    if len(mode) == len(lst):
        return None
    
    return mode

# Standard Deviation
def std_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    mean = mean_own(lst)
    sum_squared_diff = sum((x - mean) ** 2 for x in lst)
    mean_squared_diff = sum_squared_diff / len(lst)
    std_dev = math.sqrt(mean_squared_diff)
    
    return std_dev

# Variance
def variance_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return std_own(lst)**2

# Maximum Value
def max_data_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return max(lst)

# Minimum Value
def min_data_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return min(lst)

# Range
def range(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return max_data_own(lst) - min_data_own(lst)

# First Quartile
def quartile_first(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    sorted_lst = sorted(lst)
    
    n = len(sorted_lst)
    
    if n % 2 == 0:
        lower_half = sorted_lst[:n // 2]
        q1_index = len(lower_half) // 2
        q1 = (lower_half[q1_index - 1] + lower_half[q1_index]) / 2
    else:
        lower_half = sorted_lst[:n // 2 + 1]
        q1_index = len(lower_half) // 2
        q1 = lower_half[q1_index]
    
    return q1

# Second Quartile
def quartile_second(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    sorted_lst = sorted(lst)
    
    n = len(sorted_lst)
    
    if n % 2 == 0:
        q2_index = n // 2
        q2 = (sorted_lst[q2_index - 1] + sorted_lst[q2_index]) / 2
    else:
        q2_index = n // 2
        q2 = sorted_lst[q2_index]
    
    return q2

# Third Quartile
def quartile_third(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    sorted_lst = sorted(lst)
    
    n = len(sorted_lst)
    
    if n % 2 == 0:
        upper_half = sorted_lst[n // 2:]
        q3_index = len(upper_half) // 2
        q3 = (upper_half[q3_index - 1] + upper_half[q3_index]) / 2
    else:
        upper_half = sorted_lst[n // 2 + 1:]
        q3_index = len(upper_half) // 2
        q3 = upper_half[q3_index]
    
    return q3

# IQR (Interquartile Range)
def iqr_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    return quartile_third(lst) - quartile_first(lst)

# Skewness
def skewness_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    mean = mean_own(lst)
    std_dev = std_own(lst)
    n = len(lst)
    
    skewness = (sum((x - mean) ** 3 for x in lst) * n) / ((n - 1) * (n - 2) * std_dev ** 3)
    
    return skewness

# Kurtosis
def kurtosis_own(lst):
    if not all(isinstance(x, (float, int)) for x in lst):
        return None
    
    mean = mean_own(lst)
    std_dev = std_own(lst)
    n = len(lst)
    
    kurtosis = (sum((x - mean) ** 4 for x in lst) * n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3) * std_dev ** 4) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    
    return kurtosis

# Unique Value
def unique_values_own(lst):
    if not all(isinstance(x, str) for x in lst):
        return None
    
    unique_set = set(lst)
    num_unique = len(unique_set)
    
    return num_unique

# Proportion
def proportion(lst):
  arr = {}
  for x in lst:
    if x in arr:
      arr[x] += 1
    else:
      arr.setdefault(x, 1)

  sum_val = sum(arr.values())
  for x in arr:
    arr[x] /= sum_val

  return arr

def calculate_length(lst):
    length = 0
    for _ in lst:
        length += 1
    return length
  
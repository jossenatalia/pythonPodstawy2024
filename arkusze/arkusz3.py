import pandas as pd
import numpy as np

technologies = ['Spark', 'Pandas', 'Python', 'PHP']
fee = [25000, 2000, 15000, 18000, 22000]
duration = ['50 Days', '35 Days', np.nan, '15 Days', '10 Days']
discount = [2000, 1000, 800, 500, 500]
columns = ["Courses", "Fee", "Duration", "Discount"]

data = pd.DataFrame(list(zip(technologies, fee, duration, discount)),
                    columns=columns)
print(data)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas   2000  35 Days      1000
# 2  Python  15000      NaN       800
# 3     PHP  18000  15 Days       500

data.to_excel("sales2.xlsx", index=False)
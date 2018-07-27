import billionaires
import matplotlib.pyplot as plt
import numpy as np

list_of_billionaire = billionaires.get_billionaires()

import school_scores
list_of_record = school_scores.get_all()

billList = []
for billionaire in list_of_billionaire:
    if(billionaire["location"]["citizenship"] == "United States"):
        if(billionaire["wealth"]["worth in billions"] < 15):
            print(billionaire["name"], billionaire["wealth"]["worth in billions"])
            billList.append(billionaire["wealth"]["worth in billions"])

print(np.arange(0.0, 1.0, 0.1))

plt.hist(billList, bins=np.arange(0.0, 15.0, 0.5))
plt.xlabel("Wealth in Billions")
plt.ylabel("Frequency")
plt.axis([1,15,0,300])
plt.grid(True)
plt.show()

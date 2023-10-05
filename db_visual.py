import matplotlib.pyplot as plt
from db_clean_up import db_cleaned

y = db_cleaned["N global \nFCM inventories where included"]
x = db_cleaned["Name"]

chemicals = x.tolist()
occurences = y.tolist()

sorted_occurences, sorted_chemicals = zip(*sorted(zip(occurences, chemicals), reverse=True))

plt.style.use('fivethirtyeight')

plt.figure(figsize=(8, 6))
plt.bar(sorted_chemicals[0:9], sorted_occurences[0:9], color='orange')


# # plt.hist(y, bins=x)

# # plt.title('Frequency of certain chemicals in publications')
# # plt.xlabel('Chemical')
# # plt.ylabel('Amount of times appeared')

plt.tight_layout()

plt.show()

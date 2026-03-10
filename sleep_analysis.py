import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sleep_data.csv")

print(data)

avg_sleep = data["sleep_hours"].mean()
print("Average Sleep:", avg_sleep)

plt.bar(data["person"], data["sleep_hours"])
plt.title("Sleep Hours by person")
plt.xlabel("Person")
plt.ylabel("Sleep Hours")

plt.savefig("sleep_chart.png")
plt.show()


plt.scatter(data["caffeine_mg"], data["sleep_hours"])
plt.title("Caffine vs Sleep")
plt.xlabel("Caffine (MG)")
plt.ylabel("Sleep Hours")

plt.show()

import matplotlib.pyplot as plt

x_values = range(0, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='blue', s=10)

# 设置图表标题并给坐标轴加上标签。
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小。
# ax.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围。
# ax.axis([0, 1100, 0, 1100000])


plt.show()
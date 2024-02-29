import matplotlib.pyplot as plt
import mpld3

labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = [30, 25, 40, 100]
colors = ['red', 'green', 'blue', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f')

plt.title("Wykres kołowy")
plt.axis('equal')

html = mpld3.fig_to_html(plt.gcf())
plt.show()

with open("pie.html", "w") as fp:
    fp.write(html)


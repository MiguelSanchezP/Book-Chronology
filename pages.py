import matplotlib.pyplot as plt
import numpy as np


def assignar_y (list):
	output = []
	for i in range(len(list)):
		if list[i] == "Divulgatiu":
			output.append(np.random.randint(200)+50)
		if list[i] == "Novella":
			output.append(np.random.randint(200)+250)
		if list[i] == "Assaig":
			output.append(np.random.randint(40)+490)
		if list[i] == "Historic":
			output.append(np.random.randint(40)+530)
		if list[i] == "Altres":
			output.append(np.random.randint(40)+570)
	return np.array(output)

pages_2021 = np.array([498,256,128,448,393,592,36,298,148,372,388,366,325,594,334,139])
pages_2022 = np.array([751,197,215,211,168,528,408,256,319])
titles_2021 = np.array(["Sapiens", "The queen's gambit", "The abolition of man", "Homo Deus", "A thosand splendid suns", "Crime and punishment", "The withered arm", "To kill a mockingbird", "Veinte poemas de amor y\n una canción desesperada", "21 lessons for the 21st century", "Mirall trencat", "Nada", "Viral", "La cura", "Pride and prejudice", "The great Gatsby"])
categories_2021 = np.array(["Divulgatiu", "Novella", "Assaig", "Divulgatiu", "Novella", "Novella", "Novella", "Novella", "Altres", "Divulgatiu", "Novella", "Novella", "Divulgatiu", "Novella", "Novella", "Novella"])
titles_2022 = np.array(["12 rules for life", "The old man and the sea", "Farenheit 451", "A moveable feast", "El hombre ameba y otras ideas geniales", "The gulag archipelago", "Como hacer una tarta de\nmanzana desde el principio", "Las palabras primas", "La vacuna"])
categories_2022 = np.array(["Altres", "Novella", "Novella", "Novella", "Divulgatiu", "Historic", "Divulgatiu", "Assaig", "Divulgatiu"])
x_2021 = np.ones(len(pages_2021))*2021
y_2021 = assignar_y (categories_2021)
y_2022 = assignar_y (categories_2022)
x_2022 = np.ones(len(pages_2022))*2022

X = np.append(x_2021, x_2022)
Y = np.append(y_2021, y_2022)
P = np.append(pages_2021, pages_2022)
names = np.append(titles_2021, titles_2022)

colors = np.random.rand(len(P), 3)

cmap = plt.cm.RdYlGn
norm = plt.Normalize(1,4)

c = np.random.randint(1,5,size=len(np.append(pages_2021,pages_2022)))

fig,ax = plt.subplots()

plt.xticks([2020, 2021, 2022, 2023, 2024, 2025])
plt.title('Book Chronology')
plt.scatter(2020, 650,s=0)
sc = plt.scatter(X, Y ,s=P*1.5, alpha=0.5, c=colors, cmap=cmap, norm=norm)
plt.scatter(2025, 0,s=0)
plt.tick_params(left=False, labelleft=False)

annot = ax.annotate("", xy=(0,0), xytext=(20,20), textcoords="offset points", bbox=dict(boxstyle="round", fc="w"),arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
	pos = sc.get_offsets()[ind["ind"][0]]
	annot.xy = pos
	text = "{}".format(" ".join([names[n] for n in ind["ind"]]))
	annot.set_text(text)
	annot.get_bbox_patch().set_facecolor(colors[ind["ind"][0]]) #cmap(norm(c[ind["ind"][0]])))
	annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
	vis = annot.get_visible()
	if event.inaxes == ax:
		cont, ind = sc.contains(event)
		if cont:
			update_annot(ind)
			annot.set_visible(True)
			fig.canvas.draw_idle()
		else:
			if vis:
				annot.set_visible(False)
				fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()

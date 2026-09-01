import matplotlib.pyplot as plt 
events = {
    1958: "Perceptron",
    1986: "Backpropagation",
    1995: "SVM",
    2001: "Random Forest",
    2012: "AlexNet (Deep Learning revival)",
    2014: "GANs",
    2017: "Transformers",
    2018: "BERT",
    2020: "GPT-3",
    2022: "ChatGPT / RLHF"
}
fig, ax = plt.subplots(figsize=(10, 3))
years = list(events.keys())
ax.scatter(years, [0]*len(years))
for year, label in events.items():
    ax.annotate(label, (year,0), rotation=45, ha='right', fontsize=8)
ax.get_yaxis().set_visible(False)
ax.set_xlabel("Year")
ax.set_title("Key Inflection Points in ML History")
plt.tight_layout()
plt.savefig("ml_timeline.png")
print("Timeline saved.")    
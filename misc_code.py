#####BARPLOT######
plt.figure(figsize=(20, 10)) 
plt.subplots_adjust(bottom=0.20) 
# plt.bar(most_used_dev.keys(), most_used_dev.values(), color="xkcd:turquoise",) 
for k in most_used_dev.keys(): 
	plt.bar(k, most_used_dev[k], color=(np.random.random(), np.random.random(), np.random.random()), label=str(most_used_dev[k])) 
plt.xticks(rotation=45)
plt.title("Device - App Combination x Usage")
plt.xlabel("Platforms")
plt.ylabel("# of Sessions")
plt.legend()
plt.show()

#####SORTED_DICTIONARY#####
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

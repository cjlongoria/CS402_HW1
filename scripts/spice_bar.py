import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_fwf('data/spice.txt', header=None)
df.rename(columns={0:'Action',1:'Hex'}, inplace=True)

actions = ['Read', 'Write']
actions_values = [df['Action'].value_counts()[0], df['Action'].value_counts()[1]]

fig, ax = plt.subplots(figsize=(5,5))
plt.bar(actions, actions_values, .3)
plt.ylabel('Occurence')
plt.xlabel('Action')
plt.title('Read/Write Actions (spice.din)')
ax.axhline(66538, c='r')
ax.axhline(150699, c='r')
ax.annotate('66538',
            xy=(.48, .47), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=10)
ax.annotate('150699',
            xy=(.48, .84), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=10)
plt.savefig('images/Hw1_bar_spice.png')
#plt.show()
#print(actions_values)
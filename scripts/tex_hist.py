import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_fwf('tex.txt', header=None)
df.rename(columns={0:'Action',1:'Hex'}, inplace=True)
df['Dec'] = df['Hex'].apply(int, base=16)
df.sort_values(by=['Dec'], inplace=True)

dec_array = range(df['Dec'].min(),df['Dec'].max(), 200000000)
hex_array = [hex(x) for x in dec_array]

fig, ax = plt.subplots(figsize=(10,10))
plt.hist(df['Dec'], bins=20)
plt.xlim(xmin=df['Dec'].min(), xmax = df['Dec'].max())
ax.ticklabel_format(useOffset=False, style='plain')
plt.xticks(dec_array, hex_array, rotation=45)
plt.ylabel('Occurence')
plt.xlabel('Address')
plt.title('Histogram of Trace Addresses (tex.din) ')
plt.savefig('Hw1_hist1_tex')

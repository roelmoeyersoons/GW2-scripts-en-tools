#%%
import matplotlib.pyplot as plt
import psycopg2 as psy
import numpy as np
from datetime import datetime
plt.rcParams["figure.figsize"] = (20,5)

plt.show()
conn = psy.connect(host="localhost",database="gw", user="postgres")
cur = conn.cursor()
cur.execute("select * from silverwastes")
ding = np.array(cur.fetchall())
tijden = []
for ts in ding[:,0]:
    tijden.append(datetime.fromtimestamp(ts))

plt.plot(tijden, ding[:,1])
print(ding.shape[0])

# %%


# %%

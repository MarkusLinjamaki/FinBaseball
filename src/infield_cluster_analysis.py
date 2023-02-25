#%%
import numpy as np



#%%
with open('hit_stats.npy', 'rb') as f:
    infield_stats = np.load(f)

#%%
print(infield_stats.shape)
# %%
## Testing 42459
one_game_stats = infield_stats[infield_stats[:,5] == '42459',:]

# %%

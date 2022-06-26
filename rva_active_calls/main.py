#%%
from rva_active_calls.__functionality import rva_calls, database

data = rva_calls().calls()

# TODO Rename variables
data_warehouse = database()

data_warehouse.read()

data_warehouse.write(data)



# %%

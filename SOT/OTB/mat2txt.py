import os
import pdb
import scipy.io as scio
import numpy as np

base_path = '/data/home/v-zhipeng/project3/UDT/results/metacrest/otb/'
files = os.listdir(base_path)
files = [f  for f in files if '.mat' in f]

save_path = '/data/home/v-zhipeng/project3/UDT/results/metacrest/otb_txt/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

for f in files:
    f_path = os.path.join(base_path, f)
    result = scio.loadmat(f_path)
    result = result['results'][0][0][0][0][0]   # [K,4]
    new_name = f.split('_')[0]+'.txt'
    new_save_path = os.path.join(save_path, new_name)

    with open(new_save_path, "w") as fin:
        for x in result:
            fin.write(','.join([str(i) for i in x]) + '\n')


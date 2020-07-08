import os
import pdb
import scipy.io as scio
import numpy as np

base_path = '/data/home/v-zhipeng/project3/pysot-toolkit/result/UDT'
files = os.listdir(base_path)

save_path = '/data/home/v-zhipeng/project3/pysot-toolkit/result/UDT_new'
if not os.path.exists(save_path):
    os.makedirs(save_path)

for f in files:
    f_path = os.path.join(base_path, f)
    result = np.loadtxt(f_path)
    new_save_path = os.path.join(save_path,f)

    with open(new_save_path, "w") as fin:
        for x in result:
            fin.write(','.join([str(i) for i in x]) + '\n')


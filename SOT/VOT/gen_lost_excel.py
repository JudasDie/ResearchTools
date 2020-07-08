# -*- coding:utf-8 -*-
# ! ./usr/bin/env python
# __author__ = 'zzp'

import os
import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='To generate excel from tune results.')
parser.add_argument('--result_path', default='../examples/siamrpn/result', help='vot/otb tune result path')
parser.add_argument('--save_path', default='siamrpn.xlsx', help='where to save xls result')
args = parser.parse_args()


writer = pd.ExcelWriter(args.save_path)


def list_average(nums):
    nsum = 0
    for i in nums:
        nsum += i
    return nsum / len(nums)


def calc_dataset_lost(dataset_result):
    for i, key in enumerate(dataset_result.keys()):
        if i == 0:
            # calc mean
            data_matrix = np.array(dataset_result[key])
        else:
            data_matrix = np.vstack((data_matrix, np.array(dataset_result[key])))

    re = np.sum(data_matrix, axis=0)

    return re


def extract_results(result_dir):
    write_data = {}
    datasets = os.listdir(result_dir)
    print('test dataset {}'.format(datasets))

    for i, dataset in enumerate(datasets):
        dataset_result = {}
        tracker = os.listdir(os.path.join(result_dir, dataset))  # all dataset have the same tune params
        tracker.append('mean')  # calc mean
        write_data['Stracker'] = tracker
        for j, param_dir in enumerate(tracker):
            if param_dir == 'mean':
                break
            else:
                seqs = os.listdir(os.path.join(result_dir, dataset, param_dir, 'baseline'))
            for k, seq in enumerate(seqs):
                seq_path = os.path.join(result_dir, dataset, param_dir, 'baseline', seq, seq + '_001.txt')
                lost = 0
                for x in open(seq_path).readlines():
                    if x.strip() == '2':
                        lost += 1
                if not seq in dataset_result.keys():
                    dataset_result[seq] = [lost]
                else:
                    dataset_result[seq].append(lost)

        for w_i, w_key in enumerate(dataset_result.keys()):
            temp = dataset_result[w_key].copy()
            mean = list_average(dataset_result[w_key])
            temp.append(mean)
            # write_data[w_key] = dataset_result[w_key]
            write_data[w_key] = temp

        # dataset sum result
        re = list(calc_dataset_lost(dataset_result).copy())
        mean = list_average(re)
        re.append(mean)

        write_data[dataset] = re


        df1 = pd.DataFrame(data=write_data)
        df1.to_excel(writer, 'Sheet'+str(i))
    writer.save()




if __name__ == '__main__':
    extract_results(args.result_path)
    print()
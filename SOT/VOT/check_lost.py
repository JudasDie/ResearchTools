from os.path import join, realpath, dirname
import glob
import argparse
import os
import shutil
import datetime

parser = argparse.ArgumentParser(description='SiamRPN tracker Lost analysis on VOT')
parser.add_argument('--dataset', default='VOT2017', type=str, metavar='DATA', help='VOT version')
parser.add_argument('--result_path', default='./result', type=str, metavar='PATH', help='Result path')
parser.add_argument('--reg', default='*', type=str, metavar='TRACKER', help='Tracker regex')
parser.add_argument('--output', default='lost_analysis.txt', type=str, metavar='OUTPUT', help='output file name')
parser.add_argument('--start', default=0, type=int, help='Tracker regex start')
parser.add_argument('--end', default=10000000, type=int, help='Tracker regex end')
parser.add_argument('--move_ranges', type=str, default='all', help='test how many results')
args = parser.parse_args()


file_names = glob.glob(join(args.result_path, args.dataset, args.reg))
tracker_num = len(file_names)
file_names = file_names[args.start:min(args.end,tracker_num)]

min_lost = 100000
min_lost_file_name = ''

list_path = join(realpath(dirname(__file__)), '../../dataset', args.dataset,'list.txt')
with open(list_path) as f:
    seq_names = [v.strip() for v in f.readlines()]

f = open(args.output, 'w')  # output file
f.write('tracker ' + args.dataset + ' ' + ' '.join([str(i) for i in seq_names]) + '\n')

lost_res = dict()
lost_res['video'] = seq_names
lost_res['tracker'] = file_names

for file_name in file_names:
    # print file_name
    sum_lost = 0
    lost_vec = []
    lost_res[file_name] = []
    for seq in seq_names:
        seq_path = join(file_name, 'baseline', seq, seq+'_001.txt')
        lost = 0
        for x in open(seq_path).readlines():
            if x.strip() == '2':
                lost += 1
        sum_lost += lost
        lost_vec.append(lost)
        lost_res[file_name].append(lost)
        # print('{:14s} Lost: {:d}'.format(seq, lost))
    #f.write(file_name + ' ' + str(sum_lost) + ' ' + ' '.join([str(i) for i in lost_vec]) + '\n')
    min_lost = min(min_lost, sum_lost)
    if sum_lost == min_lost:
        min_lost_file_name = file_name
    f.write('{:40s} Sum Lost: {:d}\n'.format(file_name, sum_lost))
    print('{:40s} Sum Lost: {:d}'.format(file_name, sum_lost))
print('\n\n Min Lost')
print('{:40s} Lost: {:d}'.format(min_lost_file_name, min_lost))
f.close()

# import json
# print('save json (raw vid info), please wait 1 min~')
# json.dump(lost_res, open(args.output.replace('txt', 'json'), 'w'), indent=2)
# print('done!')

## zzp
# move all out of analysis range results to another dir
if args.move_ranges == 'all':
    print('You are trying test all trackers, may take a while...')
    exit()
else:
    move_range = int(args.move_ranges)

# make a dir always store untested resutls

for line, lost in enumerate(open(args.output, 'r')):
    if line == 0:
        continue
    
    tracker = lost.split(' ')[0]
    sum_lost = lost.split(' ')[-1]
    if 'test' in tracker:  # for epoch test
        save_path = os.path.join(tracker.split('test')[0], 'test_untested')
    else: 
        save_path = os.path.join(tracker.split('result')[0], 'result_untested')

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if int(sum_lost) > int(min_lost) + move_range:
        print('move to {}'.format(save_path))
        shutil.move(tracker, save_path)


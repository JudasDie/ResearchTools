import os
from os import listdir
from os.path import join, exists
from tqdm import tqdm

def calc_vot(vot_path):
    fnums = []
    size = []  # area
    motion = [] # max(mx/width, my/height)
    size_ch = []  # size change ratio
    
    videos = listdir(vot_path)
    videos.remove('list.txt')

    print('====> in processing: vot <====')
    for v in tqdm(videos):
        v_path = join(vot_path, v)
        gt_path = join(v_path, 'groundtruth.txt')
        gts = open(gt_path, 'r').readline()

        fnums.append(len(gts))
        boxs = []
        for g in gts:
            bb = eval(g)[1:5]
            if bb[0] == 0 and bb[1] ==0:
                continue
            else:
                boxs.append(bb)
        
        for i, b in enumerate(boxs):
            size.append(b[2] * b[3])
            if i > 0:
                pos = [b[0] + b[2]/2, b[1] + b[3]/2]
                pos0 = [boxs[i-1][0] + boxs[i-1][2]/2, boxs[i-1][1] + boxs[i-1][3]/2]

                mx = abs(pos[0] - pos0[0]) / pos0[2]
                my = abs(pos[1] - pos0[1]) / pos0[3]
                motion.append(max(mx, my))

                s = b[2] * b[3]
                s0 = boxs[i-1][2] * boxs[i-1][3]
                size_ch.append(abs(s-s0)/s0)

    print('====> record <====')
    with open('./vot_fnums.txt', "w") as fin:
        fin.write(','.join([str(i) for idx, i in enumerate(fnums)]) + '\n')
    
    with open('./vot_size.txt', "w") as fin:
        fin.write(','.join([str(i) for idx, i in enumerate(size)]) + '\n')

    with open('./vot_motion.txt', "w") as fin:
        fin.write(','.join([str(i) for idx, i in enumerate(motion)]) + '\n')

    with open('./vot_size_ch.txt', "w") as fin:
        fin.write(','.join([str(i) for idx, i in enumerate(size_ch)]) + '\n')

    print('Done!')


if __name__ == '__main__':
    vot_path = '/home/zpzhang/project/workspaces/vot-workspace/sequences'
    davis_path = '/home/zpzhang/data/testing/DAVIS-trainval'
    calc_vot(vot_path)


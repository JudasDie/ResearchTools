import os
import pandas as pd
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Analysis siamfc tune results')
parser.add_argument('--path',default='logs/tune_eao.log', help='tune result path')
parser.add_argument('--dataset',default='VOT2015', help='test dataset')
parser.add_argument('--save_path',default='logs', help='tune result box-graph save path')


def draw_box_graph(args):
    if not args.path.endswith('txt'):
        name = args.path.split('.')[0]
        name = name + '.txt'
        os.system("cp {0} {1}".format(args.path, name))
        args.path = name
        print('change {0} to {1}'.format(args.path, name))
    fin = open(args.path, 'r')
    lines = fin.readlines()

    win_inf = {}
    scale_lr = {}
    for line in lines:
        if not line.startswith('eao'): 
            pass
        else:
            temp0, temp1, temp2, temp3 = line.split(', ')
            eao = temp0.split(': ')[-1]
            wi = temp2.split(': ')[-1]   # get window influence
            slr = temp3.split(': ')[-1]  # get scale lr
            
            # debug
            print("w_i: {}, scale_lr: {}, eao: {}".format(wi, slr, eao))
            
            if wi in win_inf.keys():
                win_inf[wi].append(float(eao))
            else:
                win_inf[wi] = [float(eao)]

            if slr in scale_lr.keys():
                scale_lr[slr].append(float(eao))
            else:
                scale_lr[slr] = [float(eao)]
    #print(win_inf)
    #print(scale_lr)
    
    # draw box graph
    wi_data = pd.DataFrame(win_inf) 
    slr_data = pd.DataFrame(scale_lr)
    
    # draw
    wi_data.boxplot(rot=45)
    #slr_data.boxplot()
    plt.ylabel("EAO")  
    plt.xlabel("Window Influence")
    plt.title('{} Windows Influence anaylsis'.format(args.dataset))
    
    plt_save_name = os.path.join(args.save_path, '{}_W_I_analysis.png'.format(args.dataset))
    plt.savefig(plt_save_name, dpi=1000)
    
    slr_data.boxplot(rot=45)
    plt.ylabel("EAO")  
    plt.xlabel("Scale lr")
    plt.title('{} Scale Learning-Rate anaylsis'.format(args.dataset))
    
    plt_save_name = os.path.join(args.save_path, '{}_slr_analysis.png'.format(args.dataset)) 
    plt.savefig(plt_save_name, dpi=1000)


if __name__ == '__main__':
    
    args = parser.parse_args()

    # checkpath
    if not os.path.exists(args.path):
        print('Tune results path not exists, please figure out right path...')
        exit()
    
    if not os.path.exists(args.save_path):
        print('Save path not exists, make it')
    
    draw_box_graph(args)

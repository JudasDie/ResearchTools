import os
import pandas as pd
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Analysis siamfc tune results')
parser.add_argument('--path',default='logs/tune_auc_279_0.6657.log', help='tune result path')
parser.add_argument('--dataset',default='OTB2013', help='test dataset')
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
        if not line.startswith('./result'): 
            pass
        else:
            _, temp0 = line.split('w_influence_')
            wi, _, _, temp1 = temp0.split('_')   # get window influence
            slr, temp3 = temp1.split('(')  # get scale lr
            auc = temp3.split(')')[0]    # get auc
            
            # debug
            print("w_i: {}, scale_lr: {}, auc: {}".format(wi, slr, auc))
            
            if wi in win_inf.keys():
                win_inf[wi].append(float(auc))
            else:
                win_inf[wi] = [float(auc)]

            if slr in scale_lr.keys():
                scale_lr[slr].append(float(auc))
            else:
                scale_lr[slr] = [float(auc)]
    #print(win_inf)
    #print(scale_lr)
    
    # draw box graph
    wi_data = pd.DataFrame(win_inf) 
    slr_data = pd.DataFrame(scale_lr)
    
    # draw
    wi_data.boxplot(rot=45)
    #slr_data.boxplot()
    plt.ylabel("AUC")  
    plt.xlabel("Window Influence")
    plt.title('Windows Influence anaylsis')
    
    plt_save_name = os.path.join(args.save_path, 'W_I_analysis.png')
    plt.savefig(plt_save_name, dpi=1000)
    
    slr_data.boxplot(rot=45)
    plt.ylabel("AUC")  
    plt.xlabel("Scale lr")
    plt.title('Scale Learning-Rate anaylsis')
    
    plt_save_name = os.path.join(args.save_path, 'slr_analysis.png') 
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

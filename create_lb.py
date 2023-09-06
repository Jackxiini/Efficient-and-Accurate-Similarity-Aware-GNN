import numpy as np
import time
from tslearn import metrics
import argparse
import os

output_dir = './tmp'

parser = argparse.ArgumentParser(description='LB datasets creator')
parser.add_argument('--dataset', type=str, default='Phoneme',
                    help='dataset name')
args = parser.parse_args()

def get_lb_k(ts1, a = 0.1):
    rad = ts1.shape[0] * a
    envelope_down, envelope_up = metrics.lb_envelope(ts1, radius=rad)
    #lb_k_sim = metrics.lb_keogh(ts2, envelope_candidate=(envelope_down, envelope_up))
    return envelope_down, envelope_up

def get_dtw(ts1, ts2):
    return metrics.dtw(ts1,ts2, global_constraint=None, sakoe_chiba_radius=0.1, itakura_max_slope=None)


if __name__ == "__main__":
    data_name = args.dataset
    result_dir = os.path.join(output_dir, 'ucr_datasets_dtw')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    train = np.loadtxt("./UCR/"+ data_name + '/'+ data_name +"_TRAIN.tsv")
    test = np.loadtxt("./UCR/"+ data_name + '/'+ data_name +"_TEST.tsv")
    comb_data = np.concatenate([train, test], axis = 0)
    dataset = comb_data[:, 1:] #drops label
    arr = np.zeros((dataset.shape[0], dataset.shape[0]))
    start = time.time()
    for i, ts_1 in enumerate(dataset):
        envelope_down, envelope_up = get_lb_k(ts_1, a = 0.05)
        for j, ts_2 in enumerate(dataset):
            arr[i][j] = metrics.lb_keogh(ts_2, envelope_candidate=(envelope_down, envelope_up))
    end = time.time()
    np.save(os.path.join(result_dir, args.dataset), arr)
    print(data_name, end - start)
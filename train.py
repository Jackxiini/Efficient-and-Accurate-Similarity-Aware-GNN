import os
import argparse
import time
import numpy as np
import torch
from src.utils import read_dataset_from_npy, Logger, read_dtw_mt_from_txt
from src.simtsc.model import SimTSC, SimTSCTrainer

ucr_dtw_mt_dir = './UCR'
data_dir = './tmp'
log_dir = './logs'

def train(X, y, train_idx, test_idx, distances, device, logger, K, alpha, epochs=500):
    start_time = time.time()
    nb_classes = len(np.unique(y, axis=0))

    input_size = X.shape[1]

    model = SimTSC(input_size, nb_classes)
    model = model.to(device)
    trainer = SimTSCTrainer(device, logger)

    model, acc, last_acc = trainer.fit(model, X, y, train_idx, distances, K, alpha, test_idx = test_idx, epochs = epochs)
    #acc = trainer.test(model, test_idx)
    end_time = time.time()

    return acc, last_acc, round(end_time - start_time, 4)


def argsparser():
    parser = argparse.ArgumentParser("SimTSC")
    parser.add_argument('--dataset', help='Dataset name', default='Coffee')
    parser.add_argument('--seed', help='Random seed', type=int, default=0)
    parser.add_argument('--gpu', type=str, default='0')
    parser.add_argument('--shot', help='shot', type=int, default=5)
    parser.add_argument('--K', help='K', type=int, default=3)
    parser.add_argument('--alpha', help='alpha', type=float, default=11)
    parser.add_argument('--epochs', help='epochs', type=int, default=500)
    parser.add_argument('--lb', help='If using LB, 1:True, 0:False', type=int, default=1)

    return parser

if __name__ == "__main__":
    # Get the arguments
    parser = argsparser()
    args = parser.parse_args()

    # Setup the gpu
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        print("--> Running on the GPU")
    else:
        device = torch.device("cpu")
        print("--> Running on the CPU")

    # Seeding
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)

    if args.lb == 1:
        dtw_dir = os.path.join(data_dir, 'ucr_datasets_dtw') 
        distances = np.load(os.path.join(dtw_dir, args.dataset+'.npy'))

        out_dir = os.path.join(log_dir, 'simtsc_log_'+str(args.shot)+'_shot_'+str(args.K)+'_'+str(args.alpha)+'_'+str(args.epochs)+'_lb_finetune')  
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        out_path = os.path.join(out_dir, args.dataset+'_'+str(args.seed)+'_shot_'+str(args.shot)+'.txt')  # fix dir problem
        
    else:
        distances = read_dtw_mt_from_txt(ucr_dtw_mt_dir+'/'+args.dataset+'/dtw_mat.txt')

        out_dir = os.path.join(log_dir, 'simtsc_log_'+str(args.shot)+'_shot_'+str(args.K)+'_'+str(args.alpha)+'_'+str(args.epochs))  
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        out_path = os.path.join(out_dir, args.dataset+'_'+str(args.seed)+'_shot_'+str(args.shot)+'.txt')  # fix dir problem

    with open(out_path, 'w') as f:
        logger = Logger(f)
        # Read data
        X, y, train_idx, test_idx = read_dataset_from_npy(os.path.join(data_dir, 'ucr_datasets_'+str(args.shot)+'_shot', args.dataset+'.npy'))

        # Train the model
        acc, last_acc, time_use = train(X, y, train_idx, test_idx, distances, device, logger, args.K, args.alpha, epochs=args.epochs)
        for ep in range(len(acc)):
            logger.log('--> {} Epoch {}: Test Accuracy: {:5.4f}'.format(args.dataset, 100*(ep+1), acc[ep]))
            logger.log(str(acc[ep]))
        #logger.log(str(last_acc))
        logger.log(str(time_use))

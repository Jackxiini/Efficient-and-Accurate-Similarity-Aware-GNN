# LB-SimTSC

## This repo is for the paper [[paper]](https://arxiv.org/abs/2301.04838) which is accepted by DLG-AAAI'23

### Quick Start 
1. Install required packages:
``` 
pip install -r requirements.txt
```
2. Prepare few shot datasets:
``` 
sh create_dataset.sh
```
3. Train DTW-1NN:
```
sh train_knn.sh
```
4. Train LB-SimTSC:
```
sh train_simtsc.sh
```

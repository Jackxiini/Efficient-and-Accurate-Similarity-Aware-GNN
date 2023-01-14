# LBSimTSC

We propose a new efficient semi-supervised time series classification technique, LB-SimTSC, with a new graph construction module. Instead of using DTW, we propose to utilize a lower bound of DTW, LB_Keogh, to approximate the dissimilarity between instances in linear time, while retaining the relative proximity relationships one would have obtained via computing DTW. We construct the pairwise distance matrix using LB_Keogh and build a graph for the graph neural network. We apply this approach to the ten largest datasets from the well-known UCR time series classification archive. The results demonstrate that this approach can be up to 104x faster than SimTSC when constructing the graph on large datasets without significantly decreasing classification accuracy.

## :tada: Our paper is accepted by DLG-AAAI'23 [[paper]](https://arxiv.org/abs/2301.04838)

### Quick Start 
1. Install required packages:
``` 
pip install -r requirements.txt
```
2. Prepare few shot datasets:
``` 
sh create_dataset.sh
```
3. Train for DTW-1NN:
```
sh train_knn.sh
```
4. Train for SimTSC:
```
sh train_simtsc.sh
```

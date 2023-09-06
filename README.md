# LB-SimTSC
SimTSC is a novel method for time series classification that uses a graph neural network classification model based on pairwise Dynamic Time Warping (DTW) distances. Despite its high accuracy, its quadratic complexity makes it suitable only for moderately-sized datasets. To overcome this limitation, a new method, LB-SimTSC, is introduced. Instead of using the computationally intensive DTW, LB-SimTSC employs the LB Keogh lower bound to approximate time series dissimilarity in linear time, preserving important proximity relationships. Experiments on ten largest datasets from the UCR time series classification archive demonstrate that LB-SimTSC is up to 104x faster than SimTSC in graph construction, with minimal loss in classification accuracy.

## The [[paper]](https://arxiv.org/abs/2301.04838) is accepted by DLG-AAAI'23

### Dataset
We use UCR Time Series Classification Archive. You can download the full UCR datasets from [[here]](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/).

### Quick Start 
1. Install required packages:
``` 
pip install -r requirements.txt
```
2. Prepare few shot datasets:
``` 
python create_dataset.py --dataset [DATASET] --shot [SHOT] --seed [SEED]
```
3. Prepare LB pairwise matrix:
``` 
python create_lb.py --dataset [DATASET]
```
4. Train LB-SimTSC:
```
python train_lbsimtsc.py --dataset [DATASET] --shot [SHOT]
```

### Cite this work
```
@article{xi2023lb,
  title={LB-SimTSC: An Efficient Similarity-Aware Graph Neural Network for Semi-Supervised Time Series Classification},
  author={Xi, Wenjie and Jain, Arnav and Zhang, Li and Lin, Jessica},
  journal={arXiv preprint arXiv:2301.04838},
  year={2023}
}
```

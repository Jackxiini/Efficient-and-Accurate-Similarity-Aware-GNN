# LBSimTSC
### 🛠 Updates
#### 8/31/2022 -- Wenjie 
- Created .sh files for few shot dataset creation, DTW-1NN training and SimTSC training
- Added a function in [utils.py](src/utils.py) to read data from txt files
- Added a new argument `epochs` to [train_simtsc.py](train_simtsc.py)
- Fixed directory problems in [train_simtsc.py](train_simtsc.py), added more information to folder name and file name to differentiate each experiment
- Changed how files are read in [train_simtsc.py](train_simtsc.py) and [train_knn.py](train_knn.py) (npy --> txt); ~~This part needs to be changed back in the future~~ (Completed)
- Uploaded some samples for [logs](logs) and [tmp](tmp)
    - [logs folder](logs) includes knn results for 1-shot and 5-shot, and SimTSC results for 1-shot and 5-shot, the last number of the folder indicates the number of epochs (samples are for 500 epochs)
    - [tmp folder](tmp) includes the generated 1-shot dataset and 5-shot dataset (npy files)
- Fixed a small problem in [model.py](model.py) (line 57) which pops a type error

#### 9/1/2022 -- Wenjie
- Uploaded [knn_res.csv](logs/knn_res.csv) for all results of 1-shot and 5-shot of DTW-1NN
- Uploaded [simtsc_res_1_shot.csv](logs/simtsc_res_1_shot.csv) for trying different epochs (100, 300, 500) for SimTSC on 20 UCR datasets
- Added timer

#### 9/2/2022 -- Wenjie
- [create_dataset.sh](create_dataset.sh) now can generate datasets from 1 to 30 (1, 5, 10, 15, 20, 25, 30) shots
- Uploaded [all_res.xlsx](all_res.xlsx) to show all obtained results, **this will be continually updated**

#### 9/3/2022 -- Wenjie
- Uploaded [tools](tools) folder, with [UCR_names.txt](tools/UCR_names.txt), which contains 128 UCR dataset names, arranged in ascending order of the total number of training set and test set instances.
- Added a new argument `lb` to [train_simtsc.py](train_simtsc.py) and modified some code to read datasets of different file types depending on the value of argument
- Added `seeds` to [create_dataset.sh](create_dataset.sh) and `if_lb` to [train_simtsc.sh](train_simtsc.sh)

#### 9/4/2022 -- Wenjie
- Fixed a problem in [train_simtsc.sh](train_simtsc.sh) and [train_simtsc.py](train_simtsc.py), now using 'if_lb=1' for LB and 'if_lb=0' for DTW

#### 9/7/2022 -- Wenjie
- Fixed a problem in generating DTW matrix, need to run experiments again

#### 9/9/2022 -- Wenjie
- Uploaded [wilcoxon_test.ipynb](tools/wilcoxon_test.ipynb) for Wilcoxon signed-rank test and [train_simtsc_fine_tune.sh](train_simtsc_fine_tune.sh) for fine-tuning

#### 9/10/2022 --Wenjie
- Modified [model.py](src/simtsc/model.py) and [train_simtsc.py](train_simtsc.py). Now the model will report test accuracy every 100 epochs and record them into log file

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

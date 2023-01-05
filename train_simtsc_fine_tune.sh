if_lb=1
for i in {'OliveOil','Wine','Car','ACSF1','ShapeletSim','PigAirwayPressure','Fish','Adiac','SemgHandMovementCh2','FiftyWords','UWaveGestureLibraryY','TwoPatterns'}
    do
        python train_simtsc.py --dataset ${i[@]} --shot 10 --epochs 200 --lb $if_lb --K 5 --alpha 1
        python train_simtsc.py --dataset ${i[@]} --shot 20 --epochs 200 --lb $if_lb --K 5 --alpha 1
    done
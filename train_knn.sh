for i in {'BeetleFly','BirdChicken','Coffee','Beef','OliveOil','Rock','PickupGestureWiimoteZ','ShakeGestureWiimoteZ','Wine','FaceFour','Car','Meat','Lightning2','Herring','Lightning7','DodgerLoopGame','DodgerLoopWeekend','DodgerLoopDay','HouseTwenty','ToeSegmentation2','BME','UMD','ShapeletSim','GunPoint','ECG200','Trace','ACSF1','Fungi','Plane','ArrowHead','Ham','Worms','WormsTwoClass','InsectEPGSmallTrain','ToeSegmentation1','SmoothSubspace','GesturePebbleZ1','GesturePebbleZ2','InsectEPGRegularTrain','PigAirwayPressure','PigArtPressure','PigCVP','DiatomSizeReduction','GestureMidAirD1','GestureMidAirD2','GestureMidAirD3','Fish','PowerCons','Chinatown','OSULeaf','GunPointAgeSpan','GunPointMaleVersusFemale','GunPointOldVersusYoung','Earthquakes','Haptics','Computers','DistalPhalanxOutlineAgeGroup','DistalPhalanxTW','MiddlePhalanxTW','MiddlePhalanxOutlineAgeGroup','SyntheticControl','ProximalPhalanxOutlineAgeGroup','ProximalPhalanxTW','SonyAIBORobotSurface1','InlineSkate','EOGHorizontalSignal','EOGVerticalSignal','LargeKitchenAppliances','RefrigerationDevices','ScreenType','SmallKitchenAppliances','CricketX','CricketY','CricketZ','Adiac','DistalPhalanxOutlineCorrect','ECGFiveDays','MiddlePhalanxOutlineCorrect','ProximalPhalanxOutlineCorrect','SemgHandGenderCh2','SemgHandMovementCh2','SemgHandSubjectCh2','WordSynonyms','FiftyWords','CBF','SonyAIBORobotSurface2','Strawberry','AllGestureWiimoteX','AllGestureWiimoteY','AllGestureWiimoteZ','EthanolLevel','Symbols','PLAID','ItalyPowerDemand','SwedishLeaf','MedicalImages','TwoLeadECG','ShapesAll','MoteStrain','HandOutlines','CinCECGTorso','Phoneme','InsectWingbeatSound','FacesUCR','FaceAll','Mallat','MixedShapesSmallTrain','PhalangesOutlinesCorrect','FreezerSmallTrain','MixedShapesRegularTrain','FreezerRegularTrain','Yoga','MelbournePedestrian','NonInvasiveFetalECGThorax1','NonInvasiveFetalECGThorax2','ChlorineConcentration','FordB','UWaveGestureLibraryAll','UWaveGestureLibraryX','UWaveGestureLibraryY','UWaveGestureLibraryZ','FordA','ECG5000','TwoPatterns','Wafer','StarLightCurves','ElectricDevices','Crop'}
    do
        #python train_knn.py --dataset $i --shot 1
        #python train_knn.py --dataset $i --shot 5
        python train_knn.py --dataset ${i[@]} --shot 10
        python train_knn.py --dataset ${i[@]} --shot 15
        python train_knn.py --dataset ${i[@]} --shot 20
        python train_knn.py --dataset ${i[@]} --shot 25
        python train_knn.py --dataset ${i[@]} --shot 30
    done
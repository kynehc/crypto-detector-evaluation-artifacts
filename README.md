# crypto-detectors-evaluation-artifacts

The artifacts contain all reported alarms from evaluated detectors, analysis results of labeled alarms, and refined CryptoGuard as well as false positive examples.

### Major Claims

(C1): We analyzed sampled false alarms from evaluated detectors, and show various false alarm patterns exist.

(C2): We implemented this refinement in CryptoGuard, rerun it on the app data set, and found a large number of FPs for rules 1– 3, 8, 10, 12–13 because of the same root cause, as shown in Table IV.


### Evaluation

(E1): The [E1-instruction.md](./E1-instructions.md) explains which false alarm cases support the false alarm patterns shown in the paper. 


(E2): The [E2-instruction.md](./E2-instructions.md) explains the procedure for conducting a scale-down experiment comparing the original CryptoGuard with the refined CryptoGuard.


### Availability of original dataset

Our original datasets consist of a data set of 3,489 open-source Android apps obtained from F-Droid, and a data set of 1,437 firmwares collected from 6 vendors.

Due to the large size of the two datasets (APK dataset: 49 GB, firmware dataset: 21 GB), it is difficult to share them online. If you are interested in obtaining the original F-Droid dataset and firmware dataset, please contact us.
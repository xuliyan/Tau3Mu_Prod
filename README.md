# BaconProd
Tau3Mu analysis: Simple TTree  production. Runs on AOD. Current setup uses CMSSW_8_0_27.

Use config file crab/makingBaconPuppiMVAMets_MC.py to run

Files used to generate std::vector<std::bitset<256> > dictionary are located in /afs/cern.ch/work/x/xuyan/work4/CMSSW_8_0_27/src/BaconProd/Ntupler/plugins. Read the README there.

Check if the Trigger Muon selecion is properly set (FillerMuon.cc L:587)

Check if trkID is properly set (FillerMuon.cc L:426)
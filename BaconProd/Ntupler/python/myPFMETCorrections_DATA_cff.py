import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectors_cff import *

corrPfMetType1 = cms.EDProducer(
    "PFJetMETcorrInputProducer",
    src = cms.InputTag("ak4PFJetsCHS"),
    offsetCorrLabel = cms.InputTag("ak4PFCHSL1FastjetCorrector"),
    jetCorrLabel = cms.InputTag("ak4PFCHSL1FastL2L3ResidualCorrector"), # NOTE: use "ak4PFL1FastL2L3Corrector" for MC / "ak4PFL1FastL2L3ResidualCorrector" for Data
    #jetCorrEtaMax = cms.double(9.9),
    jetCorrEtaMax = cms.double(9.9),
    type1JetPtThreshold = cms.double(10.0),
    skipEM = cms.bool(True),
    skipEMfractionThreshold = cms.double(0.90),
    skipMuons = cms.bool(True),
    skipMuonSelection = cms.string("isGlobalMuon | isStandAloneMuon")
)

pfMetT1 = cms.EDProducer(
    "AddCorrectionsToPFMET",
    src = cms.InputTag('pfMet30'),
    jetCorrEtaMax = cms.double(3.0),
    srcCorrections = cms.VInputTag(
        cms.InputTag('corrPfMetType1', 'type1')
    ),
)   

#-------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# define sequence to run all modules
producePFMETCorrections = cms.Sequence(
    ak4PFCHSL1FastL2L3ResidualCorrectorChain
    * corrPfMetType1
    * pfMetT1
)
#--------------------------------------------------------------------------------
#Puppi
pfJetMETcorrPuppi = corrPfMetType1.clone(
    src = 'ak4PFJetsPuppi',
    jetCorrLabel = 'ak4PuppiL1FastL2L3ResidualCorrector',
    offsetCorrLabel = 'ak4PuppiL1FastjetCorrector',
    type1JetPtThreshold = cms.double(20)
    )

pfType1PuppiCorrectedMet = pfMetT1.clone(
    src = cms.InputTag('pfMetPuppi'),
     srcCorrections = cms.VInputTag(
        cms.InputTag('pfJetMETcorrPuppi', 'type1')
        ),
    )

producePFMETCorrectionsPuppiData = cms.Sequence(
    pfJetMETcorrPuppi 
    *pfType1PuppiCorrectedMet
)

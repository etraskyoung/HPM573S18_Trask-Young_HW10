import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating mono therapy
# create a cohorts
cohort_None = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_None = cohort_None.simulate()

# simulating combination therapy
# create a cohort
cohort_Anticoag = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAG)
# simulate the cohort
simOutputs_Anticoag = cohort_Anticoag.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_None, simOutputs_Anticoag)

# print the estimates for the mean survival time and mean time to AIDS
SupportMarkov.print_outcomes(simOutputs_None, "No Therapy:")
SupportMarkov.print_outcomes(simOutputs_Anticoag, "Anticoagulation Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_None, simOutputs_Anticoag)

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_None, simOutputs_Anticoag)

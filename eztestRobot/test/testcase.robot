| *** Settings *** |
| Library | ${ROBOTHOME}/OSHelper.py |
| Suite Setup | Combined Setup |
| Force Tags | test |
| Test Timeout | ${ROBOT_TEST_TIMEOUT} |

| *** Keywords *** |
| Combined Setup |
|  | Shell Command | echo Start Testing ... 
|  | Shell Command | rm \$DS_WORK/*.* 
|  | Change Working Directory | \${runtest}/positive 
|  | Replace Env | openhub.atl | \${DS_WORK}/openhub_4.0_Dec_1_2011.atl 
|  | Shell Command | al_engine \${al_engine_param} -U\$REPOID -P\$REPOPW -f\${DS_WORK}/openhub_4.0_Dec_1_2011.atl -z\${runtest}/work/openhub_4.0_Dec_1_2011.txt -passphrasedsplatform 
|  | Shell Command | al_engine \${al_engine_param} -U\$REPOID -P\$REPOPW -fsubstitution_parameters_openhub_4.0.atl -z\${runtest}/work/substitution_parameters_openhub_4.0.txt -passphrasedsplatform 

| *** Test Cases *** |
| openhub01 |
|  | EIM Launcher | openhub01_script 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub01.out | \${DS_WORK}/openhub01.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub02 |
|  | EIM Launcher | openhub02_table32 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub_table32.out | \${DS_WORK}/openhub_table32.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub03 |
|  | EIM Launcher | openhub03_table32 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub03_table32.out | \${DS_WORK}/openhub03_table32.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub04 |
|  | EIM Launcher | openhub04_subsparam 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub04_subsparam.out | \${DS_WORK}/openhub04_subsparam.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub05 |
|  | EIM Launcher | openhub05_changedest 
|  | Shell Command | sleep 120 
|  | Diff Unordered Files | \${runtest}/goldlog/openhub12.out | \${DS_WORK}/openhub12.out 

| openhub06 |
|  | EIM Launcher | openhub06_readparallel 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub12_read1.out | \${DS_WORK}/openhub12_read1.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub12_read2.out | \${DS_WORK}/openhub12_read2.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub07 |
|  | ${result} = | EIM Launcher | openhub07_multpc 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub08 |
|  | ${result} = | EIM Launcher | openhub08_subsparam 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub09 |
|  | ${result} = | EIM Launcher | openhub09_multpc2 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub10 |
|  | EIM Launcher | openhub10_where 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub10_where.out | \${DS_WORK}/openhub10_where.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub11 |
|  | EIM Launcher | openhub11_groupby 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub11_groupby.out | \${DS_WORK}/openhub11_groupby.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub13 |
|  | EIM Launcher | openhub13_packets 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub13_packets_16.out | \${DS_WORK}/openhub13_packets_16.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub14 |
|  | EIM Launcher | openhub14_PCinsequence 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub_table342.out | \${DS_WORK}/openhub_table342.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub13_packets_16.out | \${DS_WORK}/openhub13_packets_16.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub15a |
|  | EIM Launcher | openhub15_parallelwf 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub15_parallel1.out | \${DS_WORK}/openhub15_parallel1.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub15_parallel2.out | \${DS_WORK}/openhub15_parallel2.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub15 |
|  | EIM Launcher | openhub15_samedf 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub15_1.out | \${DS_WORK}/openhub15_1.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub15_2.out | \${DS_WORK}/openhub15_2.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub15_3.out | \${DS_WORK}/openhub15_3.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub16 |
|  | EIM Launcher | openhub16_read2tables 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub13_packets_16.out | \${DS_WORK}/openhub13_packets_16.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub_16_2.out | \${DS_WORK}/openhub_16_2.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub17 |
|  | EIM Launcher | openhub17_scriptreader 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub01.out | \${DS_WORK}/openhub01.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub03_table32.out | \${DS_WORK}/openhub03_table32.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub18 |
|  | EIM Launcher | openhub18_join 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub18_join.out | \${DS_WORK}/openhub18_join.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub19 |
|  | EIM Launcher | openhub19_delta 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub19_delta.out | \${DS_WORK}/openhub19_delta.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub20 |
|  | EIM Launcher | openhub20_lesscolumns 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub20_lesscolumns.out | \${DS_WORK}/openhub20_lesscolumns.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub22 |
|  | EIM Launcher | openhub22_diffschema 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/oherr03_difftable.out | \${DS_WORK}/oherr03_difftable.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub22a |
|  | EIM Launcher | openhub22_table13 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub13.out | \${DS_WORK}/openhub13.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub23 |
|  | ${result} = | EIM Launcher | openhub23_optionalfields 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub24 |
|  | ${result} = | EIM Launcher | openhub24_audit 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub25 |
|  | EIM Launcher | openhub25_emb 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub25_emb.out | \${DS_WORK}/openhub25_emb.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub26 |
|  | EIM Launcher | openhub26_emb 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub26_emb.out | \${DS_WORK}/openhub26_emb.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub27 |
|  | EIM Launcher | openhub27_subsparam1 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub01.out | \${DS_WORK}/openhub01.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub28 |
|  | EIM Launcher | openhub28_readinparallel 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub03_table32.out | \${DS_WORK}/openhub03_table32.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub_table342.out | \${DS_WORK}/openhub_table342.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| openhub29 |
|  | EIM Launcher | openhub29_table32full 
|  | Shell Command | sleep 120 
|  | ${result} = | Shell Command | du \${DS_WORK}/openhub30_errordtp2.out \| awk '{ print \$1 }' 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | 0 

| openhub30 |
|  | EIM Launcher | openhub30_witherrordtp 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub30_errordtp1.out | \${DS_WORK}/openhub30_errordtp1.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Shell Command | du \${DS_WORK}/openhub30_errordtp2.out \| awk '{ print \$1 }' 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | 0 

| openhub31 |
|  | EIM Launcher | openhub31_parallelsamerfc 
|  | Shell Command | sleep 120 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub_table342.out | \${DS_WORK}/openhub_table342.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/openhub20_lesscolumns.out | \${DS_WORK}/openhub20_lesscolumns.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 


| *** Variables *** |

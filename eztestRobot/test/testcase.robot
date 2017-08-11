| *** Settings *** |
| Library | ${ROBOTHOME}/OSHelper.py |
| Suite Setup | Combined Setup |
| Force Tags | test |
| Test Timeout | ${ROBOT_TEST_TIMEOUT} |

| *** Keywords *** |
| Combined Setup |
|  | Shell Command | mkdir \${DS_WORK} 
|  | Shell Command | mkdir \${DS_GOLD} 
|  | Shell Command | mkdir \${DS_INPUT} 
|  | Shell Command | rm \${DS_WORK}/* 
|  | Shell Command | rm \${DS_GOLD}/* 
|  | Shell Command | rm \${DS_INPUT}/* 
|  | Shell Command | cp \${runtest}/goldlog/* \${DS_GOLD} 
|  | Shell Command | cp \${runtest}/input/* \${DS_INPUT} 
|  | Change Working Directory | \${runtest}/positive 
|  | Import ATL | ezTest_HANA_BulkLoad_Datastore.atl 
|  | Import ATL | HANA_BulkLoad_Functional_Unit.atl 
|  | Import ATL | SubstitutionParam__Signatured.atl 
|  | Import ATL | sysconfig.atl 

| *** Test Cases *** |
| hana001 |
|  | [Documentation] | 001__HANA_BKL_DDL_CreateTables 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -k'HANA 1.x' | -s"hana 2.x"
|  | ${result} = | Shell Command | grep -o "Job <\${JOBNAME}> is completed successfully." \${DS_WORK}/\${JOBNAME}.log 
|  | Run Keyword If | $result is not None | Should Contain | ${result} | successfully 
|  | Unset | test 
|  | Unset | test1 

| hana002 |
|  | [Documentation] | 100_HANA_BKL_Gen_Inp_DataSet 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/100_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana003 |
|  | [Documentation] | 101_HANA_BKL_AutoCorrect_Insert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/101_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana004 |
|  | [Documentation] | 102_HANA_BKL_AutoCorrect_Update 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/102_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana005 |
|  | [Documentation] | 103_HANA_BKL_AutoCorrect_DeleteInsert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/103_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana006 |
|  | [Documentation] | 104_HANA_BKL_DeleteInsert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/104_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana007 |
|  | [Documentation] | 105_HANA_BKL_Update 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/105_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana008 |
|  | [Documentation] | 106_HANA_BKL_Delete 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/106_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana009 |
|  | [Documentation] | 002__HANA_BKL_DDL_2_RowBase 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Shell Command | grep -o "Job <\${JOBNAME}> is completed successfully." \${DS_WORK}/\${JOBNAME}.log 
|  | Run Keyword If | $result is not None | Should Contain | ${result} | successfully 

| hana009 |
|  | [Documentation] | 100_HANA_BKL_Gen_Inp_DataSet 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/100_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana010 |
|  | [Documentation] | 101_HANA_BKL_AutoCorrect_Insert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/101_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana011 |
|  | [Documentation] | 102_HANA_BKL_AutoCorrect_Update 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/102_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| haan012 |
|  | [Documentation] | 103_HANA_BKL_AutoCorrect_DeleteInsert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/103_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana013 |
|  | [Documentation] | 104_HANA_BKL_DeleteInsert 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/104_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana014 |
|  | [Documentation] | 105_HANA_BKL_Update 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/105_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 

| hana015 |
|  | [Documentation] | 106_HANA_BKL_Delete 
|  | Shell Command | rm \${DS_WORK}/HANA_BKL_Job.out 
|  | Unset | JOBNAME 
|  | EIM Launcher | \${JOBNAME} | -KspS1 -T2062 -l\${UDS_WORK}/\${JOBNAME}.log -z\${UDS_WORK}/\${JOBNAME}.txt
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/106_HANA_BKL_Glod.out | \${DS_WORK}/HANA_BKL_Job.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | Shell Command | cut -c38-200 \${DS_WORK}/\${JOBNAME}.log \| tr -d '\r' 


| *** Variables *** |

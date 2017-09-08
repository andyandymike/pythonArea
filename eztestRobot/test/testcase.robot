| *** Settings *** |
| Library | ${ROBOTHOME}/OSHelper.py |
| Suite Setup | Combined Setup |
| Force Tags | test |
| Test Timeout | ${ROBOT_TEST_TIMEOUT} |

| *** Keywords *** |
| Combined Setup |
|  | Shell Command | echo Start Testing ... 
|  | Shell Command | rm -rf \${DS_WORK}/* 
|  | Shell Command | mkdir \${DS_WORK} 
|  | Shell Command | chmod -R 777 \${DS_WORK} 
|  | Change Working Directory | \${runtest}/positive 
|  | Import ATL | ds_atl.atl 
|  | Import ATL | table_atl.atl 
|  | Import ATL | hanacalcjoinview_jobs.atl 
|  | Import ATL | HANA_CalcJoinView_AT_MATERIAL.atl 

| *** Test Cases *** |
| tcase001 |
|  | [Documentation] | AN_CUSTOMER_LINE_ITEM 
|  | Export Env | JOBNAME | AN_CUSTOMER_LINE_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/test space/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase002 |
|  | [Documentation] | AN_CUSTOMER_LINE_ITEM_CR 
|  | Export Env | JOBNAME | AN_CUSTOMER_LINE_ITEM_CR 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase003 |
|  | [Documentation] | AN_OVERDUE_ITEM_ANALYSIS 
|  | Export Env | JOBNAME | AN_OVERDUE_ITEM_ANALYSIS 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase004 |
|  | [Documentation] | AN_OVERDUE_ITEM_ANALYSIS_DA 
|  | Export Env | JOBNAME | AN_OVERDUE_ITEM_ANALYSIS_DA 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase005 |
|  | [Documentation] | AN_VENDOR_LINE_ITEM 
|  | Export Env | JOBNAME | AN_VENDOR_LINE_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase006 |
|  | [Documentation] | AN_VENDOR_LINE_ITEM_CR 
|  | Export Env | JOBNAME | AN_VENDOR_LINE_ITEM_CR 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase007 |
|  | [Documentation] | AT_LEDGER_GL 
|  | Export Env | JOBNAME | AT_LEDGER_GL 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase008 |
|  | [Documentation] | AT_NEW_GL_LINE_ITEM 
|  | Export Env | JOBNAME | AT_NEW_GL_LINE_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase009 |
|  | [Documentation] | AT_BUSINESS_AREA 
|  | Export Env | JOBNAME | AT_BUSINESS_AREA 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase010 |
|  | [Documentation] | AT_CCY_GL_ASSIGNMENT 
|  | Export Env | JOBNAME | AT_CCY_GL_ASSIGNMENT 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase011 |
|  | [Documentation] | AT_CLIENT 
|  | Export Env | JOBNAME | AT_CLIENT 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase012 |
|  | [Documentation] | AT_CUSTOMER_COMPANY_CODE_FIN 
|  | Export Env | JOBNAME | AT_CUSTOMER_COMPANY_CODE_FIN 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase013 |
|  | [Documentation] | AT_DOCUMENT_STATUS_FIN 
|  | Export Env | JOBNAME | AT_DOCUMENT_STATUS_FIN 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase014 |
|  | [Documentation] | AT_GLOBAL_COMPANY 
|  | Export Env | JOBNAME | AT_GLOBAL_COMPANY 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase015 |
|  | [Documentation] | AT_VENDOR_COMPANY_CODE_FIN 
|  | Export Env | JOBNAME | AT_VENDOR_COMPANY_CODE_FIN 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase016 |
|  | [Documentation] | AT_MATERIAL_VALUATED_STOCK 
|  | Export Env | JOBNAME | AT_MATERIAL_VALUATED_STOCK 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase017 |
|  | [Documentation] | AT_MATERIAL_VALUATION 
|  | Export Env | JOBNAME | AT_MATERIAL_VALUATION 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase018 |
|  | [Documentation] | AT_COMPANY_CODE 
|  | Export Env | JOBNAME | AT_COMPANY_CODE 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase019 |
|  | [Documentation] | AT_CURRENCY_KEY 
|  | Export Env | JOBNAME | AT_CURRENCY_KEY 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase020 |
|  | [Documentation] | AT_CUSTOMER 
|  | Export Env | JOBNAME | AT_CUSTOMER 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase021 |
|  | [Documentation] | AT_CUSTOMER_BASIC 
|  | Export Env | JOBNAME | AT_CUSTOMER_BASIC 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase022 |
|  | [Documentation] | AT_DEBIT_CREDIT_INDICATOR 
|  | Export Env | JOBNAME | AT_DEBIT_CREDIT_INDICATOR 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase023 |
|  | [Documentation] | AT_MATERIAL 
|  | Export Env | JOBNAME | AT_MATERIAL 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase024 |
|  | [Documentation] | AT_MATERIAL_BASIC 
|  | Export Env | JOBNAME | AT_MATERIAL_BASIC 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase025 |
|  | [Documentation] | AT_MATERIAL_DESC 
|  | Export Env | JOBNAME | AT_MATERIAL_DESC 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase026 |
|  | [Documentation] | AT_MATERIAL_GROUP 
|  | Export Env | JOBNAME | AT_MATERIAL_GROUP 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase027 |
|  | [Documentation] | AT_MEASURE_UNIT 
|  | Export Env | JOBNAME | AT_MEASURE_UNIT 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase028 |
|  | [Documentation] | AT_PLANT 
|  | Export Env | JOBNAME | AT_PLANT 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase029 |
|  | [Documentation] | AT_STORAGE_LOCATION 
|  | Export Env | JOBNAME | AT_STORAGE_LOCATION 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase030 |
|  | [Documentation] | AT_TIME 
|  | Export Env | JOBNAME | AT_TIME 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase031 |
|  | [Documentation] | AT_VENDOR 
|  | Export Env | JOBNAME | AT_VENDOR 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase032 |
|  | [Documentation] | AT_VENDOR_BASIC 
|  | Export Env | JOBNAME | AT_VENDOR_BASIC 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase033 |
|  | [Documentation] | AT_VENDOR_COMPANY_CODE 
|  | Export Env | JOBNAME | AT_VENDOR_COMPANY_CODE 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase034 |
|  | [Documentation] | AT_VENDOR_PURCHASE_ORG 
|  | Export Env | JOBNAME | AT_VENDOR_PURCHASE_ORG 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase035 |
|  | [Documentation] | AT_FS_CHART_OF_ACCOUNTS 
|  | Export Env | JOBNAME | AT_FS_CHART_OF_ACCOUNTS 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase036 |
|  | [Documentation] | AT_FS_PO_HEADER 
|  | Export Env | JOBNAME | AT_FS_PO_HEADER 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase037 |
|  | [Documentation] | AT_FS_VENDOR_BSAK 
|  | Export Env | JOBNAME | AT_FS_VENDOR_BSAK 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase038 |
|  | [Documentation] | AT_FS_VENDOR_BSIK 
|  | Export Env | JOBNAME | AT_FS_VENDOR_BSIK 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase039 |
|  | [Documentation] | AT_LOGISTICS_INVOICE_HEADER 
|  | Export Env | JOBNAME | AT_LOGISTICS_INVOICE_HEADER 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase040 |
|  | [Documentation] | AT_MOVEMENT_TYPE 
|  | Export Env | JOBNAME | AT_MOVEMENT_TYPE 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase041 |
|  | [Documentation] | AT_PLANT_COMP_CODE 
|  | Export Env | JOBNAME | AT_PLANT_COMP_CODE 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase042 |
|  | [Documentation] | AT_PO_HEADER_ORG_DATA 
|  | Export Env | JOBNAME | AT_PO_HEADER_ORG_DATA 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase043 |
|  | [Documentation] | AT_PO_ITEM 
|  | Export Env | JOBNAME | AT_PO_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase044 |
|  | [Documentation] | AT_PO_ITEM_CATEGORY 
|  | Export Env | JOBNAME | AT_PO_ITEM_CATEGORY 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase045 |
|  | [Documentation] | AT_PURCHASING_DOCUMENT_TYPE 
|  | Export Env | JOBNAME | AT_PURCHASING_DOCUMENT_TYPE 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase046 |
|  | [Documentation] | AT_PURCH_GRP 
|  | Export Env | JOBNAME | AT_PURCH_GRP 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase047 |
|  | [Documentation] | AT_PURCH_ORG 
|  | Export Env | JOBNAME | AT_PURCH_ORG 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase048 |
|  | [Documentation] | AT_VENDOR_BASIC_FOR_CALC 
|  | Export Env | JOBNAME | AT_VENDOR_BASIC_FOR_CALC 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase049 |
|  | [Documentation] | AT_DIS_CHANNEL 
|  | Export Env | JOBNAME | AT_DIS_CHANNEL 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase050 |
|  | [Documentation] | AT_SALES_DISTRICT 
|  | Export Env | JOBNAME | AT_SALES_DISTRICT 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase051 |
|  | [Documentation] | AT_SALES_DIVISION 
|  | Export Env | JOBNAME | AT_SALES_DIVISION 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase052 |
|  | [Documentation] | AT_SALES_ORG 
|  | Export Env | JOBNAME | AT_SALES_ORG 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase053 |
|  | [Documentation] | AT_STAT_DELIVERY_HEADER 
|  | Export Env | JOBNAME | AT_STAT_DELIVERY_HEADER 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase054 |
|  | [Documentation] | AT_STAT_DELIVERY_ITEM 
|  | Export Env | JOBNAME | AT_STAT_DELIVERY_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase055 |
|  | [Documentation] | AT_STAT_DEL_BILLING 
|  | Export Env | JOBNAME | AT_STAT_DEL_BILLING 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase056 |
|  | [Documentation] | AT_STAT_HEADER 
|  | Export Env | JOBNAME | AT_STAT_HEADER 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase057 |
|  | [Documentation] | AT_STAT_ITEM 
|  | Export Env | JOBNAME | AT_STAT_ITEM 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 

| tcase058 |
|  | [Documentation] | AT_STAT_ORD_BILLING 
|  | Export Env | JOBNAME | AT_STAT_ORD_BILLING 
|  | EIM Launcher | HANA_CalcJoinView_\${JOBNAME} 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}.out | \${DS_WORK}/\${JOBNAME}.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 
|  | ${result} = | Diff Unordered Files | \${runtest}/goldlog/\${JOBNAME}_NS.out | \${DS_WORK}/\${JOBNAME}_NS.out 
|  | Run Keyword If | $result is not None | Should Not Contain | ${result} | Failed 


| *** Variables *** |

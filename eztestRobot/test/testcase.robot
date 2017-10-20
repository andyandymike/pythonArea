| *** Settings *** |
| Library | ${ROBOTHOME}/OSHelper.py |
| Suite Setup | Combined Setup |
| Force Tags | test |
| Test Timeout | ${ROBOT_TEST_TIMEOUT} |

| *** Keywords *** |
| Initialize_DB |
|  | Export Env | WORK_DIR | \${runtest}/work_\$RUNTYPE 
|  | Shell Command | echo ">>>> WORK Directory.... "  \$WORK_DIR 
|  | Export Env | DBDDLLOC | \${runtest}/scripts 
|  | Shell Command | echo ">>> Database DDL Location : " \$DBDDLLOC 
|  | Replace Env | \${runtest}/positive/sqlfile_MC.atl      | \$WORK_DIR/tsqlfile_MC.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tsqlfile_MC.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/scripts/\$DBUSE/Insert_AW_FIRST_RUN_DATE.sql      | \${WORK_DIR}/tInsert_AW_FIRST_RUN_DATE.sql 
|  | Export Env | JOBNAME | sqlfile_mc 
|  | EIM Launcher | \${JOBNAME} | -Ksp\${SYS_CONFIG}  -l\${WORK_DIR}/\${JOBNAME}_\${RUNTYPE}.log  -z\${WORK_DIR}/\${JOBNAME}_\${RUNTYPE}.txt

| Compares_Files |
|  | Export Env | WORK_DIR | \${runtest}/work_\$RUNTYPE 
|  | Shell Command | echo ">>>> WORK Directory.... "  \$WORK_DIR 
|  | Replace Env | \${runtest}/positive/rm_sapgl_ext.atl      | \$WORK_DIR/trm_sapgl_ext.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/trm_sapgl_ext.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/testcase_compare_files      | \$WORK_DIR/ttestcase_compare_files 
|  | Unset | GVAR 
|  | Export Env | JOBNAME | sapgl_job 
|  | EIM Launcher | \${JOBNAME} | -Ksp\${SYS_CONFIG}  -l\${WORK_DIR}/\${JOBNAME}_\${LOADTYPE}.log  -z\${WORK_DIR}/\${JOBNAME}_\${LOADTYPE}.txt

| Combined Setup |
|  | Shell Command | echo Start Testing ... 
|  | Change Working Directory | \${runtest}/positive 
|  | Shell Command | echo \${runtest} 
|  | Shell Command | echo \${EZTEST_HOME} 
|  | Shell Command | echo \${TESTNODE} 
|  | Shell Command | echo \${QAENV} 
|  | Shell Command | echo \${QAPARAM} 
|  | Shell Command | echo \${al_engine_param}} 
|  | Shell Command | mkdir -p \${runtest}/work_\$RUNTYPE 
|  | Shell Command | chmod 777 \${runtest}/work_\$RUNTYPE 
|  | Export Env | TARGET_DIR | \${runtest}/\$RUNTYPE 
|  | Shell Command | echo ">>>> Target Directory.... "  \$TARGET_DIR 
|  | Export Env | GOLDLOG_DIR | \${runtest}/goldlog 
|  | Shell Command | echo ">>>> GOLDLOG Directory.... "  \$GOLDLOG_DIR 
|  | Export Env | WORK_DIR | \${runtest}/work_\$RUNTYPE 
|  | Shell Command | echo ">>>> WORK Directory.... "  \$WORK_DIR 
|  | Replace Env | \${runtest}/positive/R3_DS.atl      | \$WORK_DIR/tR3_DS.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tR3_DS.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/positive/RM_DS.atl      | \$WORK_DIR/tRM_DS.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tRM_DS.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/positive/files_format.atl      | \$WORK_DIR/tfiles_format.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tfiles_format.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/positive/system_config.atl      | \$WORK_DIR/tsystem_config.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tsystem_config.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/positive/substitution_parms.atl      | \$WORK_DIR/tsubstitution_parms.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tsubstitution_parms.atl  -passphrasedsplatform 
|  | Replace Env | \${runtest}/positive/sap_gl_rm.atl      | \$WORK_DIR/tsap_gl_rm.atl 
|  | Shell Command | al_engine \${al_engine_param}   -f\$WORK_DIR/tsap_gl_rm.atl  -passphrasedsplatform 

| *** Test Cases *** |
| tcase001 |
|  | [Documentation] | \$RUNTYPE_\$LOADTYPE_LOAD 
|  | Run Keyword And Continue On Failure | Initialize_DB |
|  | Shell Command | mkdir -p \${runtest}/\$RUNTYPE 
|  | Shell Command | chmod 777 \${runtest}/\$RUNTYPE 
|  | Shell Command | mkdir -p \${runtest}/work_\$RUNTYPE 
|  | Shell Command | chmod 777 \${runtest}/work_\$RUNTYPE 
|  | Export Env | TARGET_DIR | \${runtest}/\$RUNTYPE 
|  | Shell Command | echo ">>>> Target Directory.... "  \$TARGET_DIR 
|  | Export Env | GOLDLOG_DIR | \${runtest}/goldlog 
|  | Shell Command | echo ">>>> GOLDLOG Directory.... "  \$GOLDLOG_DIR 
|  | Export Env | WORK_DIR | \${runtest}/work_\$RUNTYPE 
|  | Shell Command | echo ">>>> WORK Directory.... "  \$WORK_DIR 
|  | Shell Command | echo ">>>  SYSTEM CONFIG : "  \$SYS_CONFIG 
|  | Shell Command | echo ">>>      LOAD TYPE : "  \$LOADTYPE 
|  | Shell Command | echo ">>>     START DATE : "  \$G_SDATE 
|  | Shell Command | echo ">>>       END DATE : "  \$G_EDATE 
|  | Shell Command | echo ">>>       RUN MODE : "  \$G_RUNMODE 
|  | Shell Command | echo ">>>  ENCODED_GLOADTYPE : "  \$ENCODED_GLOADTYPE 
|  | Shell Command | echo ">>>     ENCODED_SDATE  : "  \$ENCODED_SDATE 
|  | Shell Command | echo ">>>     ENCODED_EDATE  : "  \$ENCODED_EDATE 
|  | Shell Command | echo ">>>  ENCODED_GRUNMODE  : "  \$ENCODED_GRUNMODE 
|  | Export Env | GVAR | "\\\$G_LOAD_TYPE=\$ENCODED_GLOADTYPE;\\\$G_RUN_MODE=\$ENCODED_GRUNMODE;\\\$G_SDATE=\$ENCODED_SDATE;\\\$G_EDATE=\$ENCODED_EDATE" 
|  | Export Env | JOBNAME | \$EXECUTEJOB 
|  | EIM Launcher | \${JOBNAME} | -Ksp\${SYS_CONFIG}  -l\${WORK_DIR}/\${JOBNAME}_\${RUNTYPE}_\${LOADTYPE}.log  -z\${WORK_DIR}/\${JOBNAME}_\${RUNTYPE}_\${LOADTYPE}.txt

| InTestingSetup_0 |
|  | [Tags] | InTestingSetup 
|  | Run Keyword And Continue On Failure | Compares_Files |


| *** Variables *** |

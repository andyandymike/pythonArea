# Variables al_engine_param, Job_Launcher_Param, runengine and Job server info are set before calling
# If runengine is set to "Y" or "y", run job using al_engine
# If runengine is set to "R" or "r", run job using AL_RWJobLauncher first;
#   if the job fails, rerun the job using al_engine
# If runengine is not set, run job using AL_RWJobLauncher
export JOBNAME=$1
shift
export JOB_EXE_OPT=$*
[ -z "$LAUNCHER_DELAY" ] && export LAUNCHER_DELAY=2

echo JOB_EXE_OPT is $JOB_EXE_OPT
echo $DS_WORK

if [ "$Job_Launcher_Param" = "" ]
then
  echo Please set Job_Launcher_Param variable in parameter file!
fi

if [ "$runengine" = "Y" -o "$runengine" = "y" ]
then
	echo "al_engine ${al_engine_param} -s$JOBNAME -Ksp$SYSPROFF $JOB_EXE_OPT $JOB_EXE_OPT2"
	eval al_engine ${al_engine_param} -s$JOBNAME -Ksp$SYSPROF $JOB_EXE_OPT $JOB_EXE_OPT2 -l${unix_runtest}/work/$JOBNAME.log -t${unix_runtest}/work/$JOBNAME.err
	returncode=$?
	if [ $returncode -ne 0 ]
	then
		echo al_engine for job $JOBNAME returns $returncode 
	fi
else
	${JYTHON_CMD} ${ROBOTHOME}/bin/subvalue2.py $QAENV/bin/launcher.txt ${DS_WORK}/tlauncher.txt
	echo '===================================================='
	echo '==  JOb Executed on Server   =='
	echo ' JOB SERVER HOST : ' $JOBSERVERHOST
	echo '      Job Server : ' $JOBSERVERNAME
	echo '            Port : ' $JOBSERVERPORT
	echo '    Job Launcher : ' $Job_Launcher_Param
	echo '----------------------------------------------------'
	echo '      Running Job: ' $JOBNAME
	echo '          Options: ' $JOB_EXE_OPT
	echo '          RUNTEST: ' $runtest
	echo '         LINK_DIR: ' $LINK_DIR

	AL_RWJobLauncher.exe "$DS_COMMON_DIR/log/$JOBSERVERNAME/" -w "inet:$JOBSERVERHOST:$JOBSERVERPORT" -t5 -C "${DS_WORK}/tlauncher.txt"
	returncode=$?
	if [ $returncode -ne 0 ]
	then
		echo AL_RWJobLauncher job $JOBNAME returns $returncode
		if [ "$runengine" = "R" -o "$runengine" = "r" ]
		then
			eval al_engine ${al_engine_param} -s$JOBNAME -Ksp$SYSPROF $JOB_EXE_OPT
			returncode=$?
			echo Rerun job using al_engine returns $returncode
		fi
	fi
fi
# In rare cases, adiff returns cannot open output file error even the output file does exist
sleep $LAUNCHER_DELAY

# Copy error log from Data Services log directory to work directory
if [ "$COPYERRORLOG" = "Y" ]
then
    if [ `echo $JOB_EXE_OPT | grep -c '\-z'` -eq 1 ]
    then
        errorlog=${JOB_EXE_OPT##*-z}
        if [ -n "$errorlog" ]
        then
            errorlog=`echo $errorlog | cut -d ' ' -f1`
            error_basename=`basename $errorlog`
			echo error_basename is $error_basename
            error_dirname=`dirname $errorlog`
			echo error_dirname is $error_dirname
            echo Copy error log from Data Services log directory to specified work directory
            echo Specified Error log file: $errorlog
            GVAR1=`AL_Encrypt.exe "'$error_basename'" | tr -d '\r'`
            GVAR2=`AL_Encrypt.exe "'$error_dirname'" | tr -d '\r'`
            export GVAR="\$file_name=$GVAR1;\$work_dir=$GVAR2"
            export JOBNAME=CopyErrorLogNew
            export JOB_EXE_OPT=""
            ${JYTHON_CMD} ${ROBOTHOME}/bin/subvalue2.py $QAENV/bin/launcher.txt ${DS_WORK}/tlauncher.txt
            AL_RWJobLauncher.exe "$DS_COMMON_DIR/log/$JOBSERVERNAME/" -w "inet:$JOBSERVERHOST:$JOBSERVERPORT" -t10000 -C "${DS_WORK}/tlauncher.txt"
            unset GVAR
        fi
    fi
fi

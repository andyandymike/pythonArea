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

AL_RWJobLauncher.exe "$LINK_DIR/log/$JOBSERVERNAME/" -w "inet:$JOBSERVERHOST:$JOBSERVERPORT"  -C "$runtest/work/tlauncher.txt"
rv=$?
if [ $rv -ne 0 ]
then
	echo AL_RWJobLauncher job $JOBNAME returns code $rv
fi
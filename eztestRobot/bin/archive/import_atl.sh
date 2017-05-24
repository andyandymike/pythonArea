if [ $IMPORT = "FALSE" ]
then
echo "No atl import " $1
else
export ATLFILE=$1
${JYTHON_CMD} ${ROBOTHOME}/bin/subvalue2.py $runtest/positive/$ATLFILE $DS_WORK/t$ATLFILE
sed -i "s/\r//g" $DS_WORK/t$ATLFILE
al_engine ${al_engine_param} -f$DS_WORK/t$ATLFILE -z$DS_WORK/t$ATLFILE.txt  -passphrasedsplatform
fi
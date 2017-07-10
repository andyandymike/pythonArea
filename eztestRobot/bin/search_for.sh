export DSWORK=$1
export INFILE=$2
export KEYWORD=$3
export EXPCNT=$4
export ACTCNT=0
#export curdir=`pwd`
#echo "cwd: $curdir"


cp $DSWORK/${INFILE} $DSWORK/${INFILE}1
sed -i 's/,/\n/g' $DSWORK/${INFILE}1 
ACTCNT=`grep -Ec "$KEYWORD" $DSWORK/${INFILE}1`
#grep "$KEYWORD1" $DSWORK/${INFILE}1
#echo "Searching for $KEYWORD"
#echo "expected count = $EXPCNT"
#echo "actual count   = $ACTCNT"
if [ $ACTCNT -eq $EXPCNT ]
then echo 1
else echo 0
fi
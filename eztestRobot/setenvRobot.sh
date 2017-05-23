export ROBOTFOLDERNAME=${ROBOTHOME##*/}
rm -r ${TESTNODE}/tmp
mkdir ${TESTNODE}/tmp
cp -r ${ROBOTHOME} ${TESTNODE}/tmp
chmod -R 777 ${TESTNODE}/tmp/$ROBOTFOLDERNAME
export ROBOTHOME=${TESTNODE}/tmp/$ROBOTFOLDERNAME

export QAENV="$ROBOTHOME"
export jythonjar='jython-standalone-2.7.0.jar'
export robotframeworkjar='robotframework-2.8.7.jar'
export JYTHON_CMD="java -jar ${ROBOTHOME}/bin/${jythonjar}"
export subvalue2=${ROBOTHOME}/bin/subvalue2.py
[ -z "$ROBOT_TEST_TIMEOUT" ] && export ROBOT_TEST_TIMEOUT='6000s'
[ -z "$DEBUG" ] && export DEBUG=0
export ROBOT_OPTION="-v ROBOTHOME:${ROBOTHOME} --noncritical InTestingSetup"
[ -n "$ROBOT_OPTION_EX" ] && export ROBOT_OPTION="$ROBOT_OPTION $ROBOT_OPTION_EX"


if [ "$TERM" = "cygwin" ]
then
    export PATH="`cygpath -u ${QAENV}/bin`:`cygpath -u "${LINK_DIR}/bin"`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


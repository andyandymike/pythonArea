export QAENV="$ROBOTHOME"
export ROBOT_TEST_TIMEOUT='10 minutes'
export jythonjar='jython-standalone-2.7.0.jar'
export robotframeworkjar='robotframework-2.8.7.jar'
export JYTHON_CMD="java -jar ${ROBOTHOME}/bin/${jythonjar}"
export subvalue2=${ROBOTHOME}/bin/subvalue2.py
export timeout='600s'
export ROBOT_OPTION="-v ROBOTHOME:${ROBOTHOME} -v ROBOT_TEST_TIMEOUT:${timeout} --noncritical InTestingSetup"


if [ "$TERM" = "cygwin" ]
then 
    export PATH="`cygpath -u "${LINK_DIR}/bin"`:`cygpath -u ${QAENV}/bin`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


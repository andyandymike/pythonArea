export ROBOTFOLDERNAME=${ROBOTHOME##*/}
rm -r ${TESTNODE}/tmp
mkdir ${TESTNODE}/tmp
cp -r ${ROBOTHOME} ${TESTNODE}/tmp
chmod -R 777 ${TESTNODE}/tmp/$ROBOTFOLDERNAME
export ROBOTHOME=${TESTNODE}/tmp/$ROBOTFOLDERNAME

export QAENV="$ROBOTHOME"
export jythonjar='jython-standalone-2.7.0.jar'
export robotframeworkjar='robotframework-3.0.2.jar'
export JYTHON_CMD="java -jar ${ROBOTHOME}/bin/${jythonjar}"
export subvalue2=${ROBOTHOME}/bin/subvalue2.py
export ROBOT_OPTION="-v ROBOTHOME:${ROBOTHOME} --noncritical InTestingSetup"



if [ "$TERM" = "cygwin" ]
then
    export PATH="`cygpath -u ${QAENV}/bin`:`cygpath -u "${LINK_DIR}/bin"`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


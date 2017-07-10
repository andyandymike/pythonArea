export ROBOTFOLDERNAME=${ROBOTHOME##*/}

if [ -e "${TESTNODE}/tmp/$ROBOTFOLDERNAME/version.txt" ]
then
  cmp --silent "${ROBOTHOME}/version.txt" "${TESTNODE}/tmp/$ROBOTFOLDERNAME/version.txt" || export NEED_UPDATE='TRUE'
fi

if [ $NEED_UPDATE='TRUE' ] || [ ! -e "${TESTNODE}/tmp/$ROBOTFOLDERNAME/version.txt" ] || [ -n "$FORCE_COPY_ROBOT" ]
then
  rm -r ${TESTNODE}/tmp/$ROBOTFOLDERNAME
  mkdir ${TESTNODE}/tmp
  echo Due to version update, will copy latest Robot, please wait ...
  cp -r ${ROBOTHOME} ${TESTNODE}/tmp
  chmod -R 777 ${TESTNODE}/tmp/$ROBOTFOLDERNAME
  export ROBOTHOME=${TESTNODE}/tmp/$ROBOTFOLDERNAME

  export QAENV="$ROBOTHOME"
  dos2unix ${QAENV}/bin/*.sh
fi

export QAENV="$ROBOTHOME"
export jythonjar='jython-standalone-2.7.0.jar'
export robotframeworkjar='robotframework-3.0.2.jar'
export sqlitejdbc=''
export JYTHON_CMD="java -jar ${ROBOTHOME}/bin/${jythonjar}"
export subvalue2=${ROBOTHOME}/bin/subvalue2.py
export ROBOT_OPTION="-v ROBOTHOME:${ROBOTHOME} --noncritical InTestingSetup"
export ROBOT_TIMEOUT_DEF='3600s'
export DS_BUILD=`al_engine -v`


if [ "$TERM" = "cygwin" ]
then
    export PATH="`cygpath -u ${QAENV}/bin`:`cygpath -u "${LINK_DIR}/bin"`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


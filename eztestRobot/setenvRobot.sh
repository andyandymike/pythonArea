if [ -z "$ROBOTHOME" ]
then
  echo "ERROR: You have not export ROBOTHOME"
  exit 1
fi

export ROBOTFOLDERNAME=${ROBOTHOME##*/}

[ -z "$ROBOT_LOCAL_TEMP_FOLDER" ] && export ROBOT_LOCAL_TEMP_FOLDER=tmp_robot

if [ -e "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt" ]
then
  cmp --silent "${ROBOTHOME}/version.txt" "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt"
  status=$?
  [ $status -eq 1 ] && export NEED_UPDATE='TRUE'
fi

if [ -z "$NOT_COPY_ROBOT" ] && [ -n "$NEED_UPDATE" ] || [ ! -e "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt" ] || [ -n "$FORCE_COPY_ROBOT" ]
then
  rm -r ${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER
  mkdir ${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER
  chmod -R 777 ${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER
  echo Due to version update, will copy latest Robot, please wait ...
  cp -r ${ROBOTHOME} ${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER
  chmod -R 777 ${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME
  export ROBOTHOME=${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME

  export ROBOT_COPYED='TRUE'

  export QAENV="$ROBOTHOME"
  dos2unix ${QAENV}/bin/*.sh
fi

if [ -z "$NEED_UPDATE" ] && [ -z "$NOT_COPY_ROBOT" ]
then
  export ROBOTHOME=${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME
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

unset DS_WORK
unset UDS_WORK
unset DS_GOLD
unset DS_INPUT
unset UDS_INPUT

unset ROBOT_LOCAL_TEMP_FOLDER

if [ "$TERM" = "cygwin" ]
then
    export PATH="`cygpath -u ${QAENV}/bin`:`cygpath -u "${LINK_DIR}/bin"`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


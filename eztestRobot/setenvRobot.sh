if [ -z "$ROBOTHOME" ]
then
  echo "ERROR: You have not export ROBOTHOME"
  exit 1
fi

sleep 2

export ROBOTFOLDERNAME=${ROBOTHOME##*/}

[ -z "$ROBOT_LOCAL_TEMP_FOLDER" ] && export ROBOT_LOCAL_TEMP_FOLDER=tmp_robot
[ -z "$ROBOT_LOCK_FOLDER" ] && export ROBOT_LOCK_FOLDER=tmp_robot_lock
export ROBOT_LOCK=${TESTNODE}/$ROBOT_LOCK_FOLDER/upgrade_robot.lock

if [ -z "$NOT_COPY_ROBOT" ]
then
  export LOOP_COUNT=1
  while [ -e ${ROBOT_LOCK} ] && [ $LOOP_COUNT -lt 100 ]
  do
    export OTHER_SESSION="TRUE"
    unset FORCE_COPY_ROBOT
    unset NEED_UPDATE
    if [ $LOOP_COUNT = 1 ]
    then
      echo "Other Session may upgrading robot, please wait"
      echo "if wait too long, check your environment and try"
      echo "delete ${ROBOT_LOCK}"
    fi
    let LOOP_COUNT=$LOOP_COUNT+1
    sleep 6
  done
  unset LOOP_COUNT
fi

if [ -z "$OTHER_SESSION" ] && [ -z "$NOT_COPY_ROBOT" ] && [ -e "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt" ]
then
  cmp --silent "${ROBOTHOME}/version.txt" "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt"
  status=$?
  [ $status -eq 1 ] && export NEED_UPDATE='TRUE'
fi

if [ -z "$OTHER_SESSION" ] && [ -z "$NOT_COPY_ROBOT" ] && [ -n "$NEED_UPDATE" ] || [ ! -e "${TESTNODE}/$ROBOT_LOCAL_TEMP_FOLDER/$ROBOTFOLDERNAME/version.txt" ] || [ -n "$FORCE_COPY_ROBOT" ]
then
  if [ ! -e ${ROBOT_LOCK} ]
    then
      mkdir  ${TESTNODE}/$ROBOT_LOCK_FOLDER
      touch ${ROBOT_LOCK}
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
      rm ${TESTNODE}/$ROBOT_LOCK_FOLDER/upgrade_robot.lock

    else
      export LOOP_COUNT=1
      while [ -e ${ROBOT_LOCK} ] && [ $LOOP_COUNT -lt 100 ]
      do
        export OTHER_SESSION="TRUE"
        unset FORCE_COPY_ROBOT
        unset NEED_UPDATE
        if [ $LOOP_COUNT = 1 ]
        then
          echo "Other Session may upgrading robot, please wait"
          echo "if wait too long, check your environment and try"
          echo "delete ${ROBOT_LOCK}"
        fi
        let LOOP_COUNT=$LOOP_COUNT+1
        sleep 6
      done
      unset LOOP_COUNT
  fi
fi

if [ -z "$NEED_UPDATE" ] && [ -z "$NOT_COPY_ROBOT" ] || [ -n "$OTHER_SESSION" ]
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
unset ROBOT_LOCK_FOLDER
unset ROBOT_LOCK
unset OTHER_SESSION

if [ "$TERM" = "cygwin" ]
then
    export PATH="`cygpath -u ${QAENV}/bin`:`cygpath -u "${LINK_DIR}/bin"`:${PATH}"
else
    export PATH="${LINK_DIR}/bin:${QAENV}/bin:${PATH}"
fi


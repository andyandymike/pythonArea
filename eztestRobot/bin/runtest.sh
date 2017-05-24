flag=0
findsuite=0
findcase=0
testsuit=""
TESTCASE=""

function print_readme
{
    if [ ! -e $TESTNODE/$1/readme ]
    then
	print "$TESTNODE/$1/readme doesn't exit"
	return 0
    else
      print "Opening readme file for $1: $TESTNODE/$1/readme..."
	print ""
	print ""
      cat $TESTNODE/$1/readme
    fi
	
}

function print_help
{
      echo "runtest.sh testsuite testunits "
      echo " [-p paramfile] "
      echo " [-rst result foldler] "
      echo " [-t testcase] "
      echo " [-config configuration file] "
      echo " [-lang metadata language] "
      echo " [-db database type] "
      echo " [-timeout testunit level time out value] "
      echo " [-debug] "
      echo " [-robot robot options] "
      echo " [-noconvert]"
      echo " [-nosetup] "
      echo " [-n TESTNODE] "
      echo "                               "
      echo "paramfile     -- pathname for the parameters file"
      echo "result folder -- result folder name in $TESTNODE/result."  
      echo "                 Default is $TESTNODE/result" 
      echo "testcase      -- Testcase name in the testunit to be executed"
      echo "                 separate cases by \",\" eg. testcase1,testcase2"
      echo "                 support wild card eg. testcase01*"
      echo "testunits     -- testunits name in the testsuite to be executed"
      echo "                 separate cases by \",\" eg. unit1,unit2"
      echo "database type -- specify the database type such as SQL 2000"
      echo "nosetup       -- skip setup in the testunit, cannot work together with -noconvert"
      echo "noconvert     -- skip convert testcase/setup to testcase.robot"
      echo "timeout       -- set timeout value for testcase, this is testunit level"
}

######################################
##  MAIN program
######################################

export G_UPDATE='on'
export TESTCASE=
export TESTSUITE_SETUP='!call setup'
export CONFIG=$QAENV/ws.env

flag=0

while [ $# -gt 0 ]
do
  case $1 in
    -nosetup)
      shift
      export TESTSUITE_SETUP=
      export NOSETUP='on'
      ;;
    -debug)
      shift
      export DEBUG='on'
      ;;
    -noconvert)
      shift
      export NOCONVERT='on'
      ;;
    -timeout)
      shift
      export ROBOT_TEST_TIMEOUT=$1
      ;;
    -robot)
      shift
      export ROBOT_OPTION_EX=$1
      ;;
    -t)
      shift
      TESTCASE=$1
      export TESTCASE
      shift
      ;;
    -noupdate)
      shift
      G_UPDATE='off'
      ;;
    -p)
      shift
      PARAMFILE=$1
      export PARAMFILE
      shift
      ;;
    -h)
      shift
      print_help
      exit 0
      ;;
    -os)
      shift
      G_OSPLATFORM=$1
      export G_OSPLATFORM
      shift
      ;;
    -db)
      shift
      G_DBVERSION=$1
      export G_DBVERSION
      shift
      ;;
    -n)
      shift
      export TESTNODE=$1
      shift
      ;;
    -lang)
	  shift
	  export LANGFILE=$1
      shift
      ;;
    -rst)
	  shift
	  export test_result_dir=$1
      shift
	  ;;
    -config)
	  shift
	  export CONFIG=$1
      shift
      ;;
    -readme)
      shift
      if [ $# -gt 0 ]
      then
          print_readme $1
      else
        print "Opening general readme file : $TESTNODE/readme..."
        print ""
        print ""
	  cat $TESTNODE/readme
      fi
      exit 0
      ;;
     *)
   if [ $flag -eq 0 ]
      then
        export testsuite=$1
        flag=1
      elif [ $flag -eq 1 ]
      then
        testunit=$1
        flag=2
      elif [ $flag -eq 2 ]
      then
        export TESTCASE 
        flag=3
      fi
      shift
      ;;
  esac
done

if [ $flag  -lt 2 ]
then
  if [ $flag -eq 0 ]
  then
    echo "Error: Both test suite name and testunit name are missing."
    print_help
  else
    echo "Error: Test suite name or testunit name is missing."
    print_help
  fi
  exit 1
fi

####################################################
## Verying result directory exists
####################################################

echo "Specified result directory is ${test_result_dir}"
if [ -z $test_result_dir ]
then
  export test_result_dir=$TESTNODE/result
else
  vartem=${test_result_dir#*:}
  vartem=`echo $vartem | cut -c 1`
  if [ $vartem != '/' ]
  then
    export test_result_dir=${TESTNODE}/result/${test_result_dir}
  fi
fi
echo "The result directory is ${test_result_dir}"

mkdir -p $test_result_dir/$testsuite
if [ $? -ne 0 ]
then
  echo "Error: cannot create directory $test_result_dir/$testsuite"
  exit 3
fi

####################################################
## Run the test
####################################################

if [ -z $TESTNODE ]
then
  echo "The default TESTNODE is your current root"
fi

export G_BUILDVERSION="`al_engine -v | cut -d ' ' -f 4`" 
if [ $G_BUILDVERSION = 'Engine' ]
then 
  export G_BUILDVERSION="`al_engine -v | cut -d ' ' -f 6`"
fi
 
 . $PARAMFILE
 
if [ test = test$LANGFILE ]
then
  echo 'LANGFILE is not specified'
else 
  if [ -e $LANGFILE ]
  then
    . $LANGFILE
    export all
  fi
fi

IFS=',' read -ra TEMP <<< "$testunit"
for i in "${TEMP[@]}"; do
  Testlist="$Testlist $i"
done

for testunits in $Testlist
do
    export runtest=$TESTNODE/$testsuite/$testunits
	export unix_runtest=$UTESTNODE/$testsuite/$testunits
    export utestunit=$UTESTNODE/$testsuite/$testunits
    export testunit=$TESTNODE/$testsuite/$testunits
	
	[ -z "$DS_WORK_ROOT" ] && export DS_WORK_ROOT=$TESTNODE
	[ -z "$UDS_WORK_ROOT" ] && export UDS_WORK_ROOT=$UTESTNODE
	[ -z "$DS_WORK" ] && export DS_WORK=$DS_WORK_ROOT/$testsuite/$testunits/work
    [ -z "$UDS_WORK" ] && export UDS_WORK=$UDS_WORK_ROOT/$testsuite/$testunits/work
    [ -z "$DS_GOLD" ] && export DS_GOLD=$DS_WORK_ROOT/$testsuite/$testunits/gold
    [ -z "$DS_INPUT" ] && export DS_INPUT=$DS_WORK_ROOT/$testsuite/$testunits/input
    [ -z "$UDS_INPUT" ] && export UDS_INPUT=$UDS_WORK_ROOT/$testsuite/$testunits/input

    mkdir -p $DS_WORK
    mkdir -p $DS_GOLD
    mkdir -p $DS_INPUT

    chmod -R 777 $DS_WORK
    chmod -R 777 $DS_GOLD
    chmod -R 777 $DS_INPUT

    rm ${DS_WORK}/*
    rm ${DS_GOLD}/*
    rm ${DS_INPUT}/*
    cp ${runtest}/goldlog/* ${DS_GOLD}
    cp ${runtest}/input/* ${DS_INPUT}

    rm ${test_result_dir}/${testunits}_output.xml
    rm ${test_result_dir}/${testunits}_log.html
    rm ${test_result_dir}/${testunits}_report.html
    rm ${test_result_dir}/${testunits}.sum


    echo "Testsuite=$runtest"
    if [ ! -e $runtest ]
    then
       echo "Error: Testunit $runtest doesn't exist."
    fi

    [ -z "$ROBOT_TEST_TIMEOUT" ] && export ROBOT_TEST_TIMEOUT='6000s'
    [ -n "$ROBOT_OPTION_EX" ] && export ROBOT_OPTION="$ROBOT_OPTION $ROBOT_OPTION_EX"

    if [ -n $TESTCASE ]
    then
      IFS=',' read -ra TEMP <<< "$TESTCASE"
      for i in "${TEMP[@]}"; do
        TESTCASES="$TESTCASES -t $i"
      done
    fi

    [ -z "$NOCONVERT" ] && java -jar ${ROBOTHOME}/bin/${jythonjar} bin/Converter.py $runtest
	java -jar ${ROBOTHOME}/bin/${robotframeworkjar} ${ROBOT_OPTION} ${TESTCASES} -v ROBOT_TEST_TIMEOUT:${ROBOT_TEST_TIMEOUT} -d ${test_result_dir} -o ${testunits}_output.xml -l ${testunits}_log.html -r ${testunits}_report.html $runtest/testcase.robot
	java -jar ${ROBOTHOME}/bin/${jythonjar} bin/summary.py ${test_result_dir}/${testunits}_output.xml

	echo ---------------------------------------------------------------------------------
    echo ${testunits} summary:
    cat ${test_result_dir}/${testunits}.sum
    echo

    if [ $G_UPDATE = 'on' ] ;
    then
      ezupdate.sh $CONFIG ${test_result_dir}/${testunits}.sum $testunits
    fi
done

unset ROBOT_TEST_TIMEOUT
unset ROBOT_OPTION_EX
unset DEBUG
unset NOSETUP
unset TESTCASE



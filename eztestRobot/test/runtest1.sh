flag=0
manual_flag=0
findsuite=0
findcase=0
testsuite=""
TESTCASE=""

function run_the_test
{
       #cd $TESTNODE

       if [ $XML_JOB = 'on' ] ;
       then 
           echo 'XML job testcases will be executed ....'

      ##     java -classpath N:/ezTestTool/env/bin GenXMLTestCase $TESTNODE $testsuite $cases

      ##     eztest.exe < $QAENV/bin/eztest_setup_xml
       else

           echo 'ATL job testcases will be executed ....'
           if [ "$COPYERRORLOG" = "Y" ]; then
             al_engine $al_engine_param -f$QAENV/bin/CopyErrorLog.atl
           fi
           $QAENV/bin/eztest.exe < $QAENV/bin/eztest_setup
       fi
       if [ $G_UPDATE = 'on' ] ;
          then
          echo $testsuite
		  echo $testunitname
          echo $CONFIG
          echo $test_result_dir
		  echo $testunit_4_log
          if [ $XML_JOB = 'on' ] ;
            then
				echo
			if [ $testunit_4_log_exists -eq 1 ] ;
				then
					echo 'testunit_4_log_exists = 1'
					if [ -e ${test_result_dir}/${testsuite}/${testunitname}_xml.sum ]
					then
						ezupdate.sh $CONFIG ${test_result_dir}/${testsuite}/${testunitname}_xml.sum $testunit_4_log
					else
						ezupdate.sh $CONFIG ${test_result_dir}/${testunitname}_xml.sum $testunit_4_log
					fi
				else
					echo 'testunit_4_log_exists = 0'
					if [ -e ${test_result_dir}/${testsuite}/${testunitname}_xml.sum ]
					then
						ezupdate.sh $CONFIG ${test_result_dir}/${testsuite}/${testunitname}_xml.sum $testunitname
					else
						ezupdate.sh $CONFIG ${test_result_dir}/${testunitname}_xml.sum $testunitname
					fi
			fi
		  else
		  
			echo
			if [ $testunit_4_log_exists -eq 1 ] ;
				then
					echo 'testunit_4_log_exists = 1'
					if [ -e ${test_result_dir}/${testsuite}/${testunitname}.sum ]
					then
						echo "ezupdate.sh $CONFIG ${test_result_dir}/${testsuite}/${testunitname}.sum $testunit_4_log "
						ezupdate.sh $CONFIG ${test_result_dir}/${testsuite}/${testunitname}.sum $testunit_4_log
					else
						ezupdate.sh $CONFIG ${test_result_dir}/${testunitname}.sum $testunit_4_log
					fi
				else
					echo 'testunit_4_log_exists = 0'
					if [ -e ${test_result_dir}/${testsuite}/${testunitname}.sum ]
					then
						ezupdate.sh $CONFIG ${test_result_dir}/${testsuite}/${testunitname}.sum $testunitname
					else
						ezupdate.sh $CONFIG ${test_result_dir}/${testunitname}.sum $testunitname
					fi				
			fi
          fi
       fi
}

function read_alltest
{
   if [ $# -eq 0 ] 
   then
	 return 0  
   fi

   temp1=${1%=*}
   if [ ${#temp1} -eq 0 ]
   then
         return 0
   fi

   if [ $1 = "Test:" ] 
   then
	shift 
	if [ $1 = $testsuite ]
        then
	    findsuite=1
	else
	    findcase=0
	    findsuite=0
        fi
   fi

   if  [ $findsuite -eq 1 ] 
   then
	if [ $1 = "Testcase:"  ]
	then
	    if [ $findcase -eq 0 ]
            then
	        findcase=1
	        shift
	        Testlist="$Testlist $*"
            fi
	elif [ $findcase -eq 1 ]
	then
	    Testlist="$Testlist $*"
	fi
   fi
}

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
      echo "runtest.sh testgroup testsuite "
      echo " [-p paramfile] "
      echo " [-rst result foldler] "
      echo " [-t testcase] "
      echo " [-db database type] "
      echo " [-config configuration file] "
      echo " [-lang metadata language] "
      echo "                               "
      echo "paramfile     -- pathname for the parameters file"
      echo "result folder -- result folder name in $TESTNODE/result."  
      echo "                 Default is $TESTNODE/result" 
      echo "testcase      -- Testcase name in the testsuite to be executed"
      echo "database type -- specify the database type such as SQL 2000"
}


######################################
##  MAIN program
######################################

export G_UPDATE='on'
export XML_JOB='off'
export TESTCASE=
export TESTSUITE_SETUP='!call setup'
export CONFIG=$QAENV/ws.env
export testunit_4_log_exists=0
flag=0

while [ $# -gt 0 ]
do
  case $1 in
 -nosetup)
    shift
    export TESTSUITE_SETUP=
 ;;
 -t)
    shift
     TESTCASE=$1
    export TESTCASE
      shift
     ;;
 -xmljob)
      shift
      XML_JOB='on'
     ;;
 -noupdate)
      shift
      G_UPDATE='off'
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
    -m)
      shift
      manual_flag=1
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
	-testunit_4_log)
	shift
	export testunit_4_log=$1
	export testunit_4_log_exists=1
        shift
        ;;
     -release)
       shift
       export RELEASE=$1
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

if [[ "$G_BUILDVERSION" > "14.2" ]]
then
  if [ "$COPYERRORLOG" != "N" ]
  then
    export COPYERRORLOG="Y"
  fi
fi

if [ -f $PARAMFILE ]
 then
   . $PARAMFILE
 else
   echo Cannot source parameter file $PARAMFILE
   exit
fi
 # . $TESTNODE/testlib/$LANGFILE

if [ -n "$PARAM_EXTRA" -a -f "$PARAM_EXTRA" ]
 then
   . $PARAM_EXTRA
fi


if [ $testunit = "all" ]
then
    exec 5<$TESTNODE/testlist
    while read -u5 LINE
    do
        read_alltest $LINE
    done

else
    Testlist=$testunit
fi

for cases in $Testlist
do
    export runtest=$TESTNODE/$testsuite/$cases
    export utestunit=$UTESTNODE/$testsuite/$cases
    export testunit=$TESTNODE/$testsuite/$cases
	export testunitname=$cases
    echo "Testsuite=$runtest"
    if [ ! -e $runtest ]
    then
       echo "Error: Testunit $runtest doesn't exist."
       #exit 2
    fi
    run_the_test
done




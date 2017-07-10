# init classpath
export EZPATH="${QAENV}/lib/ezupdate.jar;${QAENV}/lib/wsdl4j-1.5.1.jar;${QAENV}/lib/saaj.jar;${QAENV}/lib/commons-discovery-0.2.jar;${QAENV}/lib/commons-logging-1.0.4.jar;${QAENV}/lib/jaxrpc.jar;${QAENV}/lib/axis.jar"

# JVM parameters, modify as appropriate
export JAVA_OPTS="$JAVA_OPTS -Xms128m -Xmx256m"

# ********* run ezupdate ***********
java -cp $EZPATH com.bobj.eztest.report.TestStatusUpdate $1 $2 $3

if [ $# -eq 1 ]
then
    rm -f temfile
    mv $1 temfile
    tr -d '\012\015' < temfile | sed 's/  */ /g' > $1
    rm -f temfile
else
    tr -d '\012\015' < $1 | sed 's/  */ /g' > $2
fi

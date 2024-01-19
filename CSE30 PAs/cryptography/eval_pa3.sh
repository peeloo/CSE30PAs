#! /bin/bash
# eval_pa3 - grades PA3 performance and specification
#

EXITCODE=0
MAIN=py
REPORT=grade.txt
GRADE=0
COUNTER=0
SOURCES="codec.py steganography.py"
SOURCE1=codec.py
SOURCE2=steganography.py
TEST1=test_codec.py
TEST2=test_steganography.py
COMMENTS="author"
TMP=tmp

echo "
Programming Assignment 3
**********************************
Specification and Performance :" >> $REPORT

#
# checks files by filenames
#
for f in $SOURCES
do 
    if [ -e $f -a -s $f ]
    then
        echo "$f is present +1/1" >> $REPORT
        ((GRADE = GRADE + 1))
        for c in $COMMENTS
        do
            grep -i "# *$c" $f > comments
            if [ -e comments -a $(wc -l < comments) -eq 0 ]
            then
                echo "$f does not have a comment $c +0/1" >> $REPORT
            else
                echo "$f has a comment $c +1/1" >> $REPORT
                ((GRADE = GRADE + 1))
            fi
        done
    else
        echo "$f is named incorrectly or absent +0/1" >> $REPORT 
    fi
done

#
# checks codec.py
#   

echo "0" > $TMP
if [ -e $SOURCE1 ]
then
    $MAIN $TEST1 >> $REPORT 2>> $REPORT &
    PID=$!
    sleep 2
    kill -KILL $PID 2> /dev/null
    echo >> $REPORT
    ((GRADE = GRADE + $(cat $TMP)))
else
    echo "$SOURCE1 not implemented +0 points" >> $REPORT
fi

#
# checks steganography.py
#

echo "0" > $TMP
if [ -e $SOURCE2 ]
then
    $MAIN $TEST2 >> $REPORT 2>> $REPORT &
    PID=$!
    sleep 2
    kill -KILL $PID 2> /dev/null
    echo >> $REPORT
    ((GRADE = GRADE + $(cat $TMP)))
else
    echo "$SOURCE2 not implemented +0 points" >> $REPORT
fi

#
# prints grade
#
                echo "
**********************************
Your grade is $GRADE out of 40 

        
" >> $REPORT

#cat $REPORT
rm comments
echo $GRADE > tmp
    
exit $EXITCODE

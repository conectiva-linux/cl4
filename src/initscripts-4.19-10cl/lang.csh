set temp=`mktemp /tmp/tcsh.lang.XXXXXX`
foreach line ( `cat /etc/sysconfig/i18n` )
        echo "setenv $line" | sed "s/=/ /" >> $temp
end
source $temp
rm -f $temp

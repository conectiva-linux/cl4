#!/bin/sh

test -f /etc/mail/relay_allow && while read linha
do
  echo "$linha	RELAY" >> /etc/mail/access
done < /etc/mail/relay_allow 

test -f /etc/mail/ip_allow && while read linha
do
  echo "$linha    OK" >> /etc/mail/access
done < /etc/mail/ip_allow

test -f /etc/mail/name_allow && while read linha
do
  echo "$linha    OK" >> /etc/mail/access
done < /etc/mail/name_allow

test -f /etc/mail/deny && while read linha
do
  echo "$linha    DENY" >> /etc/mail/access
done < /etc/mail/deny


#!/bin/sh
# Red Hat Software,
# Conectiva Informática
# Marcelo Wormsbecker Tosatti <marcelo@conectiva.com.br>,
# Arnaldo Carvalho de Melo <acme@conectiva.com.br>
# Wanderlei Antonio Cavassin <cavassin@conectiva.com.br>
# Modificações:
# Sun Nov 22 20:07:50 EDT 1998 - acme - xrdb -nocpp
# Sat Dec 12 22:47:41 EDT 1998 - acme & cavassin - simplifications
# Thu Apr 22 15:44:35 EST 1999 - cavassin - removed LD_PRELOAD

trap "unload_resources" 2 15

XPROP=/usr/lib/netscape/i18n/Netscape.ad.$LANG
HOSTC=

unload_resources() {
    if [ -n "$NEED_UNLOAD" ] ; then
	xrdb -nocpp -remove -screen $HOSTC $XPROP 2> /dev/null
    fi
}

which=""

ANTERIOR=

for PARAM in $* ; do
	if [ "$ANTERIOR" = "-display" ] ; then
		HOSTC="-display $PARAM"
		break
	fi
	ANTERIOR=$PARAM
done

if echo $0 | grep 'navigator' >/dev/null; then
    which=netscape-navigator
elif echo $0 | grep 'communicator' >/dev/null ; then
    which=netscape-communicator
fi

if [ -z $which ]; then
    if rpm -q netscape-communicator >/dev/null 2>&1; then
	which=netscape-communicator
    elif rpm -q netscape-navigator >/dev/null 2>&1; then
	which=netscape-navigator
    else
	echo "You don't have netscape installed." >&2
    fi
fi
	
if ! rpm -q $which >/dev/null 2>&1; then
    echo "You don't have $which installed." >&2
    exit 1
fi

I="`LANG= rpm -q $which --qf '%{INSTALLPREFIX}\n'`"
if [ "$I" = "(none)" ]; then
    I=/usr
fi

if [ -x $I/lib/netscape/$which ]; then

    if [ ! -z "$LANG" -a -f "$XPROP" ] ; then
	NEED_UNLOAD=1
	xrdb -nocpp -screen $HOSTC $XPROP 2> /dev/null
    fi

    if [ -z "$*" ]; then
	HOMEPAGE=/usr/doc/HTML/index.html
	if [ -f $HOME/.netscape/preferences.js ]; then
	    if grep "browser.startup.homepage" \
			$HOME/.netscape/preferences.js > /dev/null; then
		HOMEPAGE=""
	    fi
	fi
	$I/lib/netscape/$which $HOMEPAGE
    else
	$I/lib/netscape/$which $*
    fi
    
    unload_resources
    exit 0
fi

echo "An error occurred running and $I/lib/netscape/$which."

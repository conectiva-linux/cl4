#!/bin/sh
# starts licq with a xterm. So it can be called from wm menus for
# the 1st time
# Conectiva - Sat Mar 27 19:18:27 EST 1999

if [ -f ~/.licq/conf/owner.uin ] ; then
	exec /usr/bin/licq &
else
	exec xterm -T "licq initial configuration" -e /usr/bin/licq
fi

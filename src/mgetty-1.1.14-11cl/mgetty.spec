Summary: A getty replacement for use with data and fax modems.
Summary(pt_BR): Um substituto melhor do que o getty para modems de dados e fax
Summary(es): Un substituto mejor que el getty para módems de datos y fax
Name: mgetty
Version: 1.1.14
Release: 11cl
Source: ftp://ftp.leo.org/pub/comp/os/unix/networking/mgetty/mgetty1.1.14-Apr02.tar.gz
Source700: mgetty-man-pt_BR.tar
Patch0: mgetty-1.1.14-config.patch
Patch1: mgetty-1.1.5-makekvg.patch
Patch2: mgetty-1.1.14-policy.patch
Patch3: mgetty-1.1.5-strip.patch
Patch4: mgetty-1.1.14-echo.patch
Patch5: mgetty-1.1.14-logrotate.patch
Patch6: mgetty-1.1.9-imakefile.patch
Patch7: mgetty-1.1.14-docfix.patch
Requires: libgr-progs
Copyright: distributable
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Buildroot: /var/tmp/mgetty+sendfax-root
Prereq: info

%package sendfax
Summary: Provides support for sending faxes over a modem.
Summary(pt_BR): Suporte ao envio e recepção de faxes via faxmodem
Summary(es): Soporte a envío y recepción de faxes vía faxmódem
Requires: mgetty = %{PACKAGE_VERSION}
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones

%package voice
Summary: A program for using your modem and mgetty as an answering machine.
Summary(pt_BR): Suporte para modems com capacidade de mail por voz
Summary(es): Soporte para módems con capacidad de mail por voz
Requires: mgetty = %{PACKAGE_VERSION}
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones

%package viewfax
Summary: An X Window System fax viewer.
Summary(pt_BR): Visualizador de faxes para X11
Summary(es): Visualizador de faxes para X11
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones

%description
The mgetty package contains a "smart" getty which allows logins over a
serial line (i.e., through a modem).  If you're using a Class 2 or 2.0
modem, mgetty can receive faxes.  If you also need to send faxes, you'll
need to install the sendfax program.

If you'll be dialing in to your system using a modem, you should install
the mgetty package.  If you'd like to send faxes using mgetty and your
modem, you'll need to install the mgetty-sendfax program.  If you need a
viewer for faxes, you'll also need to install the mgetty-viewfax package.

%description -l pt_BR
Este pacote contém o programa inteligente 'getty' que permite logins
através de uma linha serial (usadas com um modem por exemplo). O
programa permite o uso automático de callback e inclui suporte a FAX
(o pacote mgetty-sendfax precisa ser instalado para fazer uso total
de seu suporte a FAX).

%description -l es
Este paquete contiene el programa inteligente 'getty' que permite
logins a través de una línea serial (usadas con un módem por
ejemplo). El programa permite el uso automático de callback y
incluye soporte a FAX (el paquete mgetty-sendfax necesita ser
instalado para hacer uso total del soporte a FAX).

%description sendfax
Sendfax is a standalone backend program for sending fax files.  The
mgetty program (a getty replacement for handling logins over a serial
line) plus sendfax will allow you to send faxes through a Class 2 modem.

If you'd like to send faxes over a Class 2 modem, you'll need to install
the mgetty-sendfax and the mgetty packages.

%description -l pt_BR sendfax
Este pacote inclui suporte para o envio e recepção de faxes em
fax-modems classe 2. Também inclui suporte simples a enfileiramento
de faxes.

%description -l es sendfax
Este paquete incluye soporte al envío y recepción de faxes en
fax-módems clase 2. También incluye soporte sencillo a encadenamiento
de faxes.

%description voice
The mgetty-voice package contains the vgetty system, which enables
mgetty and your modem to support voice capabilities.  In simple terms,
vgetty lets your modem act as an answering machine.  How well the system
will work depends upon your modem, which may or may not be able to handle
this kind of implementation.

Install mgetty-voice along with mgetty if you'd like to try having your
modem act as an answering machine.

%description -l pt_BR voice
Este pacote inclui suporte a alguns modems que têm extensões de
voice mail.

%description -l es voice
Este paquete incluye soporte a algunos módems que tiene extensiones
de voice mail.

%description viewfax
Viewfax displays the fax files received using mgetty in an X11 window.
Viewfax is capable of zooming in and out on the displayed fax.

If you're installing the mgetty-viewfax package, you'll also need to
install mgetty.

%description -l pt_BR viewfax
Este pacote fornece um visualizador de faxes para X11 com
capacidade de zoom.

%description -l es viewfax
Este paquete ofrece un visor de faxes para X11 con capacidad de zoom.

%prep
%setup -q
cp policy.h-dist policy.h
%patch0 -p1 -b .config
%patch1 -p1 -b .makekvg
%patch2 -p1
%patch3 -p1 -b .strip
%patch4 -p1 -b .echo
%patch5 -p1
%patch6 -p1
# new texinfo much stricter about xrefs
%patch7 -p1 -b .docfix

%build
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"
cd voice
make "RPM_OPT_FLAGS=$RPM_OPT_FLAGS"

cd ../frontends/X11/viewfax-2.4
xmkmf
make depend
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/spool -p $RPM_BUILD_ROOT/sbin
make prefix=$RPM_BUILD_ROOT/usr spool=$RPM_BUILD_ROOT/var/spool \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax install
install -m700 callback/callback $RPM_BUILD_ROOT/usr/sbin
install -m4711 callback/ct $RPM_BUILD_ROOT/usr/bin
strip $RPM_BUILD_ROOT/usr/bin/newslock

gzip -9n $RPM_BUILD_ROOT/usr/info/*

mv $RPM_BUILD_ROOT/usr/sbin/mgetty $RPM_BUILD_ROOT/sbin

# this conflicts with efax
mv $RPM_BUILD_ROOT/usr/man/man1/fax.1 $RPM_BUILD_ROOT/usr/man/man1/mgetty_fax.1

# voice mail extensions
(cd voice
mkdir -p $RPM_BUILD_ROOT/var/spool/voice 
mkdir -p $RPM_BUILD_ROOT/var/spool/voice/messages
mkdir -p $RPM_BUILD_ROOT/var/spool/voice/incoming

make prefix=$RPM_BUILD_ROOT/usr spool=$RPM_BUILD_ROOT/var/spool \
	CONFDIR=$RPM_BUILD_ROOT/etc/mgetty+sendfax install

mv $RPM_BUILD_ROOT/usr/sbin/vgetty $RPM_BUILD_ROOT/sbin
install -m 600 -c voice.conf-dist $RPM_BUILD_ROOT/etc/mgetty+sendfax/voice.conf
)
# don't ship documentation that is executable...
find samples -type f -exec chmod 644 {} \;

(cd frontends/X11/viewfax-2.4
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man
)

mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
install -m 0644 logrotate.mgetty $RPM_BUILD_ROOT/etc/logrotate.d/mgetty
install -m 0644 logrotate.sendfax $RPM_BUILD_ROOT/etc/logrotate.d/sendfax

# Make sure everything is stripped
strip $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT/usr/sbin/* || :



mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mgetty-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/mgetty.info.gz /usr/info/dir --entry="* mgetty: (mgetty).		Package to handle faxes, voicemail and more."

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete /usr/info/mgetty.info.gz /usr/info/dir --entry="* mgetty: (mgetty). 	Package to handle faxes, voicemail and more."
fi

%postun
if [ $1 = 0 ]; then
  rm -fr /var/log/mgetty.log*
fi

%postun sendfax
if [ $1 = 0 ]; then
  rm -fr /var/log/sendfax.log*
fi

%files
%defattr(-,root,root)
%doc FAQ BUGS ChangeLog README.1st THANKS doc/modems.db samples 
%doc doc/mgetty.ps doc/*.txt
/sbin/mgetty
/usr/man/man8/mgetty.8
/usr/man/man8/callback.8
/usr/man/man8/faxrunqd.8
/usr/man/man4/mgettydefs.4
/usr/info/mgetty.info-2.gz
/usr/info/mgetty.info-3.gz
/usr/info/mgetty.info-4.gz
/usr/info/mgetty.info.gz
/usr/info/mgetty.info-1.gz
%dir /etc/mgetty+sendfax
%config /etc/mgetty+sendfax/login.config
%config /etc/mgetty+sendfax/mgetty.config
%config /etc/mgetty+sendfax/dialin.config
%config /etc/logrotate.d/mgetty
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files sendfax
%defattr(-,root,root)
%dir /var/spool/fax
%dir /var/spool/fax/incoming
%dir /var/spool/fax/outgoing
%dir /var/spool/fax/outgoing/locks

/usr/bin/kvg
/usr/bin/newslock
/usr/bin/g3cat
/usr/bin/g32pbm
/usr/bin/pbm2g3
/usr/bin/faxspool
/usr/bin/faxrunq
/usr/bin/faxq
/usr/bin/faxrm
%attr(0755,root,root) /usr/bin/ct
/usr/sbin/sendfax
/usr/sbin/faxrunqd
/usr/sbin/callback
%dir	/usr/lib/mgetty+sendfax
/usr/lib/mgetty+sendfax/cour25.pbm
/usr/lib/mgetty+sendfax/cour25n.pbm
/usr/man/man1/g32pbm.1
/usr/man/man1/pbm2g3.1
/usr/man/man1/g3cat.1
/usr/man/man1/mgetty_fax.1
/usr/man/man1/faxspool.1
/usr/man/man1/faxrunq.1
/usr/man/man1/faxq.1
/usr/man/man1/faxrm.1
/usr/man/man1/coverpg.1
/usr/man/man5/faxqueue.5
/usr/man/man8/sendfax.8
%config /etc/mgetty+sendfax/sendfax.config
%config /etc/mgetty+sendfax/faxrunq.config
%config /etc/mgetty+sendfax/faxheader
%config /etc/logrotate.d/sendfax

%files voice
%defattr(-,root,root)
%dir /var/spool/voice
%dir /var/spool/voice/incoming
%dir /var/spool/voice/messages

/sbin/vgetty
/usr/bin/vm
/usr/bin/pvfamp
/usr/bin/pvfcut
/usr/bin/pvfecho
/usr/bin/pvffile
/usr/bin/pvffft
/usr/bin/pvfmix
/usr/bin/pvfreverse
/usr/bin/pvfsine
/usr/bin/pvfspeed
/usr/bin/pvftormd
/usr/bin/rmdtopvf
/usr/bin/rmdfile
/usr/bin/pvftovoc
/usr/bin/voctopvf
/usr/bin/pvftolin
/usr/bin/lintopvf
/usr/bin/pvftobasic
/usr/bin/basictopvf
/usr/bin/pvftoau
/usr/bin/autopvf
/usr/bin/pvftowav
/usr/bin/wavtopvf

/usr/man/man1/zplay.1
/usr/man/man1/pvf.1
/usr/man/man1/pvfamp.1
/usr/man/man1/pvfcut.1
/usr/man/man1/pvfecho.1
/usr/man/man1/pvffile.1
/usr/man/man1/pvffft.1
/usr/man/man1/pvfmix.1
/usr/man/man1/pvfreverse.1
/usr/man/man1/pvfsine.1
/usr/man/man1/pvfspeed.1
/usr/man/man1/pvftormd.1
/usr/man/man1/rmdtopvf.1
/usr/man/man1/rmdfile.1
/usr/man/man1/pvftovoc.1
/usr/man/man1/voctopvf.1
/usr/man/man1/pvftolin.1
/usr/man/man1/lintopvf.1
/usr/man/man1/pvftobasic.1
/usr/man/man1/basictopvf.1
/usr/man/man1/pvftoau.1
/usr/man/man1/autopvf.1
/usr/man/man1/pvftowav.1
/usr/man/man1/wavtopvf.1
%config /etc/mgetty+sendfax/voice.conf

%files viewfax
%defattr(-,root,root)
%doc frontends/X11/viewfax-2.4/C* frontends/X11/viewfax-2.4/README
/usr/bin/viewfax
%dir /usr/lib/mgetty+sendfax
/usr/lib/mgetty+sendfax/viewfax.tif
/usr/man/man1/viewfax.1x

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr  6 1999 Bill Nottingham <notting@redhat.com>
- strip setuid bit from ct

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- better log handling

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Sat Aug 22 1998 Jos Vos <jos@xos.nl>
- Use a patch for creating policy.h using policy.h-dist.
- Add viewfax subpackage (X11 fax viewing program).
- Add logrotate config files for mgetty and sendfax log files.
- Properly define ECHO in Makefile for use with bash.
- Add optional use of dialin.config (for modems supporting this).
- Change default notification address to "root" (was "faxadmin").
- Change log file names according to better defaults.
- Change default notify program to /etc/mgetty+sendfax/new_fax (was
  /usr/local/bin/new_fax).

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- add faxrunqd man page (problem #850)
- add missing pbm2g3 (and man page); remove unnecessary "rm -f pbmtog3"
- delete redundant ( cd tools; make ... )

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.1.14
- AutoPPP patch
 
* Thu Dec 18 1997 Mike Wangsmo <wanger@redhat.com>
- added more of the documentation files to the rpm

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info support

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- updated version

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- now requires libgr-progs instead of netpbm

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc

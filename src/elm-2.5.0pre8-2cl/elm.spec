Summary: The elm mail user agent.
Summary(pt_BR): Agente de mail ELM
Summary(es): Agente de mail ELM
Name: elm
Version: 2.5.0pre8
Release: 2cl
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Url: http://www.myxa.com/elm.html
Source0: ftp://dsinc.myxa.com/pub/elm/elm2.5.0pre8.tar.gz
Source1: elm.wmconfig
Source800: elm-wmconfig.i18n.tgz
Patch0: elm-2.5.0pre8-config.patch
Patch1: elm-2.5.0pre8-compat21.patch
BuildRoot: /var/tmp/%{name}-root

%description
Elm is a popular terminal mode email user agent. Elm includes all
standard mailhandling features, including MIME support via metamail.

Elm is still used by some people, but is no longer in development. If
you've used Elm before and you're devoted to it, you should install the
elm package.  If you would like to use metamail's MIME support, you'll
also need to install the metamail package.

%description -l pt_BR
ELM é um popular leitor de mail em modo terminal. É poderoso, fácil
de usar e fácil de conseguir ajuda. Possui todas as características
que você poderia esperar, inclusive suporte a MINE (via metamail).

%description -l es
ELM es un popular lector de mail en modo terminal. Es potente,
fácil de usar y de conseguir ayuda. Posee todas las características
que se podría esperar, incluso soporte a MINE (vía metamail).

%prep
%setup -q -n elm2.5.0pre8

%patch0 -p1 -b .p11
%patch1 -p1 -b .p17

%build
mkdir -p bin
make	# XXX This make to rerun Makefile.SH everywhere ...
make	# XXX ... and this make to buils.
strip bin/* || :

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/elm,man/man1}

make	DESTBIN=$RPM_BUILD_ROOT/usr/bin \
	BIN=$RPM_BUILD_ROOT/usr/bin \
	DESTLIB=$RPM_BUILD_ROOT/usr/lib/elm \
	LIB=$RPM_BUILD_ROOT/usr/lib/elm \
	MAN=$RPM_BUILD_ROOT/usr/man/man1 \
	install

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
  install -m 644 $RPM_SOURCE_DIR/elm.wmconfig ./etc/X11/wmconfig/elm
)
 




tar xvfpz $RPM_SOURCE_DIR/elm-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(missingok) /etc/X11/wmconfig/elm
/usr/bin/elm
/usr/bin/answer
/usr/bin/checkalias
/usr/bin/elmalias
/usr/bin/fastmail
/usr/bin/frm
/usr/bin/listalias
/usr/bin/messages
/usr/bin/newalias
/usr/bin/newmail
/usr/bin/printmail
/usr/bin/readmsg
/usr/lib/elm
/usr/bin/wnewmail
/usr/bin/nfrm
/usr/man/man1/answer.1
/usr/man/man1/checkalias.1
/usr/man/man1/elm.1
/usr/man/man1/elmalias.1
/usr/man/man1/fastmail.1
/usr/man/man1/frm.1
/usr/man/man1/listalias.1
/usr/man/man1/messages.1
/usr/man/man1/newalias.1
/usr/man/man1/newmail.1
/usr/man/man1/printmail.1
/usr/man/man1/readmsg.1
/usr/man/man1/wnewmail.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 14 1999 Jeff Johnson <jbj@redhat.com>
- enable metamail support (#823)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.5.0pre8.

* Tue Jan 19 1999 Alex deVries <puffin@redhat.com>
- fixed it to build for all architectures

* Thu Jan 14 1999 Bill Nottingham <notting@redhat.com>
- build for arm

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue Jun 16 1998 Alan Cox <alan@redhat.com>
- Make elm non setgid and use fcntl locking (this is fine
  with procmail and matches our PINE setup).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Jan 07 1998 Erik Troan <ewt@redhat.com>
- removed filter -- it's a security problem

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

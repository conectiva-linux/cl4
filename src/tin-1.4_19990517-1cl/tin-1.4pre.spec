Summary: A basic Internet news reader.
Summary(pt_BR): Leitor de News
Summary(es): Lector de News
Name: tin
Version: 1.4_19990517
Release: 1cl
Serial: 1
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://ftp.tin.org/pub/news/clients/tin/pre-v1.4/tinpre-1.4-19990517.tar.bz2
Patch0: tinpre-1.4-egcs.patch
BuildRoot: /var/tmp/tin-root

%description
Tin is a basic, easy to use Internet news reader.  Tin can read news
locally or remotely via an NNTP (Network News Transport Protocol) server.

Install tin if you need a basic news reader.

%description -l pt_BR
Tin é um leitor de Netnews de tela cheia e fácil de usar. Ele
pode ler news localmente (isto é, /usr/spool/news) ou remotamente
(opção rtin ou tin -r) via um servidor NNTP (Network News Transport
Protocol).

%description -l es
Tin es un lector de Netnews de pantalla llena y fácil de usar. Puede
leer news localmente (es decir, /usr/spool/news) o remotamente
(opción rtin o tin -r) vía un servidor NNTP (Network News Transport
Protocol).

%prep
%setup -q -n tin-19990517
%patch -p1 -b .egcs

%build
./configure --verbose \
	--prefix=/usr \
	--with-spooldir=/var/lib/news \
	--enable-nntp \
	--enable-prototypes \
	--disable-echo \
	--disable-mime-strict-charset \
	--enable-color \
	--enable-ncurses \
	--enable-locale

make clean
CFLAGS=$RPM_OPT_FLAGS make build
%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/
/usr/bin/tin
/usr/bin/rtin
/usr/man/man1/tin.1

%changelog
* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 1.4-19990517

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- upgraded to latest dev version snapshot.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Dec 22 1998 Preston Brown <pbrown@redhat.com>
- upgraded again to latest snapshot.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- Alan is right; 1.22 is full of bugs and ANCIENT. Moved to latest tin.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jun 24 1998 Alan Cox <alan@redhat.com>
- turned on DONT_LOG_USER - get rid of the silly file in /tmp. We probably
  ought to move to a newer tin soon.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov 3 1997 Erik Troan <ewt@redhat.com>
- hacked to use just termios, not a motley mix of termios and termio

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

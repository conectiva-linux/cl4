Summary: Threaded News Reader
Summary(pt_BR): Leitor de News com Threads
Summary(es): Lector de News con Threads
Name: trn
Version: 3.6
Release: 17cl
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
#Source0:  ftp://ftp.uu.net:/networking/news/readers/trn/trn-3.6.tar.gz
# recompressed with bzip2
Source0:  ftp://ftp.uu.net:/networking/news/readers/trn/trn-3.6.tar.bz2
Source1: trn.wmconfig
Source800: trn-wmconfig.i18n.tgz
Patch0: trn-3.6-linux.patch
Patch1: trn-3.6-sigtstp.patch
Patch2: trn-3.6-make.patch
Patch3: trn-3.6-tmprace.patch
Summary(de): News-Reader mit Thread-Funktion
Summary(fr): Lecteur de news avec fils de discussion
Summary(tr): Haber grubu okuyucu
Buildroot: /var/tmp/trn-root

%description
`trn' is one of the original threaded news readers.  this version is
configured to read news from an NNTP news server.

%description -l pt_BR
'trn' é um dos leitores originais de threaded news. Esta versão é
configurada para ler news de um servidor NNTP.

%description -l es
'trn' es uno de los lectores originales de threaded news. Esta
versión está configurada para leer news de un servidor NNTP.

%description -l de
`trn' ist einer der ersten News-Reader mit Threads. Diese Version ist
für einen NNTP.News-Server konfiguriert.

%description -l fr
trn est l'un des premiers lecteurs de news avec fils de discussion.
Cette version est configurée pour lire les articles sur un serveur NNTP.

%description -l tr
trn, özgün haber grubu okuyuculardan biridir.

%prep
%setup -q 
%patch0 -p1 -b .linux
%patch1 -p1 -b .sigstp
%patch2 -p1 -b .make
%patch3 -p1 

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/trn
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/

chmod 755 filexp
chmod 755 makedir

make install RPM_INSTALL=$RPM_BUILD_ROOT

chmod 755 $RPM_BUILD_ROOT/usr/bin/*
chmod 755 $RPM_BUILD_ROOT/usr/lib/*

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#cp $RPM_SOURCE_DIR/trn.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/trn



tar xvfpz $RPM_SOURCE_DIR/trn-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README INSTALL MANIFEST HINTS.TRN HACKERSGUIDE NEW
/usr/bin/trn
/usr/bin/newsetup
/usr/bin/newsgroups
/usr/bin/Pnews
/usr/bin/Rnmail
/usr/bin/trn-artchk
/usr/bin/nntplist
/usr/lib/trn
/usr/man/man1/trn.1
/usr/man/man1/Pnews.1
/usr/man/man1/Rnmail.1
/usr/man/man1/newsetup.1
/usr/man/man1/newsgroups.1
%config /etc/X11/wmconfig/trn

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Mon Oct 30 1998 Marcelo Tosatti <marcelo@conectiva.com>
- arrumado tmp race no newsgroups

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig translated to pt_BR

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- added buildroot
- updated spec file

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Dec 30 1997 Erik Troan <ewt@redhat.com>
- SIGTSTP handler was flaky, which made ^Z fail w/ built against glibc
- added a wmconfig entry

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc 

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- some of the files in /usr/bin wrre 647, which makes no sense.

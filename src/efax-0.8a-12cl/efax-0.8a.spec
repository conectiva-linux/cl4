Summary: A program for faxing using a Class 1, 2 or 2.0 fax modem.
Summary(pt_BR): Envia e recebe faxes em modems classe 1 ou 2
Summary(es): Envía y recibe faxes en módems clase 1 ó 2
Name: efax
Version: 0.8a
Release: 12cl
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Source: http://metalab.unc.edu/pub/Linux/apps/serialcomm/fax/efax08a.tar.gz
Patch: efax08a-config.patch
Patch1: efax08a-strerror.patch
Patch2: efax08a-time.patch
Patch3: efax-08a-64bit.patch
Patch4: efax08a-glibc21.patch
Patch5: efax08a-nullptr.patch
BuildRoot: /var/tmp/efax-root

%description
Efax is a small ANSI C/POSIX program that sends and receives faxes using
any Class 1, 2 or 2.0 fax modem.

You need to install efax if you want to send faxes and you have a
Class 1, 2 or 2.0 fax modem.

%description -l pt_BR
Este é um programa para enviar e receber fax com fax/modems de classe
1 ou classe 2. Possui uma boa interface para facilitar o manuseio.

%description -l es
Este es un programa para enviar y recibir fax con fax/módems de clase
1 o clase 2. Posee una buena interface para facilitar el manejo.

%prep
%setup -q -n efax08a
%patch -p1
%patch1 -p1
%patch2 -p1
%ifarch alpha
%patch3 -p1
%endif
%patch4 -p1 -b .glibc21
%patch5 -p1 -b .nullptr

%build
make RPM_OPT_FLAGS="-ansi $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man install
strip $RPM_BUILD_ROOT/usr/bin/{efax,efix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%config /usr/bin/fax
/usr/bin/efax
/usr/bin/efix
/usr/man/man1/fax.1
/usr/man/man1/efax.1
/usr/man/man1/efix.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 11)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- patch to fix null ptr dereference
- added -ansi flag; fixes efix problem (produced bad tiff files)

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Michael Fulbright <msf@redhat.com>
- cleaned spec file to new standard, confirmed package is up to date

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Added efax-08a-64bit.patch from David Mosberger

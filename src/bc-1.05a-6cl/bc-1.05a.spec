Summary: GNU bc
Summary(pt_BR): GNU bc - calculadora de linha de comando
Summary(es): GNU bc - calculadora de línea de comando
Name: bc
Version: 1.05a
Release: 6cl
Copyright: GPL
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
# was .gz
Source: ftp://prep.ai.mit.edu/pug/gnu/bc-%{version}.tar.bz2
Prereq: info grep
Buildroot: /var/tmp/bc-root
Summary(de): GNU bc
Summary(fr): GNU bc
Summary(tr): GNU hesap makinasý

%description
bc is a text mode calculator of sorts.  It has many extended
features such as base translation.  It can also accept input
from stdin and return output. dc is the RPN version.

%description -l pt_BR
bc é uma calculadora modo texto. Ela possui várias características
estendidas como translação de base.

%description -l es
bc es una calculadora modo texto. Posee varias características
extendidas como translación de base.

%description -l de
bc ist eine Art Textmodus-Rechner, der viele erweiterte Funktionen
wie Basisübersetzung enthält. Er kann auch Eingaben von
stdin annehmen und die Ergebnisse ausgeben. dc ist die RPN-Version.

%description -l fr
bc est est un outil de calcul en mode texte. Il a des fonctionnalités
étendues comme la conversion de base. il peut aussi accepter l'entrée
sur stdin et retourner le résultat. dc est la version RPN.

%description -l tr
bc metin ekranda çalýþan bir hesap makinasýdýr. Taban dönüþümü gibi ileri
yetenekleri vardýr.

%prep
%setup -q -n bc-1.05

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr --with-readline
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install
gzip -n -9f $RPM_BUILD_ROOT/usr/info/dc.info

strip $RPM_BUILD_ROOT/usr/bin/dc $RPM_BUILD_ROOT/usr/bin/bc

%clean
rm -rf $RPM_BUILD_ROOT

%post
# previous versions of bc put an improper entry into /usr/info/dir -- remove
# it
if grep 'dc: (bc)' /usr/info/dir > /dev/null; then
    grep -v 'The GNU RPN calculator' < /usr/info/dir > /usr/info/dir.$$
    mv -f /usr/info/dir.$$ /usr/info/dir
fi

/sbin/install-info /usr/info/dc.info.gz /usr/info/dir --entry="* dc: (dc).                      The GNU RPN calculator."

%preun
if [ $1 = 0 ]; then
  /sbin/install-info --delete /usr/info/dc.info.gz /usr/info/dir --entry="* dc: (dc).                      The GNU RPN calculator."
fi

%files
%defattr(-,root,root)
/usr/bin/dc
/usr/bin/bc
/usr/man/man1/bc.1
/usr/man/man1/dc.1
/usr/info/dc.info.gz

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Sep 18 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.05a.

* Sun Jun 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.05 with build root.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Erik Troan <ewt@redhat.com>
- got upgrades of info entry working (I hope)

* Sun Apr 05 1998 Erik Troan <ewt@redhat.com>
- fixed incorrect info entry

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- added install-info support

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.03 to 1.04

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

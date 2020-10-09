Summary: A password-checking library.
Summary(pt_BR): Biblioteca de checagem de senhas
Summary(es): Biblioteca de chequeo de contrase�as
Name: cracklib
Version: 2.7
Release: 8cl
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/cracklib_2.7.tgz
Url: ftp://coast.cs.purdue.edu/pub/tools/unix/cracklib/
Copyright: artistic
Patch: cracklib-2.7-redhat.patch
Buildroot: /var/tmp/cracklib-root/

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop
users from choosing passwords which would be easy to guess. CrackLib
performs certain tests: 

* It tries to generate words from a username and gecos entry and 
  checks those words against the password;
* It checks for simplistic patterns in passwords;
* It checks for the password in a dictionary.

CrackLib is actually a library containing a particular
C function which is used to check the password, as well as
other C functions. CrackLib is not a replacement for a passwd
program; it must be used in conjunction with an existing passwd
program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you
install CrackLib, you'll also want to install the cracklib-dicts
package.

%description -l pt_BR
Inclui os dicion�rios cracklib para o padr�o /usr/dict/words,
assim como os utilit�rios necess�rios para criar dicion�rios.

%description -l es
Incluye los diccionarios cracklib para el padr�n /usr/dict/words,
as� como, los utilitarios necesarios para crear diccionarios.

%package dicts
Summary: The standard CrackLib dictionaries.
Summary(pt_BR): Dicion�rios para checagem de senhas
Summary(es): Diccionarios para chequeo de contrase�as
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas

%description dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/dict/words.  Cracklib-dicts also contains
the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%description -l pt_BR dicts
Inclui o dicion�rio cracklib para o padr�o /usr/dict/words, bem
como utilit�rios necess�rios a cria��o de novos dicion�rios.

%description -l es dicts
Incluye el diccionario cracklib para el padr�n /usr/dict/words,
bien como utilitarios necesarios a creaci�n de nuevos diccionarios.

%prep
%setup -n cracklib,2.7
%patch -p1 -b .rh

%build
make all

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{sbin,lib,include}
make install ROOT=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT/usr/sbin/packer

%files
%doc README MANIFEST LICENCE HISTORY POSTER
/usr/include/*
/usr/lib/lib*

%files dicts
/usr/sbin/*
/usr/lib/cracklib_dict*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat May 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.7
- build shared libraries

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added -fPIC

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- basic spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

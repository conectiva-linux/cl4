#
# gnupg -- gnu privacy guard
# This is a template.  The dist target uses it to create the real file.
#
%define version 0.9.8
%define name gnupg
Summary: GPL public key crypto
Summary(pt_BR): Criptografia com chaves públicas (assimétricas). GPL
Summary(es): Criptografía con llaves públicas (asimétricas). GPL
Name: %{name}
Version: %{version}
Release: 4cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
#Source: ftp://ftp.gnupg.org/pub/gcrypt/%{name}-%{version}.tar.gz
Source: %{name}-%{version}.tar.bz2
URL: http://www.gnupg.org
Provides: gpg openpgp
BuildRoot: /tmp/rpmbuild_%{name}

%changelog
* Sat Jun 26 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- simplified %files section

* Sat Jun 26 1999 Guilherme Manika <gwm@conectiva.com>
- Updated to 0.9.8

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Jan 12 1999 Fabio Coatti <cova@felix.unife.it>
- LINGUAS variable is now unset in configure to ensure that all
  languages will be built. (Thanks to Luca Olivetti <luca@luca.ddns.org>)
 
* Sat Jan 02 1999 Fabio Coatti <cova@felix.unife.it>
- Added pl language file.
- Included g10/pubring.asc in documentation files.

* Sat Dec 19 1998 Fabio Coatti <cova@felix.unife.it>
- Modified the spec file provided by Caskey L. Dickson <caskey-at-technocage.com>
- Now it can be built also by non-root. Installation has to be done as
root, gpg is suid.
- Added some changes by  Ross Golder <rossigee@bigfoot.com>
- Updates for version 0.4.5 of GnuPG (.mo files)

%description
GnuPG is a complete and free replacement for PGP. Because it does not
use IDEA or RSA it can be used without any restrictions. GnuPG is in
compliance with the OpenPGP specification (RFC2440).

%description -l pt_BR
O GNUPG é um substituto completo e de livre distribuição para o PGP. Como
ele não usa IDEA e RSA seu uso é irrestrito. Está quase completamente
de acordo com o rascunho (draft) OpenPGP.

%description -l es
GNUPG es un sustituto completo y de libre distribución para
PGP. Como no utiliza IDEA y RSA, su uso no está restringido. Está
casi completamente de acuerdo con el borrador (draft) OpenPGP.

%description -l it
GnuPG è un sostituto completo e gratuito per il PGP. Non utilizzando
IDEA o RSA può essere utilizzato senza restrizioni. GnuPG è conforme
alle specifiche OpenPGP (RFC2440).

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%setup

%build
if test -n "$LINGUAS"; then
 unset LINGUAS
fi    
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
make install-strip prefix=$RPM_BUILD_ROOT/usr
cd $RPM_BUILD_ROOT/usr/man/man1/
gzip -9 gpg.1
ln -s gpg.1.gz gpgm.1.gz
cd $RPM_BUILD_ROOT/usr/bin/
ln -s gpg gpgm

%files
%defattr(-,root,root)
%doc INSTALL AUTHORS COPYING ChangeLog NEWS
%doc README THANKS TODO PROJECTS 
%doc doc/DETAILS doc/FAQ doc/HACKING doc/OpenPGP
%doc g10/pubring.asc
/usr/man/man1/gpg.1.gz
/usr/man/man1/gpgm.1.gz
%attr (755,root,root) /usr/bin/gpg
/usr/bin/gpgm
/usr/share/locale/*/LC_MESSAGES/%{name}.mo
/usr/lib/%{name}
/usr/share/%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

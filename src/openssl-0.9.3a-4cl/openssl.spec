%define libmaj 0
%define libmin 9
%define librel 3a

%define openssldir /var/ssl

Summary: Secure Sockets Layer and cryptography libraries and tools
Summary(pt_BR): Uma biblioteca C que fornece vários algoritmos e protocolos criptográficos.
Summary(es): Una biblioteca C que ofrece varios algoritmos y protocolos criptográficos.
Name: openssl
Version: 0.9.3a
Release: 4cl
Source0: ftp://ftp.openssl.org/pub/openssl/%{name}-%{version}.tar.bz2
Copyright: Freely distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Provides: SSL
URL: http://www.openssl.org/
BuildRoot:   /tmp/%{name}-%{version}-root
Patch: openssl-0.9.3-cnc.patch
Obsoletes: SSLeay

%description
The openssl certificate management tool and the shared libraries that
provide various encryption and decription algorithms and protocols,
including DES, RC4, RSA and SSL.

 This product includes software developed by the
  OpenSSL Project for use in the OpenSSL Toolkit
 (http://www.openssl.org).

 This product includes cryptographic software written by
  Eric Young (eay@cryptsoft.com).
 This product includes software written by
  Tim Hudson (tjh@cryptsoft.com).

%description -l pt_BR
Uma biblioteca C que fornece vários algoritmos e protocolos
criptográficos, incluindo DES, RC4, RSA e SSL. Inclui bibliotecas
compartilhadas e utilitários.

%description -l es
Biblioteca C que ofrece varios algoritmos y protocolos,
como DES RC4, RSA, SSL y TLS. Incluye bibliotecas
compartidas y utilitarios.

%package devel
Summary: Secure Sockets Layer and cryptography static libraries and headers
Summary(pt_BR): Bibliotecas estáticas e arquivos de inclusão para desenvolvimento OpenSSL
Summary(es): Bibliotecas estáticas y archivos de inclusión para desarrollo OpenSSL
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: openssl
Obsoletes: SSLeay-devel

%description devel
The static libraries and include files needed to compile apps
with support for various cryptographic algorithms and protocols,
including DES, RC4, RSA and SSL.

 This product includes software developed by the
  OpenSSL Project for use in the OpenSSL Toolkit
  (http://www.openssl.org).
 This product includes cryptographic software written by
  Eric Young (eay@cryptsoft.com).
 This product includes software written by
  Tim Hudson (tjh@cryptsoft.com).

 Patches for many networking apps can be found at:
  ftp://ftp.psy.uq.oz.au/pub/Crypto/SSLapps/

%description -l pt_BR devel
Uma biblioteca C que fornece vários algoritmos e protocolos
criptográficos, incluindo DES, RC4, RSA e SSL. Inclui bibliotecas
estáticas e arquivos de inclusão para desenvolvimento.

%description -l es devel
Biblioteca C que ofrece varios algoritmos y protocolos, como
DES RC4, RSA, SSL y TLS. Incluye bibliotecas estáticas, archivos
de inclusión y utilitarios.

%prep

%setup -q
%patch -p1
# Set path to perl
perl util/perlpath.pl /usr/bin/perl
mv ./apps/der_chop ./apps/der_chop.bak
sed '/#!\/usr\/local\/bin\/perl/s//#!\/usr\/bin\/perl/' < ./apps/der_chop.bak > ./apps/der_chop 

%build 
./Configure --prefix=/usr --openssldir=%{openssldir} linux-elf
make linux-shared
LD_LIBRARY_PATH=`pwd` make
LD_LIBRARY_PATH=`pwd` make rehash

%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_PREFIX="$RPM_BUILD_ROOT"

# Install RSAref stuff
install -m644 rsaref/rsaref.h $RPM_BUILD_ROOT/usr/include/openssl
install -m644 libRSAglue.a $RPM_BUILD_ROOT/usr/lib

# Make backwards-compatibility symlink to ssleay
ln -s /usr/bin/openssl $RPM_BUILD_ROOT/usr/bin/ssleay

# Install shared libs
install -m755 libcrypto.so.0.9.3 $RPM_BUILD_ROOT/usr/lib
install -m755 libssl.so.0.9.3 $RPM_BUILD_ROOT/usr/lib
ln -s /usr/lib/libcrypto.so.0.9.3 $RPM_BUILD_ROOT/usr/lib/libcrypto.so.%{libmaj}
ln -s /usr/lib/libcrypto.so.0.9.3 $RPM_BUILD_ROOT/usr/lib/libcrypto.so
ln -s /usr/lib/libssl.so.0.9.3 $RPM_BUILD_ROOT/usr/lib/libssl.so.%{libmaj}
ln -s /usr/lib/libssl.so.0.9.3 $RPM_BUILD_ROOT/usr/lib/libssl.so

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc %attr(0644,root,root) CHANGES
%doc %attr(0644,root,root) CHANGES.SSLeay
%doc %attr(0644,root,root) LICENSE
%doc %attr(0644,root,root) NEWS
%doc %attr(0644,root,root) README
%doc %attr(0644,root,root) doc

%attr(0755,root,root) /usr/bin/*
%attr(0755,root,root) /usr/lib/*.so*
%attr(0755,root,root) %{openssldir}/misc/*

%config %attr(0644,root,root) %{openssldir}/openssl.cnf 
%dir %attr(0755,root,root) %{openssldir}/certs
%dir %attr(0755,root,root) %{openssldir}/lib
%dir %attr(0755,root,root) %{openssldir}/misc
%dir %attr(0750,root,root) %{openssldir}/private

%files devel
%doc %attr(0644,root,root) CHANGES
%doc %attr(0644,root,root) CHANGES.SSLeay
%doc %attr(0644,root,root) LICENSE
%doc %attr(0644,root,root) NEWS
%doc %attr(0644,root,root) README
%doc %attr(0644,root,root) doc
%doc %attr(0644,root,root) demos

%attr(0644,root,root) /usr/lib/*.a
%attr(0644,root,root) /usr/include/openssl/*

%post
ldconfig

%postun
ldconfig

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Jun 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Obsoletes SSLeay

* Tue Jun  1 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May 25 1999 Damien Miller <damien@ibs.com.au>
- Updated to version 0.9.3
- Added attributes for all files
- Paramatised openssl directory

* Sat Mar 20 1999 Carlo M. Arenas Belon <carenas@jmconsultores.com.pe>
- Added "official" bnrec patch and taking other out
- making a link from ssleay to openssl binary
- putting all changelog together on SPEC file

* Fri Mar  5 1999 Henri Gomez <gomez@slib.fr>
- Added bnrec patch

* Tue Dec 29 1998 Jonathan Ruano <kobalt@james.encomix.es>
- minimum spec and patches changes for openssl
- modified for openssl sources

* Sat Aug  8 1998 Khimenko Victor <khim@sch57.msk.ru>
- shared library creating process honours $RPM_OPT_FLAGS
- shared libarry supports threads (as well as static library)

* Wed Jul 22 1998 Khimenko Victor <khim@sch57.msk.ru>
- building of shared library completely reworked

* Tue Jul 21 1998 Khimenko Victor <khim@sch57.msk.ru>
- RPM is BuildRoot'ed

* Tue Feb 10 1998 Khimenko Victor <khim@sch57.msk.ru>
- all stuff is moved out of /usr/local

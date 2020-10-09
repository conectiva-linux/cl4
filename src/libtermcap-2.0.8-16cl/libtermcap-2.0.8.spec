Summary: library for accessing the termcap database
Summary(pt_BR): Biblioteca para acessar a base de dados termcap
Summary(es): Biblioteca para acceder a base de datos termcap
Name: libtermcap
Version: 2.0.8
Release: 16cl
Source: ftp://sunsite.unc.edu/pub/Linux/GCC/termcap-2.0.8.tar.bz2
Url: ftp://sunsite.unc.edu/pub/Linux/GCC/
Copyright: LGPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Patch: termcap-2.0.8-shared.patch
Patch1: termcap-2.0.8-setuid.patch
Patch2: termcap-2.0.8-instnoroot.patch
Patch3: termcap-2.0.8.termcap.texi.patch
Requires: termcap
BuildRoot: /var/tmp/libtermcap-root
Summary(de): Library zum Zugriff auf die termcap-Datenbank
Summary(fr): Librairie pour acc�der � la base de donn�es termcap.
Summary(tr): termcap veri taban�na eri�im kitapl���

%description
This is the library for accessing the termcap database.  It is necessary
to be installed for a system to be able to do much of anything.  

%description -l pt_BR
Esta � a biblioteca para acesso ao banco de dados termcap.

%description -l es
Esta es la biblioteca para acceso al banco de datos termcap.

%package devel
Summary: development libraries and header files for termcap library
Summary(pt_BR): Biblioteca para desenvolvimento e arquivos de inclus�o para biblioteca termcap
Summary(es): Biblioteca para desarrollo y archivos de inclusi�n para biblioteca termcap
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: libtermcap
Summary(de): Entwicklungs-Libraries und Header-Dateien f�r die termcap-Library
Summary(fr): Librairies de d�veloppement et fichiers d'en-t�te pour la librairie termcap.
Summary(tr): termcap kitapl���n� kullanan programlar geli�tirmek i�in gerekli dosyalar

%description devel
This is the package containing the development libaries and header
files for writing programs that access the termcap database.  It may
be necessary to build some other packages as well.

%description -l pt_BR devel
Este � o pacote que cont�m as bibliotecas e arquivos de inclus�o
para a escrita de programas que acessam o banco de dados termcap. Ele
pode ser necess�rio para construir outros pacotes tamb�m.

%description -l es devel
Este es el paquete que contiene las bibliotecas y archivos de
inclusi�n para la escritura de programas que acceden al banco de
datos termcap.  Puede ser necesario tambi�n para construir otros
paquetes.

%description -l de devel
Dies ist ein Paket mit Entwicklungs-Libraries und Header-Dateien
zum Schreiben von Programmen, die auf die termcap-Datenbank
zugreifen. Eventuell m�ssen noch ein paar andere Pakete gebaut
werden.

%description -l de
Dies ist die Library zum Zugriff auf die termcap-Datenbank. Sie mu�
installiert werden, damit das System funktionsf�hig ist.

%description -l fr devel
Ceci est le package contenant les biblioth�ques de d�veloppement et
les fichiers d'en-t�te pour �crire des programmes acc�dant � la base 
de donn�es termcap. Cela peut �tre n�cessaire pour construire certains
autres packages.

%description -l fr
Biblioth�que pour acc�der � la base de donn�es termcap. N�cessaire pour
qu'un syst�me puisse faire quelque chose.

%description -l tr devel
Bu paket, termcap veri taban�n� kullanan programlar geli�tirmek i�in gereken
ba�l�k dosyalar� ve kitapl�klar� i�erir.

%description -l tr
Bu paket termcap veri taban�na ula��m kitapl���n� i�erir. Sistem �zerinde
pek �ok �eyi yapabilmek i�in kurulu olmas� gerekmektedir.

%prep
%setup -q -n termcap-2.0.8
%patch -p1
%patch1 -p1
%patch2 -p1 -b .nochown
%patch3 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{usr/lib,usr/info,usr/include,etc,lib}

export PATH=/sbin:$PATH
make prefix=$RPM_BUILD_ROOT/usr install

install -m644 termcap.src $RPM_BUILD_ROOT/etc/termcap
cp termcap.info* $RPM_BUILD_ROOT/usr/info

( cd $RPM_BUILD_ROOT
  rm -f ./etc/termcap
  mv ./usr/lib/libtermcap.so* ./lib
  ln -sf libtermcap.so.2.0.8 ./lib/libtermcap.so
  ln -sf ../../lib/libtermcap.so.2.0.8 ./usr/lib/libtermcap.so
  gzip -9nf ./usr/info/termcap.info*
  chmod 644 ./usr/info/termcap.info*
)

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%trigger -- info >= 3.12
/sbin/install-info \
	--section="Libraries" --entry="* Termcap: (termcap).               The GNU termcap library." \
	--info-dir=/usr/info /usr/info/termcap.info.gz

%postun
if [ $1 = 0 ]; then
    /sbin/install-info --delete \
	--section="Libraries" --entry="* Termcap: (termcap).               The GNU termcap library." \
	--info-dir=/usr/info /usr/info/termcap.info.gz
fi
/sbin/ldconfig

%files
%defattr(-,root,root)
/usr/info/termcap.info*
/lib/libtermcap.so.2.0.8

%files devel
%defattr(-,root,root)
/usr/lib/libtermcap.a
/usr/lib/libtermcap.so
/usr/include/termcap.h

%changelog
* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- termcap-2.0.8.termcap.texi.patch

* Mon May 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- fixed Requires

* Thu Oct 22 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 05 1998 Erik Troan <ewt@redhat.com>
- run install-info from a %trigger so we don't have to make it a prereq; as
  termcap is used by bash, the install ordering issues are hairy
- commented out the chown stuff from 'make install' so you don't have to
  be root to build this
- don't run ldconfig if prefix= is used during 'make install'

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root.

* Tue Jun 30 1998 Alan Cox <alan@redhat.com>
- But assume system termcap is sane. Also handle setfsuid return right.

* Tue Jun 30 1998 Alan Cox <alan@redhat.com>
- TERMCAP environment hole for setuid apps squished.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

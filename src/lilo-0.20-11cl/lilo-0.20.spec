Summary: Boot loader for Linux and other operating systems
Summary(pt_BR): Carregador de boot para Linux e outros sistemas operacionais
Summary(es): Cargador de arranque para Linux y otros sistemas operativos
Name: lilo
Version: 0.20
Release: 11cl
Exclusivearch: i386
Copyright: MIT
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
#Source: ftp://sunsite.unc.edu/pub/Linux/system/boot/lilo/lilo-20.tar.gz
# recompactado com bzip2
Source: ftp://sunsite.unc.edu/pub/Linux/system/boot/lilo/lilo-20.tar.bz2
Buildroot: /var/tmp/lilo-root
Summary(de): Boot-Lader f�r Linux und andere Betriebssysteme
Summary(fr): Chargeur de boot pour Linux et autres syst�mes d'exploitation
Summary(tr): Linux ve diger i�letim sistemleri i�in sistem y�kleyici

%changelog
* Tue Jun  1 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- final rebuild for 3.0
- created lilo-doc subpackage

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to release 0.20
- uses a build root

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
Lilo is repsonsible for loading your linux kernel from either a floppy
or a hard drive and giving it control of the system. It can also be
used to boot many other operating sysetms, including the BSD variants,
DOS, and OS/2.

%description -l pt_BR
Lilo � respons�vel pelo carregamento do kernel Linux de um disquete
ou do disco r�gido, dando a ele o controle do sistema. Ele pode
tamb�m ser usado para "bootar" v�rios outros sistemas operacionais,
incluindo variantes de BSD, DOS e OS/2.

%description -l es
Lilo es responsable de cargar el kernel Linux de un disquete o
del disco duro, d�ndole el control del sistema. Puede tambi�n ser
usado para "bootar" varios otros sistemas operativos, incluyendo
variantes de BSD, DOS y OS/2.

%description -l de
Lilo ist zust�ndig f�r das Laden des Linux-Kernels, entweder von einer
Diskette oder einer Festplatte, und �bergibt diesem dann die Kontrolle
�ber das System. Es kann auch benutzt werden, um viele andere
Betriebssysteme zu laden, etwa die BSD-Varianten, DOS und OS/2.

%description -l tr
Lilo, Linux �ekirde�inin disket veya sabit disk s�r�c�den y�klenmesinden
sorumludur. Ayr�ca pek �ok di�er i�letim sisteminin de a��l��ta y�klenmesi
i�in kullan�l�r. Bu sistemler aras�nda BSD t�revleri, DOS ve OS/2 say�labilir.

%package doc
Summary: Documentation on lilo
Summary(pt_BR): Documenta��o sobre o lilo
Summary(es): Documentaci�n sobre lilo
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n

%description doc
Documentation on lilo

%description -l pt_BR doc
Documenta��o sobre o lilo

%description -l es doc
Documentaci�n sobre lilo

%prep
%setup -n lilo

%build
make
cd doc
make
dvips user.dvi -o User_Guide.ps
dvips tech.dvi -o Technical_Guide.ps
rm -f *.aux *.log *.toc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make install ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/lilo.conf ]; then
	/sbin/lilo > /dev/null
fi

%files
/boot/boot.b
/boot/chain.b
/boot/os2_d.b
/sbin/lilo

%files doc
%doc doc
%doc README

Summary: Creates shared library cache and maintains symlinks
Summary(pt_BR): Cria cache de bibliotecas compartilhadas e mant�m os links simb�licos
Summary(es): Crea cach� de bibliotecas compartidas y mantiene los links simb�licos
Name: ldconfig
Version: 1.9.9
Release: 5cl
Copyright: GPL
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source: ftp://ftp.yggdrasil.com/private/hjl/%{name}-980708.tar.gz
Patch: %{name}.patch
Summary(de): Erstellt ein shared library cache und verwaltet symlinks
Summary(fr): Cr�e un cache de biblioth�que partag�e et g�re les liens symboliques
Summary(pl): Tworzy cache bibliotek dynamicznych i ich symlinki
Summary(tr): Ortak kitapl�k �nbelle�i yarat�r ve ba�lant�lar� kurar
Buildroot: /tmp/%{name}-%{verson}-%{release}-root

%description
ldconfig scans a running system and sets up the symbolic links that are
used to load shared libraries properly. It also creates /etc/ld.so.cache
which speeds the loading programs which use shared libraries.

%description -l pt_BR
O ldconfig examina um sistema e mant�m os links simb�licos que s�o
usados para carregar adequadamente as bibliotecas compartilhadas. Ele
tamb�m cria o arquivo /etc/ld.so.cache que acelera a carga dos
programas que essas bibliotecas.

%description -l es
ldconfig examina un sistema y mantiene los links simb�licos que se
usan para cargar adecuadamente las bibliotecas compartidas. Tambi�n
crea el archivo /etc/ld.so.cache que acelera el proceso de carga
de los programas que utilizan estas bibliotecas.

%description -l pl
Ldconfig testuje uruchominy system i tworzy symboliczne linki, kt�re s�
nast�pnie u�ywane do poprawnego �adowania bibliotek dynamicznych. Program 
ten tworzy plik /etc/ld.so.chache, kt�ry przy�piesza wywo�anie dowolnego 
programu korzystaj�cego z bibliotek dynamicznych.

%description -l de
ldconfig scannt ein laufendes System und richtet die symbolischen 
Verkn�pfungen zum Laden der gemeinsam genutzten Libraries ein.
Au�erdem erstellt es /etc/ld.so.cache, was das Laden von Programmen
mit gemeinsam genutzten Libraries beschleunigt.

%description -l fr
ldconfig analyse un syst�me et configure les liens symboliques utilis�s
pour charger correctement les biblioth�ques partag�es. Il cr�e aussi
/etc/ld.so.cache qui acc�l�re le chargement des programmes utilisant
les biblioth�ques partag�es.

%description -l tr
ldconfig, �al��makta olan sistemi ara�t�r�r ve ortak kitapl�klar�n d�zg�n bir
�ekilde y�klenmesi i�in gereken simgesel ba�lant�lar� kurar. Ayr�ca ortak
kitapl�klar� kullanan programlar�n y�klenmesini h�zland�ran /etc/ld.so.cache
dosyas�n� yarat�r.

%prep
%setup -q -n %{name}-980708
%patch -p1

%build
rm -f ldconfig
gcc -o ldconfig $RPM_OPT_FLAGS -D_LIBC -static ldconfig.c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/sbin
install -s ldconfig $RPM_BUILD_ROOT/sbin/ldconfig

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(711,root,root) /sbin/ldconfig

%changelog
* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Dec  8 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- patch refeito para incluir somente linux/a.out.h

* Tue Oct 06 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
[1.9.9-1d]
- translation modified for pl,
- updated to ldconfig-980708,
- restricted ELF binary permissions,
- minor modifications of the spec file.

* Sun Jun 14 1998 Wojtek Slusarczyk <wojtek@shadow.eu.org>
[1.9.5-6]
- build against glibc-2.1

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>

- patched to remove broken symlinks

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>

- updated the formerly Alpha only version to the latest from 
  HJ Lu.  It should now be used on all platforms.
- added BuildRoot support
- added this changelog ;-)

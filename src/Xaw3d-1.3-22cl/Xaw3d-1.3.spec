Summary: X athena widgets in 3d
Summary(pt_BR): Widgets X athena em 3d
Summary(es): Widgets X athena en 3D
Name: Xaw3d
Version: 1.3
Release: 22cl
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
#Source: ftp://ftp.x.org:/contrib/widgets/Xaw3d/R6.1/Xaw3d-1.3.tar.gz
# recompressed with bzip2
Source: ftp://ftp.x.org:/contrib/widgets/Xaw3d/R6.1/Xaw3d-1.3.tar.bz2
Url: ftp://ftp.x.org/contrib/widgets/Xaw3d/
Patch: Xaw3d-1.1-shlib.patch
Patch1: Xaw3d-1.3-glibc.patch
Copyright: MIT
Prefix: /usr
Prereq: fileutils
Summary(de): X-Athena-Widgets in 3D 
Summary(fr): Widgets X Athena en 3D
Summary(tr): 3D X Athena arayüz elemanlarý (widgets)
BuildRoot: /var/tmp/Xaw3d-root

%description
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes.

%description -l pt_BR
Xaw3d é uma versão incrementada do conjunto MIT Athena Widget para
X Window que adiciona uma aparência tri-dimensional às aplicações
com mudanças mínimas ou nenhuma nos códigos fonte.

%description -l es
Xaw3d es una versión incrementada del conjunto MIT Athena Widget
para X Window que adiciona una apariencia tridimensional a las
aplicaciones con cambios mínimos, o ninguno, en los códigos fuente.

%package devel
Summary: Files for developing programs that use Xaw3d
Summary(pt_BR): Arquivos para desenvolvimento de programas que usam Xaw3d
Summary(es): Archivos para desarrollo de programas que usan Xaw3d
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: Xaw3d
Summary(de): Dateien zur Entwicklung von Programmen, die Xaw3d benutzen 
Summary(fr): Fichiers pour développer des programmes utilisant Xaw3d
Summary(tr): Xaw3d kitaplýðýný kullanan programlar geliþtirmek için gerekli dosyalar

%description devel
Xaw3d is an enhanced version of the MIT Athena Widget set for X Windows
that adds a 3-dimensional look to the applications with minimal or no
source code changes. This package includes the header files and static
libraries for developing programs that take full advantage of Xaw3d's
features.

%description -l pt_BR devel
Xaw3d é uma versão incrementada do conjunto MIT Athena Widget para
X Window que adiciona uma visão tri-dimensional às aplicações com
mudanças mínimas ou nenhuma nos códigos fonte. Este pacote inclui
os arquivos principais e as bibliotecas estáticas para programas
de desenvolvimento que utilizam total vantagem das características
de Xaw3d.

%description -l es devel
Xaw3d es una versión incrementada del conjunto MIT Athena Widget para
X Window que adiciona una visión tridimensional a las aplicaciones
con cambios mínimos, o ninguno, en los códigos fuente. Este paquete
incluye los archivos principales y las bibliotecas estáticas
para programas de desarrollo que utilizan total ventaja de las
características de Xaw3d.

%description -l de devel
Xaw3d ist eine erweiterte Version des MIT-Athena Widget-Sets für X-Windows, 
das einer Applikationen mit minimalen oder keinen Änderungen am Quellcode
einen 3D-Look verleiht. Das Paket enthält die Headerdateien und 
statischen Libraries zur Entwicklung von Programmen, die die Vorteile 
von Xaw3d voll nutzen.

%description -l de
Xaw3d ist eine erweiterte Version des MIT Athena Widget Set für X Windows,
das die Anwendung dreidimensional erscheinen läßt, ohne daß umfangreiche 
Änderungen am Quellcode notwendig sind.

%description -l fr devel
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT pour
X Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout,
de modification du code. Ce paquetage contient les en-têtes et les
bibliothèques statiques pour développer des programmes tirant plein
avantage des caractéristiques de Xaw3d

%description -l fr
Xaw3d est une version améliorée de l'ensemble Athena Widget du MIT pour
X Window qui ajoute un aspect 3D aux applications avec peu, ou pas du tout,
de modification du code.

%description -l tr devel
Bu paket, Xaw3d kitaplýðýný kullanan programlar geliþtirmek için gereken
baþlýk dosyalarý ve statik kitaplýklarý içerir.

%description -l tr
Xaw3d, MIT Athena kitaplýðýna, uygulamalara herhangi bir kod deðiþikliði
yapýlmasýný gerektirmeden (ya da ufak deðiþiklikler yaparak), üç boyutlu
bir görüntü kazandýran bir geliþtirmedir.

%prep
%setup -q -c
cd xc/lib/Xaw3d
%patch -p0
ln -s .. X11

%patch1 -p4

%build
cd xc/lib/Xaw3d
export PATH=/usr/X11R6/bin:$PATH
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
cd xc/lib/Xaw3d
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11

ln -s ../Xaw3d $RPM_BUILD_ROOT/usr/X11R6/include/X11

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
if [ ! -d /usr/X11R6/include/X11/Xaw3d ] ; then
	rm -f /usr/X11R6/include/X11/Xaw3d
	ln -sf ../Xaw3d /usr/X11R6/include/X11
fi

%triggerpostun -- Xaw3d-devel < 1.3-17
rm -rf /usr/X11R6/include/X11/Xaw3d
ln -sf ../Xaw3d /usr/X11R6/include/X11

%files
%defattr(-,root,root)
/usr/X11R6/lib/*.so.*

%files devel
%defattr(-,root,root)
/usr/X11R6/lib/*.a
/usr/X11R6/lib/*.so
/usr/X11R6/include/Xaw3d
%ghost /usr/X11R6/include/X11/Xaw3d

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  2 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- handle the symlink with triggers instead of getting rid of it

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- remove backward compatible symlink.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- fixed the bad symlink
- BuildRoot

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Nov 04 1997 Erik Troan <ewt@redhat.com>
- don't lave an improper return code from %pre

* Mon Nov 03 1997 Cristian Gafton <gafton@redhat.com>
- take care of the old location of the Xaw3d includes in case that one exist
- updated Prereq: field

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com
- fixed the -devel package for the right include files path

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- minor spec file cleanups

* Wed Oct 01 1997 Erik Troan <ewt@redhat.com>
- i18n widec.h patch needs to be applied on all systems

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- changed axp check to alpha

* Mon Jun 16 1997 Erik Troan <ewt@redhat.com>
- built against glibc

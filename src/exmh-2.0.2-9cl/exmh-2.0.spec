Summary: EXMH mail program
Summary(pt_BR): Interface gr�fica para o programa de mail MH
Summary(es): Interface gr�fica para el programa de mail MH
Name: exmh
Version: 2.0.2
Release: 9cl
Requires: mh metamail
Copyright: freeware
Group: Applications/Internet
Group(pt_BR): Aplica��es/Internet
Group(es): Aplicaciones/Internet
BuildArchitectures: noarch
Source0: ftp://ftp.sunlabs.com/exmh-2.0.2.tar.bz2
Source800: wmconfig.i18n.tgz
Url: http://www.beedub.com/exmh/
Patch1: exmh-2.0.2-conf.patch
BuildRoot: /var/tmp/exmh-root
Summary(de): EXMH-Mail-Programm
Summary(fr): Programme de courrier EXMH
Summary(tr): e-posta yaz�l�m�

%description
exmh is a graphical interface to the MH mail system.  It includes
MIME support, faces, glimpse indexing, color highlighting, PGP
interface, and more.  Requires sox (or play) for sound support.

%description -l pt_BR
exmh � uma interface gr�fica para o sistema de mail MH. Ela inclui
suporte para MIME, quadros, indexa��o r�pida, destacamento de cores,
interface PGP, e mais.

%description -l es
exmh es una interface gr�fica para el sistema de mail MH. Incluye
soporte para MINE, cuadros, indexaci�n r�pida, realce de colores,
interface PGP, y m�s.

%description -l de
exmh ist eine grafische Oberfl�che f�r das MH-Mail-System. Zu den
Funktionen geh�ren MIME-Unterst�tzung, Faces, Glimpse-Indexing, 
farbiges Markieren, PGP-Schnittstelle usw. Erfordert sox (oder play)
f�r Sound-Unterst�tzung.

%description -l fr
exmh est uen interface graphique au syst�me de courrier MH. Il
g�re MIME, les aspects, l'indexation glimpse, la mise en valeur par
couleurs, PGP, et autres. Il faut sox (ou play) pour g�r�r le son. 

%description -l tr
exmh, yayg�n olarak kullan�lan mh paketi i�in X11 aray�z�d�r. MIME deste�i,
PGP deste�i, faces, glimpse yard�m�yla dizin olu�turma gibi yetenekleri
vard�r. Ses deste�i i�in sox (ya da play) gerekir.

%prep
%setup -q -n exmh-%{PACKAGE_VERSION}
for i in *.MASTER; do
	cp $i ${i%%.MASTER}
done
%patch1 -p1
find . -name "*.orig" -exec rm {} \;

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
mkdir -p $RPM_BUILD_ROOT/usr/lib/exmh-%{PACKAGE_VERSION}

for i in exmh exmh-bg exmh-async ftp.expect; do
	install -m755 $i $RPM_BUILD_ROOT/usr/bin
done
for i in *.l; do
	install -m644 $i $RPM_BUILD_ROOT/usr/man/man1/${i%%.l}.1
done

cp -ar lib/* $RPM_BUILD_ROOT/usr/lib/exmh-%{PACKAGE_VERSION}

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYRIGHT exmh.CHANGES exmh.COLORS exmh.README
%config /etc/X11/wmconfig/exmh
/usr/bin/exmh
/usr/bin/exmh-bg
/usr/bin/exmh-async
/usr/bin/ftp.expect
/usr/lib/exmh-%{PACKAGE_VERSION}
/usr/man/man1/exmh.1

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuilt to remove TkStep-replace dependencies

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- exmh.wmconfig translated to pt_BR

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Apr 10 1998 Donnie Barnes <djb@redhat.com>
- updated to 2.0.2

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig support

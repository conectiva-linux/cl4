Summary: Units conversion program.
Summary(pt_BR): Programas de conversão de unidades.
Summary(es): Programas de conversión de unidades.
Name: units
Version: 1.0
Release: 14cl
Source: ftp://lth.se/pub/usenet/comp.sources.misc/volume38/units/part01.gz
Patch0: units-1.0-makefile.patch
Patch1: units-1.0-jbj.patch
Copyright: freely distributable
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
BuildRoot: /var/tmp/units-root
Summary(de): Einheitenkonvertierungsprogramm
Summary(fr): Programme de conversion d'unités
Summary(tr): Birim dönüþtürme programý

%description
The units program converts quantities expression in various scales to their
equivalents in other scales. The units program can only handle multiplicative
scale changes.

%description -l pt_BR
O programa units converte expressões de quantidade em várias escalas
para seus equivalentes em outras escalas. Ele somente pode manipular
mudanças multiplicativas de escala.

%description -l es
El programa units convierte expresiones de cantidad en varias escalas
para sus equivalentes en otras escalas. Solamente puede manipular
cambios multiplicativos de escala.

%description -l de
Das Programm 'units' konvertiert Mengenausdrücke in verschiedenen Maßstäben
in die entsprechenden Werte des anderen Maßstabs um. Das Programm kann
nur multiplikative Maßstabsänderungen verarbeiten.

%description -l fr
Le programme units convertit des quantités exprimées en différents systèmes
en leur équivalents sous d'autres systèmes. Il ne peut gérer que les
changements multiplicatifs de systèmes. 

%description -l tr
units programý, çeþitli birimlerdeki büyüklükleri baþka birimlere çevirir.

%prep
%setup -q -T -c
cd $RPM_BUILD_DIR/units-1.0
zcat $RPM_SOURCE_DIR/part01.gz | tail -1683 | sh
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}

install -s -m 755 units $RPM_BUILD_ROOT/usr/bin
install -m 644 units.lib $RPM_BUILD_ROOT/usr/lib
install -m 644 units.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/units
/usr/lib/units.lib
/usr/man/man1/units.1

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 19 1998 Conectiva <bugs@conectiva.com>
- added pt_BR translations

* Sun Aug 23 1998 Jeff Johnson <jbj@redhat.com>
- units.lib corrections (problem #685)

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

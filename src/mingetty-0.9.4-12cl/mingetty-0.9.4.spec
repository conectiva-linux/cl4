Summary: a compact, console-only getty
Summary(pt_BR): Um getty compacto, que s� funciona na console
Summary(es): Un getty compacto, que s�lo funciona en la consola
Name: mingetty
Version: 0.9.4
Copyright: GPL
Release: 12cl
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Source0: ftp://jurix.jura.uni-sb.de/pub/linux/source/system/daemons/mingetty-0.9.4.tar.gz
Source700: mingetty-man-pt_BR.tar
Patch0: mingetty-0.9.4-make.patch
Patch1: mingetty-0.9.4-glibc.patch
Patch2: mingetty-0.9.4-isprint.patch
Patch3: mingetty-0.9.4-wtmplock.patch
BuildRoot: /var/tmp/mingetty-root
Summary(de): ein kompaktes, auf Konsolen beschr�nktes GETTY 
Summary(fr): getty compact, uniquement pour la console
Summary(tr): Ufak bir getty

%description
mingetty, by Florian La Roche, is a lightweight, minimalist getty for
use on virtual consoles only.  mingetty is not suitable for serial
lines (the author recommends using `mgetty' for that purpose).

%description -l pt_BR
mingetty, de Florian La Roche, � um leve e pequeno getty para usar
somente em consoles virtuais. Mingetty n�o � apropriado para linhas
seriais (o autor recomenda o uso de "mgetty" para este prop�sito.

%description -l es
mingetty, de Florian La Roche, es un ligero y peque�o getty para
usar solamente en pantallas virtuales. Mingetty no es apropiado
para l�neas seriales (el autor recomienda el uso de "mgetty" para
este prop�sito.

%description -l de
mingetty von Florian La Roche ist ein kleiner, minimalistischer getty
f�r die Verwendung an virtuellen Konsolen. Er ist nicht f�r serielle
Leitungen geeignet (der Autor empfiehlt f�r diesen Zweck`mgetty').

%description -l fr
mingetty, de Florian La Roche, est un getty r�duit et all�g� pour
console virtuelle uniquement. mingetty n'est pas adapt� pour les lignes
s�rie (l'auteur recommande d'utiliser `mgetty' pour cet usage). 

%description -l tr
Bu pakette seri ba�lant� �zerinden sisteme giri�e olanak veren, ak�ll� bir
getty s�r�m� bulunur. Otomatik arama ve faks deste�i i�erir (sa�lad��� fax
deste�inin tam olarak kullan�labilmesi i�in mgetty-sendfax paketi gerekir).

%prep
%setup -q
%patch0 -p0 -b .make
%patch1 -p1 -b .glibc
%patch2 -p1 -b .isprint
%patch3 -p1 -b .wtmplock

%build
make "RPM_OPTS=$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,usr/man/man8}

install -m 0755 -s mingetty $RPM_BUILD_ROOT/sbin/
install -m 0644 mingetty.8 $RPM_BUILD_ROOT/usr/man/man8/




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/mingetty-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ANNOUNCE COPYING TODO
/sbin/mingetty
/usr/man/man8/mingetty.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado para o 3.0

* Sat Dec  5 1998 Conectiva <dist@conectiva.com>
- man pages revisadas

* Tue Nov 17 1998 Conectiva <dist@conectiva.com>
- added pt_BR man pages

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- fixed build problems on intel and alpha for manhattan

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

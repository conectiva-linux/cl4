Summary: X Windows Programming Environment
Summary(pt_BR): Ambiente de programa��o X Window
Summary(es): Ambiente de programaci�n X Window
Name: xwpe
%define	version	1.5.18a
Version: %{version}
Release: 2cl
Copyright: GPL
Url: http://www.rpi.edu/~payned/xwpe
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
#
#Source: ftp://ftp.rrzn.uni-hannover.de/pub/systems/unix/xwpe/xwpe-1.4.2.tar.Z
#Source: http://www.rpi.com/~payned/xwpe/xwpe-%{version}.tgz
# recompressed with bzip2
Source: http://www.rpi.com/~payned/xwpe/xwpe-%{version}.tar.bz2
Source1: xwpe.wmconfig
Source800: xwpe-wmconfig.i18n.tgz
Prefix: /usr
Summary(de): X-Windows-Programmierumgebung
Summary(fr): Environnement de programmation X Window
Summary(tr): X Windows program geli�tirme ortam�
BuildRoot: /var/tmp/xwpe-root

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe.
They are different versions of the same basic programmers editor and
development environment. If you have used some of the Micro$oft
Windows programming IDE's and longed for an X Windows equivalent, this
is what you have been looking for! Also included are the text-mode
equivalents of the X programs, enabling you to use xwpe no matter what
your development environment may be.

This package includes the basic xwpe libraries and the text-mode programs;
the X Windows programs are contained in the 'xwpe-X11' package.

%description -l pt_BR
O XWPE � na verdade um pacote de 4 programas: we, wpe, xwe,
e xwpe. Eles s�o diferentes vers�es do mesmo ambiente de
desenvolvimento e editor de programa��o. Se voc� usou algum dos
ambientes de programa��o do Micro$oft Windows e quer algo equivalente
no X, voc� achou o que estava procurando! Tamb�m est�o inclu�dos
as vers�es em modo texto dos programas, deixando voc�s usar o xwpe
n�o importando o tipo de ambiente de desenvolvimento que tenha. Este
pacote inclui as bibliotecas b�sicas do xwpe e os programas em modo
texto; os programas para X est�o no pacote 'xwpe-X11'.

%description -l es
XWPE es en realidad un paquete de 4 programas: we, wpe, xwe, y
xwpe. Son diferentes versiones del mismo ambiente de desarrollo
y editor de programaci�n. Si has usado alg�n de los ambientes de
programaci�n del Micro\$oft Windows y quieres algo equivalente en
el X, acabas de encontrar lo que buscabas. Tambi�n se incluyen las
versiones en modo texto de los programas, dejando que usen el xwpe
no importando el tipo de ambiente de desarrollo que tengas. Este
paquete incluye las bibliotecas b�sicas del xwpe y los programas
en modo texto; los programas para X est�n en el paquete 'xwpe-X11'.

%package X11
Summary: X Windows Programming Environment - X11 programs
Summary(pt_BR): Ambiente de Programa��o X Window - Programas X11
Summary(es): Ambiente de Programaci�n X Window - Programas X11
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Summary(de): X-Windows-Programmierumgebung - X11-Programme 
Summary(fr): Environnement de programmation X Window - programmes X11
Summary(tr): X Windows Programming Environment - t�mle�ik geli�tirme ortam�

%description X11

Includes the 'xwpe' and 'xwe' programs from the xwpe package that are
specific to X Windows.

%description -l pt_BR X11
Inclui os programas 'xwpe' e 'xwe' do pacote xwpe que s�o espec�ficos
para X Window.

%description -l es X11
Incluye los programas 'xwpe' y 'xwe' del paquete xwpe que son
espec�ficos para X Window.

%description -l de X11
Beinhaltet die 'xwpe'- und 'xwe'-Programme aus dem xwpe-Paket, die 
X-Windows-spezifisch sind.

%description -l de
XWPE sind eigentlich 4 Programme: we, wpe, xwe und xwpe.
Dies sind verschiedene Versionen desselben elementaren Programmeditors 
und derselben Entwicklungsumgebung. Wenn Sie bereits mit manchen der 
Micro$oft-Windows-Programmier-IDEs gearbeitet und sich nach einem X-
Windows-�quivalent gesehnt haben, dann ist das hier die L�sung f�r 
Sie! Ebenfalls eingeschlossen sind die Textmodus-�quivalente der 
X-Programme, so da� Sie xwpe benutzen k�nnen, unabh�ngig davon, in 
welcher Entwicklungsumgebung sie arbeiten.

Das Paket schlie�t die Grund-xwpe-Libraries und die Textmodusprogramme 
mit ein; die X Windows-Programme sind Teil des xwpe-X11-Pakets.

%description -l fr
xwpe is un paquetage de quatre programmes : we, wpe, xwe et xwpe.
Ce sont des versions diff�rentes du m�me �diteur et environnement de
d�veloppement. Si vous avez d�j� utilis� les environnements de programmation
de Micro$oft Windows et que vous recherchiez un �quivalent sous X, vous
l'avez trouv� ! Il y a aussi les �quivalents en mode texte des programmes X,
ce qui vous permet d'utiliser xwpe quel que soit votre environnement de
d�veloppement.

Ce paquetage contient les biblioth�ques xwpe de base et les programmes en
mode texte ; les programmes X Window se trouvent dans le paquetage xwpe-X11

%description -l tr X11
X Window alt�nda �al��an t�mle�ik geli�tirme ortam� yaz�l�mlar�.

%description -l tr
XWPE, Micro$oft Windows'da bulunan benzerleri gibi, bir metin d�zenleyici ve
t�mle�ik bir geli�tirme ortam� sunan bir yaz�l�md�r. Bu pakettekiler metin
ekranda �al��an s�r�mleri bulundurmaktad�r.

%prep
%setup -q

%build
./configure --prefix=/usr
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

make prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT/usr/bin
  strip we wpe xwe xwpe
)

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#install -m644 -o root -g root $RPM_SOURCE_DIR/xwpe.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xwpe



tar xvfpz $RPM_SOURCE_DIR/xwpe-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGELOG
/usr/bin/we
/usr/bin/wpe
/usr/lib/xwpe
/usr/man/man1/wpe.1
/usr/man/man1/we.1

%files X11
%defattr(-,root,root)
/usr/man/man1/xwpe.1
/usr/man/man1/xwe.1
/usr/bin/xwe
/usr/bin/xwpe
/etc/X11/wmconfig/xwpe

%changelog
* Fri Jun 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 1.5.12a to 1.5.18a

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Thu Nov 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- wmconfig included

* Mon Oct 12 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.12a.

* Thu Aug 20 1998 Jeff Johnson <jbj!redhat.com>
- update to 1.5.11a.

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.10a.

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.5.9a.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source and patch urls
- added URL tag

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

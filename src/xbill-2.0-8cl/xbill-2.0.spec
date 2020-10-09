Summary: Kill Bill as he tries to put Windows in computers.
Summary(pt_BR): Mate Bill quando ele estiver tentando colocar Windows nos computadores.
Summary(es): Mata Bill cuando est� intentando poner Windows en los ordenadores.
Name: xbill
Version: 2.0
Release: 8cl
Copyright: MIT
Group: Amusements/Games
Group(pt_BR): Passatempos/Jogos
Group(es): Pasatiempos/Juegos
Source: ftp://ftp.x.org/contrib/games/xbill-2.0.tgz
Source800: xbill-wmconfig.i18n.tgz
Patch0: xbill-2.0-rh.patch
Icon: xbill.gif
BuildRoot: /var/tmp/xbill-root
Summary(de): Haltet Bill davon ab, jeden Computer in die Windows-Zwangsjacke zu stecken! 
Summary(fr): Tuez Bill lorsqu'il essaie de mettre Windows dans les ordinateurs
Summary(tr): Bilgisayarlara Windows yerle�tirmeye �al��an Bill'i �ld�rme oyunu

%description
This package has seen increased popularity with the dawn of the Linux age.
Very popular at Red Hat.

The object of the game?  To seek out and destroy all forms of Bill, 
to disestablish new and alien operating systems, and to boldly go where 
no geek has gone before.

%description -l pt_BR
Este pacote vem crescendo de popularidade com o passar dos anos
do Linux. Ele � muito popular na Red Hat e na Conectiva tamb�m!.
O objetivo do jogo? Achar e destruir todas as formas de Bill que
tenta desestabilizar novos e antigos sistemas operacionais, e para
corajosamente chegar onde nenhum homem jamais chegou antes.

%description -l es
Este paquete viene creciendo de popularidad con el pasar de los
anos de Linux. Es muy popular en Red Hat y �en Conectiva tambi�n!.
�Cu�l es el objetivo del juego? Encontrar y destruir todas las
f�rmulas de Bill para intenta desestabilizar nuevos y antiguos
sistemas operativos, y para con coraje llegar donde ning�n hombre
jam�s ha llegado.

%description -l de
Sinn des Spiels? Alle Inkarnationen von Bill zu finden und zu vernichten,
neue und fremdartige Betriebssysteme zu eliminieren und wagemutig neue
Territorien zu beschreiten, die noch niemand betreten hat 

%description -l fr
Ce paquetage a vu sa popularit� augmenter depuis l'aube de l'�re Linux. 
Il est tr�s populaire chez Red Hat.

Le but du jeu ? Trouver et d�truire toutes les incarnations de Bill, pour
s�parer les syst�mes d'exploitation nouveaux et �trangers et aller hardiment
l� o� personne n'a �t� avant.

%description -l tr
Bu paket, Linux �a��n�n ba�lamas�yla b�y�k pop�larite kazand�. Red Hat'de
�ok seviliyor. Amac� ne mi? Bill'in her t�r�n� bulmak ve yok etmek.

%prep
%setup -q
%patch -p1 -b .rh

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./usr/lib/xbill
  for i in bitmaps pixmaps
  do
    mv ./var/lib/games/xbill/$i ./usr/lib/xbill/$i
    ln -s ../../../../usr/lib/xbill/$i ./var/lib/games/xbill/$i
  done

  mkdir -p ./etc/X11/wmconfig
#cat > ./etc/X11/wmconfig/xbill <<EOF
#xbill name "xbill"
#xbill description "Salve o mundo"
#xbill group Jogos/V�deo
#xbill exec "xbill &"
#EOF
)



tar xvfpz $RPM_SOURCE_DIR/xbill-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(2755,root,games)	/usr/X11R6/bin/xbill
%attr(0775,root,games)	%dir /var/lib/games/xbill
%attr(0664,root,games)	%config /var/lib/games/xbill/scores
/var/lib/games/xbill/bitmaps
/var/lib/games/xbill/pixmaps
/usr/lib/xbill
%config /etc/X11/wmconfig/xbill

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

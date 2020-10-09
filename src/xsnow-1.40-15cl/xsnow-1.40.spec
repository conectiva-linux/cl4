Summary: Xsnow will spread Christmas cheer on your X display
Summary(pt_BR): Para aqueles que desejam o Natal 12 meses por ano
Summary(es): Para aquellos que desean una Navidad, los 12 meses del a�o
Name: xsnow
Version: 1.40
Release: 15cl
Copyright: MIT
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gr�ficos
Group(es): Pasatiempos/Gr�ficos
Source0: ftp://ftp.x.org/contrib/games/xsnow-1.40.tar.Z
Source1: xsnow.wmconfig
Source800: xsnow-wmconfig.i18n.tgz
BuildRoot: /var/tmp/xsnow-root
Summary(de): Xsnow bringt Weihnachtsstimmung auf Ihren X-Bildschirm
Summary(fr): Xsnow va projeter l'esprit de noel sur votre �cran X.
Summary(tr): X ekran�na kar ya�d�r�r

%description
A continual gentle snowfall is accompanied by Santa Claus flying his
sleigh around your screen. Don't forget to shake the snow off those
windows every now and then!

%description -l pt_BR
Neve caindo continuamente acompanhada pelo v�o do Papai Noel pela
sua tela. N�o se esque�a de chacoalhar as janelas de vez em quando
para tirar a neve!

%description -l es
Nieve cayendo continuamente acompa�ada por el vuelo de Papa Noel
por tu pantalla. �Y no te olvides sacudir las ventanas, de vez en
cuando, para quitar la nieve!

%description -l de
Umgeben von sanftem Schneegest�ber fliegt Sankt Nikolaus in seinem 
Schlitten auf Ihrem Bildschirm umher. Vergessen Sie nicht, den Schnee 
gelegentlich von den Fenstern zu wischen! 

%description -l fr
Une douce chute de neige continue s'accompage du p�re No�l conduisant son
traineau � travers votre �cran. N'oubliez pas de secouer la neige de ces
fen�tres de temps en temps !

%description -l tr
Noel Baba'n�n geyikleriyle birlikte karlar alt�nda u�u�unu seyretmek
isterseniz xsnow kurun. Arada bir pencerelerin yerlerini de�i�tirip karlar�
da��tmay� unutmay�n.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man



tar xvfpz $RPM_SOURCE_DIR/xsnow-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xsnow
/usr/X11R6/man/man1/xsnow.1x
%config /etc/X11/wmconfig/xsnow

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

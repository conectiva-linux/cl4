Summary: Marc's favorite clock
Summary(pt_BR): Relógio favorito do Marc (seja lá quem for!)
Summary(es): Reloj favorito del Marc (¡Y da igual quien sea!)
Name: xdaliclock
Version: 2.10
Release: 7cl
Group: Amusements/Graphics
Group(pt_BR): Passatempos/Gráficos
Group(es): Pasatiempos/Gráficos
Copyright: MIT
Source: ftp://ftp.x.org/contrib/applications/xdaliclock-2.10.tar.gz
Source800: xdaliclock-wmconfig.i18n.tgz
BuildRoot: /var/tmp/xdaliclock-root
Summary(de): Marcs Lieblingsuhr
Summary(fr): Marc's favorite clock.
Summary(tr): Marc'ýn gözde saati

%description
The xdaliclock program displays a digital clock; when a digit changes, it
"melts" into its new shape.

It can display in 12 or 24 hour modes, and displays the date when a mouse
button is held down.  It has two large fonts built into it, but it can animate
other fonts.

%description -l pt_BR
O programa xdaliclock mostra um relógio digital; quando um dígito
muda, ele funde-se em sua nova forma. Ele pode funcionar em modo
de 12 ou 24 horas, e mostra a data quando o botão de mouse é
pressionado. Possui duas grandes fontes programadas dentro dele,
mas pode utilizar outras.

%description -l es
El programa xdaliclock enseña un reloj digital; cuando un dígito
cambia, fúndese en su nueva forma. Puede funcionar en modo de 12 ó
24 horas, y enseña la fecha cuando se presiona el botón de ratón
. Posee dos grandes fuentes programadas dentro de él, pero puede
utilizar otras.

%prep
%setup -q

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdaliclock <<EOF
#xdaliclock name "xdaliclock"
#xdaliclock description "Relógio favorito do Marc"
#xdaliclock group Passatempos
#xdaliclock exec "xdaliclock &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xdaliclock-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xdaliclock
/usr/X11R6/lib/X11/app-defaults/XDaliClock
/usr/X11R6/man/man1/xdaliclock.1x
%config /etc/X11/wmconfig/xdaliclock

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

Summary: X based gopher client
Summary(pt_BR): Cliente X para gopher
Summary(es): Cliente X para gopher
Name: xgopher
Version: 1.3.3
Release: 10cl
Copyright: distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
#Source: ftp.x.org:/contrib/applications/xgopher.1.3.3.tar.Z
# recompressed with bzip2
Source: ftp.x.org:/contrib/applications/xgopher.1.3.3.tar.bz2
Source800: xgopher-wmconfig.i18n.tgz
Patch: xgopher.1.3.3-config.patch
BuildRoot: /var/tmp/xgopher-root
Summary(de): X-orientierter Gopher-Client
Summary(fr): Client gopher sous X
Summary(tr): X tabanlý gopher istemcisi

%description
Gopher, a method of accessing information on the Internet, is made easy
with this X-Windows gopher client. Although gopher is less up-to-date than
the WWW, Xgopher can still open up a portal to the vast storehouse of
information available on the Internet.

%description -l pt_BR
Gopher, um método de acesso a informações na Internet, é facilitado
com este cliente X-Window. Apesar de que o gopher é menos atualizado
que o WWW, Xgopher ainda pode ser um portal para uma vasta fonte
de informação disponível na Internet.

%description -l es
Gopher, un método de acceso a información en la Internet, se
facilita con este cliente X-Window. A pesar de que gopher es menos
actualizado que WWW, Xgopher puede ser también, un portal para una
extensa fuente de información disponible en la Internet.

%description -l de
Gopher, ein Verfahren des Informationszugriffs im Internet, wird mit
diesem Gopher-Client für X-Windows zum Kinderspiel. Obwohl Gopher
nicht so aktuell wie das WWW ist, stellt Xgopher trotzdem ein Tor 
zu den im Internet gespeicherten Informationen dar.

%description -l tr
gopher, Ýnternet üzerindeki bilgilere ulaþmanýn en eski yöntemlerinden
biridir. xgopher yardýmýyla son derece geniþ bilgi bankalarýna grafik
arabirimi yardýmýyla rahatlýkla baðlanabileceksiniz.

%prep
%setup -q -n xgopher.1.3
%patch -p0

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install install.man

#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xgopher <<EOF
#xgopher name "xgopher"
#xgopher description "Cliente Gopher"
#xgopher group Rede
#xgopher exec "xgopher &"
#EOF



tar xvfpz $RPM_SOURCE_DIR/xgopher-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xgopher
/usr/X11R6/lib/X11/xgopher/xgopher.help
%config /usr/X11R6/lib/X11/app-defaults/Xgopher
%config /usr/X11R6/lib/X11/app-defaults/Xgopher-color
/usr/X11R6/man/man1/xgopher.1x
%config /etc/X11/wmconfig/xgopher

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

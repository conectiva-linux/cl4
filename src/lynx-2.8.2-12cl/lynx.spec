Summary: Text based browser for the world wide web
Summary(pt_BR): Navegador web modo texto
Summary(es): Navegador web modo texto
Name: lynx
Version: 2.8.2
Release: 12cl
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source0: ftp://www.slcc.edu/pub/lynx/curren/lynx2.8.2rel.1.tar.bz2
Source1: lynx.wmconfig
Source800: lynx-wmconfig.i18n.tgz
Patch0: lynx-2-8-2-cnc.patch
Patch2: lynx2-8-2.ssl.patch
Patch3: lynx-2.8.2-imgover.patch
Patch4: lynx-2-8-1-openssl.patch
Patch5: lynx2-8-2-brokenssl.patch
Serial: 1
Requires: indexhtml
%define VER 2-8-2
Buildroot: /var/tmp/lynx-root
Summary(de): Text-Browser für das WWW 
Summary(fr): Navigateur en mode texte pour le world wide web
Summary(tr): Metin ekranda WWW tarayýcý

%description
This a terminal based WWW browser. While it does not make any attempt
at displaying graphics, it has good support for HTML text formatting,
forms, and tables.

%description -l pt_BR
Este é um browser WWW para terminal em modo texto. Enquanto ele não
faz nenhuma tentativa para mostrar gráficos, possui um bom suporte
para o formato de texto HTML, formulários e tabelas.

%description -l es
Este es un browser WWW para terminal en modo texto. Mientras no hace
ningún intento de enseñar gráficos, posee un buen soporte para el
formato de texto HTML, formularios y tablas.

%prep
%setup -n lynx%{VER}
%patch0 -p1 -b .redhat
%patch2 -p1 -b .ssl
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=/etc \
	--with-screen=slang --enable-warnings \
	--enable-default-colors --enable-externs \
	--enable-internal-links --enable-nsl-fork --with-zlib 
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m644 -o root -g root $RPM_SOURCE_DIR/lynx.wmconfig \
	$RPM_BUILD_ROOT/etc/X11/wmconfig/lynx
strip $RPM_BUILD_ROOT/usr/bin/lynx








tar xvfpz $RPM_SOURCE_DIR/lynx-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc docs README INSTALLATION samples
%doc test lynx.hlp lynx_help
%config(missingok) /etc/X11/wmconfig/lynx
/usr/bin/lynx
/usr/man/man1/lynx.1
%config /etc/lynx.cfg

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  1 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr  9 1999 Marcelo Tosatti <marcelo@conectiva.com> 
- updated SSLeay library init function with OpenSSL one

* Sun Mar 28 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig
- added Group, Summary and %description translations

* Mon Mar 22 1999 Marcelo Tosatti <marcelo@conectiva.com> 
- fixed buffer overflow with <img width> tag.

* Sat Oct 31 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 2.8.1 final
- included ssl support

* Wed Oct 28 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- 2.8.1pre11

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig translated to pt_BR

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- 2.8.1pre9
- strip binaries

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- updated to lynx2.8.1pre.7.tar.gz

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 2.8rel3
- fixed mailto: buffer overflow (used Alan's patch)

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.8
- added buildroot

* Tue Jan 13 1998 Erik Troan <ewt@redhat.com>
- updated to 2.7.2
- enabled lynxcgi

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from 2.6 to 2.7.1
- moved /usr/lib/lynx.cfg to /etc/lynx.cfg
- build with slang instead of ncurses
- made default startup file be file:/usr/doc/HTML/index.html

Summary: GNU Line Editor
Summary(pt_BR): Editor de linhas da GNU
Summary(es): Editor de líneas de la GNU
Name: ed
Version: 0.2
Release: 14cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
#Source: ftp://prep.ai.mit.edu/pub/gnu/ed-0.2.tar.gz
# recompactado com bzip2
Source: ftp://prep.ai.mit.edu/pub/gnu/ed-0.2.tar.bz2
Prereq: /sbin/install-info
Buildroot: /var/tmp/ed-root
Summary(de): GNU-Zeileneditor 
Summary(fr): Éditeur ligne de GNU
Summary(tr): GNU satýr düzenleyici

%description
This is the GNU line editor.  It is an implementation of one
of the first editors under *nix.  Some programs rely on it,
but in general you probably don't *need* it.

%description -l pt_BR
Este é o GNU editor de linha. É uma implementação de um dos primeiros
editores para *nix. Alguns programas contam com ele, mas no geral
você provavelmente não irá *precisar* dele.

%description -l es
Este es GNU editor de línea. Es un soporte a uno de los primeros
editores para *nix. Algunos de los programas cuentan con él, pero
de manera general, es muy probable que no lo *necesites*.

%description -l de
Dies ist der GNU-Zeileneditor, eine Implementierung einer
der ersten Editoren unter *nix. Manche Programme verlassen sich darauf,
i.a. *brauchen* Sie ihn wahrscheinlich nicht.

%description -l fr
Éditeur ligne de GNU. C'est une implantation de l'un des premiers
éditeurs d'*nix. Certains programmes en ont besoin, mais en
général, vous n'en aurez probablement pas l'utilité.

%description -l tr
Bu paket UN*X'in en eski metin düzenleyicilerinden birini içermektedir. Bazý
yazýlýmlar hala bu programa gereksinim duymaktadýrlar.

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Dec 09 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- final rebuild for 3.0
- acertos no %preun (o ] estava "colado" no 0 -> 0] )

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>

- added install-info support
- added BuildRoot
- correct URL in Source line

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>

- built against glibc

%prep
%setup

%build
./configure --prefix=/usr --exec-prefix=/
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s prefix=$RPM_BUILD_ROOT/usr \
     exec_prefix=$RPM_BUILD_ROOT install
gzip -fn $RPM_BUILD_ROOT/usr/info/ed.info

strip $RPM_BUILD_ROOT/bin/ed

%post
/sbin/install-info /usr/info/ed.info.gz /usr/info/dir --entry="* ed: (ed).                  The GNU Line Editor."

%preun
if [ $1 = 0 ]; then
/sbin/install-info --delete /usr/info/ed.info.gz /usr/info/dir --entry="* ed: (ed).                  The GNU Line Editor."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NEWS POSIX README THANKS
/bin/ed
/bin/red
/usr/info/ed.info.gz
/usr/man/man1/ed.1
/usr/man/man1/red.1

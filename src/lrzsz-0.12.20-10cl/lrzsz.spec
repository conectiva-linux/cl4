Summary: The lrz and lsz modem communications programs.
Summary(pt_BR): Lzrz - sz, rz, e amigos
Summary(es): Lzrz - sz, rz, y amigos
Name: lrzsz
Version: 0.12.20
Release: 10cl
Copyright: GPL
Group: Applications/Communications
Group(pt_BR): Aplicações/Comunicação
Group(es): Aplicaciones/Comunicaciones
Source: http://www.nrw.net/uwe/archive/lrzsz-0.12.20.tar.gz
Patch1: lrzsz-0.12.20-glibc21.patch
BuildRoot: /var/tmp/lrzsz-root

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of the
rzsz package.  Lrzsz was created to provide a working GNU copylefted
Zmodem solution for Linux systems.  

You should install lrzsz if you're also installing a Zmodem communications
program that uses lrzsz.  If you're installing minicom, you need to install
lrzsz.

%description -l pt_BR
Esta coleção de comandos podem ser usados para baixar e atualizar
arquivos usando os protocolos Z, X e Y. Muitos programas de terminal
(como o minicom) usam estes programas para transferir arquivos.

%description -l es
Esta colección de comandos se pueden usar para bajar y actualizar
archivos usando los protocolos Z, X y Y. Muchos programas de terminal
(como el minicom) usan estos programas para transferir archivos.

%prep
%setup -q
%patch1 -p1 -b .glibc21

%build
[ "$LINGUAS" ] && unset LINGUAS
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s \
	./configure --disable-pubdir \
		--enable-syslog \
		--prefix=/usr \
		--program-transform-name=s/l//
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/sz
/usr/bin/sb
/usr/bin/sx
/usr/bin/rz
/usr/bin/rb
/usr/bin/rx
/usr/man/man1/sz.1
/usr/man/man1/rz.1
/usr/share/locale/*/LC_MESSAGES/*

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 0.12.20, i18n translations included.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Dec 18 1998 Preston Brown <pbrown@redhat.com>
- bumped spec number for initial rh 6.0 build

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups 

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- Upgraded to 0.12.14 and changed makefiles so gettext isnt built.

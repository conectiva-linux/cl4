Summary: An X Window System based news reader.
Summary(pt_BR): Leitor de news baseado em X
Summary(es): Lector de news basado en X
Name: xrn
Version: 9.01
Release: 4cl
Copyright: Distributable
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Source: ftp://ftp.x.org/contrib/applications/xrn/xrn-9.01.tgz
Source800: xrn-wmconfig.i18n.tgz
Patch0: xrn-rh.patch
Patch1: xrn-glibc.patch 
BuildRoot: /var/tmp/xrn-root

%description
A simple Usenet News reader for the X Window System.  Xrn allows you to
point and click your way through reading, replying and posting news
messages.

Install the xrn package if you need a simple news reader for X.

%description -l pt_BR
Este é um programa do X Window para leitura de news. Ele permite
leitura do tipo "apontar e clicar", respostas e postagem, assim
como seleções simples de grupo.

%description -l es
Este es un programa del X Window para lectura de news. Permite
lectura del tipo "apuntar y cliquear", respuestas y postagem,
así como selecciones sencillas de grupo.

%prep
%setup -q -c
%patch0 -p1 -b .config
%patch1 -p1 -b .glibc

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make DESTDIR=$RPM_BUILD_ROOT install

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xrn <<EOF
xrn name "xrn"
xrn description "X News Reader"
xrn group Utilities/News
xrn exec "xrn &"
EOF


tar xvfpz $RPM_SOURCE_DIR/xrn-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xrn
%config /usr/X11R6/lib/X11/app-defaults/XRn
%config /etc/X11/wmconfig/xrn

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- add wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

Summary: X interface to the gdb debugger
Summary(pt_BR): Interface X para o depurador gdb
Summary(es): Interface X para el depurador gdb
Name: xxgdb
Version: 1.12
Release: 11cl
Copyright: MIT
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
#Source: http://metalab.unc.edu/pub/Linux/devel/debuggers/xxgdb-1.12.tar.gz
# recompressed with bzip2
Source: http://metalab.unc.edu/pub/Linux/devel/debuggers/xxgdb-1.12.tar.bz2
Source1: xxgdb.wmconfig
Source800: xxgdb-wmconfig.i18n.tgz
Patch: xxgdb-1.08-glibc.patch
Patch1: xxgdb-1.12-sysv.patch
Patch2: xxgdb-1.12-compat21.patch
Icon: xxgdb.gif
Summary(de): X-Schnittstelle für den gdb-Debugger
Summary(fr): Interface X au déboggueur gdb.
Summary(tr): gdb hata ayýklayýcýsý için X arayüzü
BuildRoot: /var/tmp/xxgdb-root

%description
xxgdb is a graphical interface to GNU's debugger. It has the ability
to display source files as they are executed, set breakpoints, and
singlestep through or over commands - all with an easy-to-use
graphical X Windows interface.

%description -l pt_BR
xxgdb é uma interface gráfica para o debugger da GNU. Ele tem a
habilidade de mostrar arquivos fonte enquanto eles são executados,
configura "breakpoints", e passo a passo através dos comandos -
tudo com uma interface gráfica X Window muito simples de se usar.

%description -l es
xxgdb es una interface gráfica para el debugger de GNU. Tiene
la habilidad de enseñar archivos fuente mientras se ejecutan, y
configurar "breakpoints", paso a paso, a través de los comandos -
todo con una interface gráfica X Window muy sencilla de usar.

%description -l de
xxgdb ist eine grafische Oberfläche zum GNU-Debugger. Es kann
Quelldateien bei der Ausführung anzeigen, Breakpoints setzen und
in Einzelschritten Befehle durchlaufen - alles mit einer intuitiven
grafischen X-Windows-Oberfläche.

%description -l tr
xxgdb, GNU hata ayýklayýcýsý için bir arayüzdür. Çalýþma anýnda kaynak
kodunu gösterebilir ve çalýþmayý belirli yerlerde durdurabilirsiniz.

%prep
%setup -q -n xxgdb-1.12
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
  #install -m 644 $RPM_SOURCE_DIR/xxgdb.wmconfig ./etc/X11/wmconfig/xxgdb
)


tar xvfpz $RPM_SOURCE_DIR/xxgdb-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xxgdb
%config /usr/X11R6/lib/X11/app-defaults/XDbx
/usr/X11R6/man/man1/xxgdb.1x
/etc/X11/wmconfig/xxgdb

%changelog
* Fri Jun 11 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added Patch to make xxgdb compatible with glibc 2.1

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Wed Jul 29 1998 Jeff Johnson <jbj@redhat.com>
- change wmconfig group to utilities
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Feb  9 1998 Otto Hammersmith <otto@redhat.com>
- fixed wmconfig entry

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed src url
- added wmconfig entries
- removed prefix line ... can't have it with wmconfig file :(

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

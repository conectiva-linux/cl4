Summary: Viewer for various animated graphic formats
Summary(pt_BR): Visualizador para vários formatos de gráficos animados
Summary(es): Visor para varios formatos gráficos animados, incluyendo QuickTime y FLiC.
Name: xanim
Version: 28010
Release: 1cl
Copyright: MIT
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
#Source: ftp://xanim.va.pubnix.com/xanim2801.tar.gz
# Era gzip
Source: xanim2801.tar.bz2
Patch0: xanim-mod-path.patch
Prefix: /usr
BuildRoot: /var/tmp/xanim-root
Summary(de): Viewer für diverse animierte Grafikformate 
Summary(fr): Visualisateur de divers formats graphiques animés
Summary(tr): Deðiþik animasyon grafik dosyalarý için gösterici

%description
Viewer for various animated graphic formats, including QuickTime and FLiC.

This version supports dynamically loadable libraries, so adding new
codecs doesn't require a recompilation anymore. You can find new codecs
at the Xanim homepage: http://xanim.va.pubnix.com.

New codecs should be put in /usr/lib/xanim/. Please note this
package does not have any aditional codecs.

%description -l pt_BR
Visualizador para vários formatos gráficos animados, incluindo
QuickTime e FLiC.

Esta versão suporta que codecs sejam instalados dinamicamente, portanto
não é necessária a recompilação do xanim, para instalá-los. Você pode
encontrar vários codecs na página do xanim: http://xanim.va.pubnix.com.

Codecs novos devem ser colocados em /usr/lib/xanim.

%description -l es
Visor para varios formatos gráficos animados, incluyendo QuickTime
y FLiC.


Viewer for various animated graphic formats, including QuickTime and FLiC.

This version supports dynamically loadable libraries, so adding new
codecs doesn't require a recompilation anymore. You can find new codecs
at the Xanim homepage: http://xanim.va.pubnix.com.

New codecs should be put in /usr/lib/xanim/. Please note this
package does not have any aditional codecs.

%description -l de
Viewer für diverse animierte Grafikformate, einschließlich QuickTime und FliC.

%description -l fr
Visualiseur pour différents formats graphiques animés, dont Quicktime
et FLiC.

%description -l tr
QuickTime, FLiC dahil pek çok animasyon dosyasýný gösterir. /dev/dsp aygýtý
kuruluysa sesli gösterim de yapabilir.

%prep
%setup -q -n xanim2801
%patch -p1

%build
export PATH=/usr/X11R6/bin:$PATH
xmkmf
make INCDIR=/usr/X11R6/include/X11

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install 
cp docs/xanim.man .
make DESTDIR=$RPM_BUILD_ROOT install.man

#mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
#cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xanim <<EOF
#xboard name "xanim"
#xboard description "Visualizador de Animações"
#xboard group Aplicações/Gráficos
#xboard exec "xanim &"
#EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
mkdir -p /usr/lib/xanim/mods

%files
%doc docs/*
%defattr(-,root,root)
/usr/X11R6/bin/xanim
/usr/X11R6/man/man1/xanim.1x
#/etc/X11/wmconfig/xanim

%changelog
* Wed Jun 16 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 3 1999 Guilherme Manika <gwm@conectiva.com>
- xanim 2801

* Thu Mar 25 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- removed wmconfig (don't start w/o file on the cmd line)

* Thu Mar 25 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Nov 30 1998 Conectiva <dist@conectiva.com>
- correção wmconfig

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- updated package

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

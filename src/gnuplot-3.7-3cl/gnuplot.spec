Summary: A program for plotting mathematical expressions and data.
Summary(pt_BR): Pacote para traçar gráficos
Summary(es): Paquete para trazar gráficos
Name: gnuplot
Version: 3.7
Release: 3cl
Copyright: GPL
Group: Applications/Engineering
Group(pt_BR): Aplicações/Engenharia
Group(es): Aplicaciones/Ingeniería
# was .gz
Source: ftp://cmpc1.phys.soton.ac.uk/pub/gnuplot-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
URL: http://www.nas.nasa.gov/~woo/gnuplot/beta/

%description
Gnuplot is a command-line driven, interactive function plotting program
especially suited for scientific data representation.  Gnuplot can be
used to plot functions and data points in both two and three dimensions
and in many different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

%description -l pt_BR
Este é o pacote GNU de plotagem. Pode ser usado para gerar gráficos
em X Window ou para arquivo.

%description -l es
Este es el paquete GNU de ploteado. Se puede usar para crear gráficos
en X Window o para archivo.

%prep
%setup -q

%build
./configure --prefix=/usr --with-gnu-readline --with-png

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/gnuplot,man/man1}

install -m 755 -s gnuplot_x11 $RPM_BUILD_ROOT/usr/bin/gnuplot_x11
install -m 755 -s gnuplot $RPM_BUILD_ROOT/usr/bin/gnuplot
install -m 644 docs/gnuplot.1 $RPM_BUILD_ROOT/usr/man/man1
install -m 644 docs/gnuplot.gih $RPM_BUILD_ROOT/usr/share/gnuplot.gih

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/gnuplot_x11
/usr/bin/gnuplot
/usr/man/man1/gnuplot.1
/usr/share/gnuplot.gih

%changelog
* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.7.

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.6beta347

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

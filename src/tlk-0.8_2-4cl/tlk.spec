Summary: The Linux Kernel
Summary(pt_BR): O Kernel do Linux, livro do LDP
Summary(es): Kernel del Linux, libro del LDP
Name: tlk
Version: 0.8_2
Release: 4cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source: http://sunsite.unc.edu/LDP/tlk-0.8-2.html.tar.gz
Source800: wmconfig.i18n.tgz
Copyright: distributable
Buildroot: /var/tmp/tlk
BuildArchitectures: noarch

%description
The kernel is at the heart of the operating system. This book is a guide to how
the kernel fits together, how it works; a tour of the kernel.

%description -l pt_BR
O kernel é o coração de um sistema operacional. Este livro é um guia sobre
as partes internas do kernel, como elas funcionam. Um passeio pelo kernel.

%description -l es
kernel es el corazón de un sistema operativo. Este libro es un guía
sobre las partes internas del kernel, y como funcionan. Un paseo
por el kernel.

%changelog
* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- created the package

%prep
%setup -n tlk-0.8-2.html

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/tlk
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/tlk
cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/tlk
find $RPM_BUILD_ROOT/usr/doc/LDP -type f | xargs chmod 644
find $RPM_BUILD_ROOT/usr/doc/LDP -type d | xargs chmod 755

tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/tlk
/etc/X11/wmconfig/tlk

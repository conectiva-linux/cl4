Summary: LDP Getting Started Guide
Summary(pt_BR): LDP Guia de Instalação 
Summary(es): LDP Guía de Instalación 
Name: install-guide
Version: 3.2
Release: 4cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Source: ftp://sunsite.unc.edu/pub/Linux/docs/LDP/install-guide/install-guide-3.2.html.tar.bz2
Copyright: distributable
BuildRoot: /var/tmp/install-guide-root
BuildArchitectures: noarch

%description
A general guide for installing and getting started with Linux.  The
installation sections should be ignored, in favor of the Red Hat
Linux manual.  Although, there is overlap, there is other useful 
information in this guide.

%description -l pt_BR
Um guia geral para instalar e começar o uso do Linux. As seções sobre
instalação devem ser ignoradas, em favor do manual do Conectiva Linux.
Apesar desta sobreposição, há outras informações úteis neste guia.

%description -l es
Un guía general para instalar y empezar el uso del Linux. Las
secciones sobre instalación deben ser ignoradas, en favor del
manual del Conectiva Linux.  A pesar de esta superposición, hay
más información útil en este guía.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 3.2

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package

%prep 
%setup -n install-guide-3.2.html

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/install-guide
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/install-guide
cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/install-guide
find $RPM_BUILD_ROOT/usr/doc/LDP -type f | xargs chmod 644
find $RPM_BUILD_ROOT/usr/doc/LDP -type d | xargs chmod 755

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/install-guide

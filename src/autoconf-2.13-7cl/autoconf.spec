Summary: A GNU tool for automatically configuring source code.
Summary(pt_BR): GNU autoconf - ferramentas de configuração de fontes
Summary(es): GNU autoconf - herramientas de configuración de fuentes
Name: autoconf
Version: 2.13
Release: 7cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: ftp://prep.ai.mit.edu/pub/gnu/autoconf/autoconf-%{version}.tar.bz2
Patch0: autoconf-2.12-race.patch
Patch1: autoconf-2.13-mawk.patch
Patch2: autoconf-2.13-notmp.patch
Prereq: info
Requires: gawk, m4, mktemp, perl
BuildRoot: /var/tmp/%{name}-root
BuildArchitectures: noarch

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to 
specify various configuration options.

You should install Autoconf if you are developing software and you'd
like to use it to create shell scripts which will configure your 
source code packages. If you are installing Autoconf, you will also
need to install the GNU m4 package.

Note that the Autoconf package is not required for the end user who
may be configuring software with an Autoconf-generated script; 
Autoconf is only required for the generation of the scripts, not
their use.

%description -l pt_BR
GNU "autoconf" é uma ferramenta para configuração de fontes e
Makefiles. Ele ajuda o programador na criação de pacotes portáveis
e configuráveis, permitindo que a pessoa que programa o pacote
especifique várias opções de configuração. Autoconf é necessário
somente para gerar scripts de configuração.

%description -l es
GNU "autoconf" es una herramienta para configuración de fuentes y
Makefiles. Ayuda el programador en la creación de paquetes portátiles
y configurables, y permite que el programador del paquete especifique
varias opciones de configuración. Autoconf es necesario solamente
para crear scripts de configuración.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/info

make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT/usr/info/autoconf.info*

# We don't want to include the standards.info stuff in the package,
# because it comes from binutils...
rm -f $RPM_BUILD_ROOT/usr/info/standards*
cp install-sh $RPM_BUILD_ROOT/usr/share/autoconf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/autoconf.info.gz /usr/info/dir

%preun
/sbin/install-info --del /usr/info/autoconf.info.gz /usr/info/dir

%files
/usr/info/autoconf.info*
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add patch to help autoconf clean after itself and not leave /tmp clobbered
  with acin.* and acout.* files (can you say annoying?)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)
- use gawk, not mawk

* Thu Mar 18 1999 Preston Brown <pbrown@redhat.com>
- moved /usr/lib/autoconf to /usr/share/autoconf (with automake)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.13.

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires perl

* Thu Aug 27 1998 Cristian Gafton <gafton@redhat.com>
- patch for fixing /tmp race conditions

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups
- made a noarch package
- uses autoconf
- uses install-info

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built with glibc


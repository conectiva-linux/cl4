Summary: The Perl programming language.
Summary(pt_BR): Linguagem prática de extração e relatório
Summary(es): Lenguaje práctica de extracción y listado
Name: perl

%define perlver 5.005
%define perlrel 03
#Version: %{perlver}%{perlrel}
Version: 5.00503
Release: 3cl
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: ftp://ftp.perl.org/pub/perl/CPAN/src/perl%{perlver}_%{perlrel}.tar.bz2
Patch0: perl5.005_02-buildsys.patch
Patch1: perl5-installman.patch
Patch2: perl5.005_03-db1.patch
Requires: csh
Buildroot: /var/tmp/perl-root

%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications (and what it excels
at) are probably system administration utilities and web programming.
A large proportion of the CGI scripts on the web are written in Perl.
You need the perl package installed on your system so that your
system can handle Perl scripts.

%description -l pt_BR
Perl é uma linguagem interpretada, otimizada para tratar arquivos
texto, extraindo informação desses arquivos e mostrando relatórios
baseados nessa informação. Também é uma boa linguagem para várias
tarefas de administração de sistema. A linguagem procura ser
mais prática (fácil de usar, eficiente, completa) do que bonita
(minúscula, elegante, mínima).

%description -l es
Perl es un lenguaje interpretado, optimizado para manejar archivos
texto, extrayendo información de estos archivos y mostrando
listados basados en esta información. También es un buen lenguaje
para varias tareas de administración de sistema. El lenguaje busca
ser más práctico (fácil de usar, eficiente, completo) que bonito
(minúsculo, elegante, mínimo).

%package doc
Summary: Documentation for the Perl programming language.
Summary(pt_BR): Documentação para a linguagem de programação Perl.
Summary(es): Documentación sobre Perl.
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación

%description doc
This package contains documentation on the Perl programming language,
as an extra set of man pages and pod files (Perl plain documentation).

%description -l pt_BR doc
Este pacote contém documentação para a linguagem Perl,
na forma de um conjunto extra de páginas de manual e arquivos pod 
(Perl plain documentation)

%description -l es doc
Este paquete contiene la documentación del lenguaje Perl
, como un conjunto extra de páginas de manual y archivos pod
(Perl plain documentation).

%prep
%setup -q -n perl%{perlver}_%{perlrel}
%patch0 -p1
%patch1 -p1
# Perl does not have a single entry point to define what db library to use
# so the patch below is mostly broken...
#%patch2 -p1
find . -name \*.orig -exec rm -fv {} \;

%build
# this is gross
cat > config.over <<EOF
installprefix=$RPM_BUILD_ROOT/usr
test -d \$installprefix || mkdir \$installprefix
test -d \$installprefix/bin || mkdir \$installprefix/bin
installarchlib=\`echo \$installarchlib | sed "s!\$prefix!\$installprefix!"\`
installbin=\`echo \$installbin | sed "s!\$prefix!\$installprefix!"\`
installman1dir=\`echo \$installman1dir | sed "s!\$prefix!\$installprefix!"\`
installman3dir=\`echo \$installman3dir | sed "s!\$prefix!\$installprefix!"\`
installprivlib=\`echo \$installprivlib | sed "s!\$prefix!\$installprefix!"\`
installscript=\`echo \$installscript | sed "s!\$prefix!\$installprefix!"\`
installsitelib=\`echo \$installsitelib | sed "s!\$prefix!\$installprefix!"\`
installsitearch=\`echo \$installsitearch | sed "s!\$prefix!\$installprefix!"\`
EOF

sh Configure -des -Dprefix=/usr -Darchname=${RPM_ARCH}-linux -Dd_dosuid \
	-Ud_setresuid -Ud_setresgid -Dd_semctl_semun \
	-Dman3dir=/usr/lib/perl5/man/man3 -Doptimize="$RPM_OPT_FLAGS"

make

# Strip binaries (done now rather than at install)
strip perl
strip suidperl
strip x2p/a2p

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install
install -m 755 utils/pl2pm $RPM_BUILD_ROOT/usr/bin/pl2pm

# Generate *.ph files with a trick. Is this sick or what ?
make all -f - <<EOF
PKGS	= glibc-devel gdbm-devel gpm-devel libgr-devel libjpeg-devel \
	  libpng-devel libtiff-devel ncurses-devel popt \
	  zlib-devel binutils libelf e2fsprogs-devel pam pwdb \
	  rpm-devel
STDH	= \$(filter /usr/include/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' \$(PKGS)))
STDH	+=\$(wildcard /usr/include/linux/*.h) \$(wildcard /usr/include/asm/*.h) \
	  \$(wildcard /usr/include/scsi/*.h)
GCCDIR	= \$(shell gcc --print-file-name include)
GCCH	= \$(filter \$(GCCDIR)/%%, \$(shell rpm -q --queryformat '[%%{FILENAMES}\n]' egcs))

PERLLIB = \$(RPM_BUILD_ROOT)/usr/lib/perl5/%{perlver}%{perlrel}
PERL	= PERL5LIB=\$(PERLLIB) \$(RPM_BUILD_ROOT)/usr/bin/perl
PHDIR	= \$(PERLLIB)/\${RPM_ARCH}-linux
H2PH	= \$(PERL) \$(RPM_BUILD_ROOT)/usr/bin/h2ph -d \$(PHDIR)/

all: std-headers gcc-headers fix-config

std-headers: \$(STDH)
	cd /usr/include && \$(H2PH) \$(STDH:/usr/include/%%=%%)

gcc-headers: \$(GCCH)
	cd \$(GCCDIR) && \$(H2PH) \$(GCCH:\$(GCCDIR)/%%=%%)

fix-config: \$(PHDIR)/Config.pm
	\$(PERL) -i -p -e "s|\$(RPM_BUILD_ROOT)||g;" \$<

EOF

gzip -9f $RPM_BUILD_ROOT/usr/man/man1/*
gzip -9f $RPM_BUILD_ROOT/usr/lib/perl5/man/man3/*
gzip -9f $RPM_BUILD_ROOT/usr/lib/perl5/5.00503/pod/*

find $RPM_BUILD_ROOT/usr/lib/perl5/ -type d \
      ! -regex "$RPM_BUILD_ROOT/usr/lib/perl5/5.00503/pod" \
      ! -regex "$RPM_BUILD_ROOT/usr/lib/perl5/man/man3" \
     | sed  -e "s:$RPM_BUILD_ROOT:%dir :" > libperl.files

find $RPM_BUILD_ROOT/usr/lib/perl5/ -type f \
      ! -regex "$RPM_BUILD_ROOT/usr/lib/perl5/5.00503/pod/.*" \
      ! -regex "$RPM_BUILD_ROOT/usr/lib/perl5/man/man3/.*" \
     | sed  -e "s:$RPM_BUILD_ROOT::" >> libperl.files

%clean
rm -rf $RPM_BUILD_ROOT

%files -f libperl.files
%defattr(-,root,root)
/usr/bin/*
/usr/man/man1/*

%files doc
%docdir /usr/lib/perl5/man
%docdir /usr/lib/perl5/5.00503/pod
%doc /usr/lib/perl5/man
%doc /usr/lib/perl5/5.00503/pod

%changelog
* Fri Jun 25 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included optimize option
- created doc package (with extra man pages and pod files)
- compressed all doc files

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- recompressed sources

* Tue Apr 06 1999 Cristian Gafton <gafton@redhat.com>
- version 5.00503
- make the default man3 install dir be release independent
- try to link against db1 to preserve compatibility with older databases;
  abandoned idea because perl is too broken to allow such an easy change
  (hardcoded names *everywhere* !!!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- guilty of the inlined Makefile in the spec file
- adapted for the arm build

* Wed Sep 09 1998 Preston Brown <pbrown@redhat.com>
- added newer CGI.pm to the build
- changed the version naming scheme around to work with RPM

* Sun Jul 19 1998 Jeff Johnson <jbj@redhat.com>
- attempt to generate *.ph files reproducibly

* Mon Jun 15 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.004_04-m4 (pre-5.005 maintenance release)

* Tue Jun 12 1998 Christopher McCrory <chrismcc@netus.com
- need stdarg.h from gcc shadow to fix "use Sys::Syslog" (problem #635)

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to correct the .ph constructs unless defined (foo) to read
  unless(defined(foo))

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Mar 10 1998 Cristian Gafton <gafton@redhat.com>
- fixed strftime problem

* Sun Mar 08 1998 Cristian Gafton <gafton@redhat.com>
- added a patch to fix a security race
- do not use setres[ug]id - those are not implemented on 2.0.3x kernels

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 5.004_04 - 5.004_01 had some nasty memory leaks.
- fixed the spec file to be version-independent

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- Config.pm wasn't right do to the builtrooting

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- fixed arch-specfic part of spec file

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to perl 5.004_01
- users a build root

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- Incorporated security patch from Chip Salzenberg <salzench@nielsenmedia.com>

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
- Use -Darchname=i386-linux 
- Require csh (for glob)
- Use RPM_ARCH during configuration and installation for arch independence

Summary: A GNU collection of diff utilities.
Summary(pt_BR): Utilitários diff da GNU
Summary(es): Utilitarios diff de la GNU
Name: diffutils
Version: 2.7
Release: 17cl
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
Source: ftp://prep.ai.mit.edu/pub/gnu/diffutils-2.7.tar.gz
Source1: cmp.1
Source2: diff.1
Source3: diff3.1
Source4: sdiff.1
Copyright: GPL
Prefix: %{_prefix}
Prereq: info
Buildroot: /var/tmp/%{name}-root

%description
Diffutils includes four utilities:  diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line.  The cmp
command shows the offset and line numbers where two files differ, or cmp
can show the characters that differ between the two files.  The diff3
command shows the differences between three files.  Diff3 can be used when
two people have made independent changes to a common original; diff3 can
produce a merged file that contains both persons' changes and warnings
about conflicts.  The sdiff command can be used to merge two files
interactively.

Install diffutils if you need to compare text files.

%description -l pt_BR
Os utilitários diff podem ser usados para comparar arquivos,
e gerar uma gravação das "diferenças" entre eles. Essa gravação
pode ser usada pelo programa patch para atualizar um arquivo com o
outro. Todos estes utilitários (exceto cmp) trabalham somente com
arquivos texto.

%description -l es
Los utilitarios diff pueden ser usados para comparar archivos, y
crear una grabación de las "diferencias" entre ellos. Esta grabación
puede ser usada por el programa patch para actualización entre dos
archivos. Todos estos utilitarios (excepto cmp) trabajan solamente
con archivos texto.

%prep
%setup -q

%build
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/%{_prefix} 

%configure
make PR_PROGRAM=%{_prefix}/bin/pr

%install
rm -rf $RPM_BUILD_ROOT

make prefix=${RPM_BUILD_ROOT}%{_prefix} install

( cd $RPM_BUILD_ROOT
  gzip -9nf .%{_prefix}/info/diff*
  strip .%{_prefix}/bin/* || :
  mkdir -p .%{_prefix}/man/man1
  for manpage in %{SOURCE1} %{SOURCE3} %{SOURCE4}
  do
    install -m 0644 ${manpage} .%{_prefix}/man/man1
  done
)

%post
/sbin/install-info %{_prefix}/info/diff.info.gz %{_prefix}/info/dir --entry="* diff: (diff).                 The GNU diff."

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_prefix}/info/diff.info.gz %{_prefix}/info/dir --entry="* diff: (diff).                 The GNU diff."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NEWS README
%{_prefix}/bin/*
%{_prefix}/man/man*/*
%{_prefix}/info/diff.info*gz

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Jeff Johnson <jbj@redhat.com>
- man pages not in %files.
- but avoid conflict for diff.1

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 14)

* Sun Mar 14 1999 Jeff Johnson <jbj@redhat.com>
- add man pages (#831).
- add %configure and Prefix.

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Jul 14 1998 Bill Kawakami <billk@home.com>
- included the four man pages stolen from Slackware

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun May 03 1998 Cristian Gafton <gafton@redhat.com>
- fixed spec file to reference/use the $RPM_BUILD_ROOT always

* Wed Dec 31 1997 Otto Hammersmith <otto@redhat.com>
- fixed where it looks for 'pr' (/usr/bin, rather than /bin)

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

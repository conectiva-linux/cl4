Summary: The GNU Bourne Again shell (bash).
Summary(pt_BR): GNU Bourne Again shell (bash)
Summary(es): GNU Bourne Again shell (bash).
Name: bash2
Version: 2.03
Release: 6cl
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Copyright: GPL
Source0: ftp://ftp.gnu.org/pub/gnu/bash-%{version}.tar.gz
Source1: bashrc
Source2: ftp://ftp.gnu.org/pub/gnu/bash-doc-%{version}.tar.gz
Patch0: bash-2.03-paths.patch
Patch1: bash-2.02-security.patch
Patch2: bash-2.02.1-arm.patch
Patch3: bash-2.03-profile.patch
Patch4: bash-2.03-bash2.patch
Patch5: bash-2.03-builtins-man.patch
Prefix: %{_prefix}
BuildRoot: /var/tmp/%{name}-root

%description
Bash is a GNU project sh-compatible shell or command language
interpreter. Bash (Bourne Again shell) incorporates useful features
from the Korn shell (ksh) and the C shell (csh). Most sh scripts
can be run by bash without modification.

Bash offers several improvements over sh, including command line
editing, unlimited size command history, job control, shell
functions and aliases, indexed arrays of unlimited size and 
integer arithmetic in any base from two to 64. Bash is ultimately
intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 Shell and
Tools standard.

%description -l pt_BR
Bash é um interpretador de comandos compatível com sh, que executa
comandos lidos da entrada padrão ou de um arquivo. Bash também
incorpora características úteis das shells Korn e C (ksh e csh).
Bash tem sido desenvolvido para ser uma implementação compatível
com a especificação IEEE Posix para shells e ferramentas (IEEE
Working Group 1003.2).

%description -l es
Bash es un interpretador de comandos compatible con sh, que ejecuta
comandos leídos de la entrada padrón o de un archivo. Bash también
incorpora características útiles de las shells Korn y C (ksh y csh).
Bash ha sido desarrollado para ser una adición compatible con la
especificación IEEE Posix para shells y herramientas (IEEE Working
Group 1003.2).

%package doc
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
Summary: Documentation for the GNU Bourne Again shell (bash).
Summary(pt_BR): Documentação para o GNU Bourne Again shell (bash).
Summary(es): Documentación para el GNU Bourne Again shell (bash)

%description doc
This is a separate documentation package for the GNU Bourne
Again shell.

%description -l pt_BR doc
Este é um pacote separado para a documentação do GNU Bourne
Again Shell.

%description -l es doc
Documentación para el GNU Bourne Again Shell.

%prep
%setup -q -n bash-%{version} -a 2
%patch0 -p1 -b .paths
%patch1 -p1 -b .security
%patch2 -p1 -b .arm
%patch3 -p1 -b .profile
%patch4 -p1 -b .bash2
%patch5 -p1 -b .builtins-man
echo %{version} > _distribution
echo 0 > _patchlevel

%build
#CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
#    ./configure --prefix=$RPM_BUILD_ROOT/usr $RPM_ARCH-conectiva-linux

%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=${RPM_BUILD_ROOT}%{_prefix} install

# make manpages for bash builtins as per suggestion in DOC/README
cd doc
sed -e '
/^\.SH NAME/, /\\- bash built-in commands, see \\fBbash\\fR(1)$/{
/^\.SH NAME/d
s/^bash, //
s/\\- bash built-in commands, see \\fBbash\\fR(1)$//
s/,//g
b
}
d
' builtins.1 > man.pages
install -m 644 builtins.1 ${RPM_BUILD_ROOT}%{_prefix}/man/man1/builtins2.1

for i in `cat man.pages` ; do
  echo .so man1/builtins2.1 > ${RPM_BUILD_ROOT}%{_prefix}/man/man1/$i.1
done

# now turn man.pages into a filelist for the man subpackage
cat man.pages |tr -s ' ' '\n' |sed '
1i\
%defattr(0644,root,man,0755)
s:^:%{_prefix}/man/man1/:
s/$/.1/
' > ../man.pages

{ cd $RPM_BUILD_ROOT
  mkdir ./bin
  mv .%{_prefix}/bin/bash ./bin/bash2
  mv .%{_prefix}/bin/bashbug .%{_prefix}/bin/bash2bug
  mv .%{_prefix}/info/bash.info .%{_prefix}/info/bash2.info
  mv .%{_prefix}/man/man1/bashbug.1 .%{_prefix}/man/man1/bash2bug.1
  mv .%{_prefix}/man/man1/bash.1 .%{_prefix}/man/man1/bash2.1
  strip ./bin/* || :
  gzip -9nf .%{_prefix}/info/bash2.info
  rm -f .%{_prefix}/info/dir
}

%clean
rm -rf $RPM_BUILD_ROOT

# ***** bash doesn't use install-info. It's always listed in /usr/info/dir
# to prevent prereq loops

%post
if [ ! -f /etc/shells ]; then
        echo "/bin/bash2" > /etc/shells
else
        if ! grep '^/bin/bash2$' /etc/shells > /dev/null; then
                echo "/bin/bash2" >> /etc/shells
        fi
fi

%postun
if [ "$1" = 0 ]; then
        grep -v '^/bin/bash2' < /etc/shells > /etc/shells.new
        mv /etc/shells.new /etc/shells
fi

%files -f man.pages
%defattr(-,root,root)
%doc CHANGES COMPAT NEWS NOTES README CWRU/POSIX.NOTES
%doc doc/FAQ doc/INTRO doc/article.ms
%doc examples/bashdb/ examples/functions/ examples/misc/
%doc examples/scripts.noah/ examples/scripts.v2/ examples/scripts/
%doc examples/startup-files/
/bin/bash2
%{_prefix}/info/bash2.info.gz
%{_prefix}/man/man1/bash2.1
%{_prefix}/man/man1/builtins2.1
%{_prefix}/bin/bash2bug
%{_prefix}/man/man1/bash2bug.1

%files doc
%defattr(-,root,root)
%doc doc/*.ps doc/*.0 doc/*.html doc/article.txt

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Jun 18 1999 Wanderlei Cavassin <cavassin@conectiva.com>
- fix source bug in man page man1/builtins2.1

* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Removed a kludge added by the Red Hat guys
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- strip binaries.
- include bash-doc correctly.

* Thu Mar 18 1999 Preston Brown <pbrown@redhat.com>
- fixed post/postun /etc/shells work.

* Thu Mar 18 1999 Cristian Gafton <gafton@redhat.com>
- updated again text in the spec file

* Mon Feb 22 1999 Jeff Johnson <jbj@redhat.com>
- updated text in spec file.
- update to 2.03.

* Fri Feb 12 1999 Cristian Gafton <gafton@redhat.com>
- build it as bash2 instead of bash

* Tue Feb  9 1999 Bill Nottingham <notting@redhat.com>
- set 'NON_INTERACTIVE_LOGIN_SHELLS' so profile gets read

* Thu Jan 14 1999 Jeff Johnson <jbj@redhat.com>
- rename man pages in bash-doc to avoid packaging conflicts (#606).

* Wed Dec 02 1998 Cristian Gafton <gafton@redhat.com>
- patch for the arm
- use $RPM_ARCH-redhat-linux as the build target

* Tue Oct  6 1998 Bill Nottingham <notting@redhat.com>
- rewrite %pre, axe %postun (to avoid prereq loops)

* Wed Aug 19 1998 Jeff Johnson <jbj@redhat.com>
- resurrect for RH 6.0.

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.02.1

* Thu Jun 11 1998 Jeff Johnson <jbj@redhat.com>
- Package for 5.2.

* Mon Apr 20 1998 Ian Macdonald <ianmacd@xs4all.nl>
- added POSIX.NOTES doc file
- some extraneous doc files removed
- minor .spec file changes

* Sun Apr 19 1998 Ian Macdonald <ianmacd@xs4all.nl>
- upgraded to version 2.02
- Alpha, MIPS & Sparc patches removed due to lack of test platforms
- glibc & signal patches no longer required
- added documentation subpackage (doc)

* Fri Nov 07 1997 Donnie Barnes <djb@redhat.com>
- added signal handling patch from Dean Gaudet <dgaudet@arctic.org> that
  is based on a change made in bash 2.0.  Should fix some early exit
  problems with suspends and fg.

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- added %clean

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- added comment explaining why install-info isn't used
- added mips patch 

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- added BuildRoot

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

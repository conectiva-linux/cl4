Summary: A shell similar to ksh, but with improvements.
Summary(pt_BR): Shell bourne melhorada
Summary(es): Shell bourne mejorada
Name: zsh
Version: 3.0.5
Release: 12cl
Copyright: GPL

Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos

Source0: ftp://ftp.lysator.liu.se/pub/unix/zsh/zsh-3.0.5.tar.bz2
Source1: zlogin.rhs
Source2: zlogout.rhs
Source3: zprofile.rhs
Source4: zshrc.rhs
Source5: zshenv.rhs
Patch0: zsh-3.0.5-nsl.patch
Patch1: zsh-3.0.5-docfix.patch
Buildroot: /var/tmp/zsh-root
Prereq: fileutils grep /sbin/install-info

%description
The zsh shell is a command interpreter usable as an interactive login
shell and as a shell script command processor.  Zsh resembles the ksh
shell (the Korn shell), but includes many enhancements.  Zsh supports
command line editing, built-in spelling correction, programmable
command completion, shell functions (with autoloading), a history
mechanism and more.

%description -l pt_BR
zsh é uma versão melhorada do bourne shell com essas características:
- muito próximo da gramática do ksh/sh, com adições csh - várias
características do ksh, bash e tcsh - 75 funções embutidas, 89
opções, 154 combinações de teclas - seleção - funções shell ...e
muito mais

%description -l es
zsh es una versión mejorada del bourne shell con estas
características: - muy próximo de la gramática del ksh/sh, con
adiciones csh - varias características del ksh, bash y tcsh - 75
funciones empotradas, 89 opciones, 154 combinaciones de teclas -
selección - funciones shell ...y mucho más

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS"  ./configure --prefix=/usr --bindir=/bin --enable-etcdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/info $RPM_BUILD_ROOT/bin $RPM_BUILD_ROOT/etc

make prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/bin install
strip $RPM_BUILD_ROOT/bin/zsh
chmod 755 $RPM_BUILD_ROOT/bin/zsh
gzip -9nf $RPM_BUILD_ROOT/usr/info/zsh*
cp Etc/{BUGS,FAQ,CONTRIBUTORS,FEATURES,NEWS} .

for I in zshrc zlogin zlogout zshenv zprofile; do
	cp $RPM_SOURCE_DIR/${I}.rhs $RPM_BUILD_ROOT/etc/$I
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ] ; then
    echo "/bin/zsh" > /etc/shells
else
    echo "/bin/zsh" >> /etc/shells
fi

/sbin/install-info /usr/info/zsh.info.gz /usr/info/dir \
	--entry="* zsh: (zsh).			An enhanced bourne shell."

%preun
if [ "$1" = 0 ] ; then
    /sbin/install-info --delete /usr/info/zsh.info.gz /usr/info/dir \
	--entry="* zsh: (zsh).			An enhanced bourne shell."
fi

%postun
if [ -f /etc/shells ] ; then
    TmpFile=`/bin/mktemp /tmp/.zshrpmXXXXXX`
    grep -v '^/bin/zsh$' /etc/shells > $TmpFile
    cp -f TmpFile /etc/shells
    rm -f TmpFile
    chmod 644 /etc/shells
fi

%files
%defattr(-,root,root)
%doc META-FAQ README NEWS ChangeLog Etc Util Functions CONTRIBUTORS BUGS FAQ
%doc FEATURES
/bin/zsh
/usr/man/man1/zsh*.1
/usr/info/zsh*gz
%config /etc/*

%changelog
* Thu Jun 10 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 10)
- fix the texi source
- patch to detect & link against nsl

* Wed Mar 10 1999 Cristian Gafton <gafton@redhat.com>
- use mktemp to handle temporary files.

* Thu Feb 11 1999 Michael Maher <mike@redhat.com>
- fixed bug #365

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- compile for 5.2

* Sat Jun 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Sat Jun  6 1998 Jeff Johnson <jbj@redhat.com>
- Eliminate incorrect info page removal.

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build
- moved profile.d handling from zshrc to zprofile

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- Upgraded to 3.0.5
- Install-info handling

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Apr 10 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 3.0.2
- Added 'reasonable' default startup files in /etc

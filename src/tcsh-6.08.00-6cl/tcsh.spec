Summary: Enhanced C-Shell
Summary(pt_BR): C-shell melhorada
Summary(es): C-shell mejorada
Name: tcsh
Version: 6.08.00
Release: 6cl
Copyright: distributable
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
#Source: ftp://ftp.astron.com/pub/tcsh/tcsh-6.08.tar.gz
# recompactado com o bzip2
Source: ftp://ftp.astron.com/pub/tcsh/tcsh-6.08.tar.bz2
Patch0: tcsh-6.07.09-utmp.patch
Patch1: tcsh-6.07.09-termios.patch
Provides: csh
Prereq: fileutils grep
URL: http://www.primate.wisc.edu/software/csh-tcsh-book/
Buildroot: /var/tmp/tcsh-root
Summary(de): Erweiterte C-Shell
Summary(fr): Shell C amélioré.
Summary(tr): Geliþmiþ c-kabuðu (c-shell)

%description
'tcsh' is an enhanced version of csh (the C shell), with additional features
such as command history, filename completion, and fancier prompts.

%description -l pt_BR
"tcsh" é uma versão melhorada da csh (C shell), com características
adicionais como history dos comandos, complemento de nome de arquivo
e prompts.

%description -l es
"tcsh" es una versión mejorada de la csh (C shell), con
características adicionales como historia de los comandos,
complemento de nombre de archivo y prompts.

%description -l de
'tcsh' ist eine erweiterte Version von csh (der C-Shell) mit zusätzlichen
Funktionen wie Befehlsgeschichte, Dateinamenvervollständigung und
attraktiveren Prompts.

%description -l fr
'tcsh' est une version améliorée de csh (le shell C), avec des
fonctionnalités supplémentaires comme un historique des commandes,
la complétion des noms de fichiers, et des prompts sympas.

%description -l tr
tcsh, csh'in (C kabuðu) geliþkin bir sürümüdür ve komut tarihçesi, dosya adý
tamamlama ve þýk komut imleri gibi özellikler sunar.

%prep
%setup -q
%patch0 -p1 -b .getutent
%patch1 -p1 -b .termios

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=
make LIBES="-lnsl -ltermcap -lcrypt"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/man/man1 $RPM_BUILD_ROOT/bin
install -m 755 -s tcsh $RPM_BUILD_ROOT/bin/tcsh
install -m 644 tcsh.man $RPM_BUILD_ROOT/usr/man/man1/tcsh.1
ln -sf tcsh $RPM_BUILD_ROOT/bin/csh
nroff -me eight-bit.me > eight-bit.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/tcsh" > /etc/shells
	echo "/bin/csh" > /etc/shells
else
	grep '^/bin/tcsh$' /etc/shells > /dev/null || echo "/bin/tcsh" >> /etc/shells
	grep '^/bin/csh$' /etc/shells > /dev/null || echo "/bin/csh" >> /etc/shells
fi

%postun
if [ ! -x /bin/tcsh ]; then
	grep -v '^/bin/tcsh$' /etc/shells | grep -v '^/bin/csh$'> /etc/shells.rpm
	mv /etc/shells.rpmsave /etc/shells
fi

%files
%defattr(-,root,root)
%doc NewThings FAQ eight-bit.txt complete.tcsh Fixes Ported README WishList README.imake Y2K
/bin/tcsh
/bin/csh
/usr/man/man1/tcsh.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 20 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Nov 23 1998 Domingos Parra Novo <domingos@conectiva.com>
- updated to 6.08
- cleaned up the spec file
- fixed source url and ftp site
- patch de segurança não é mais necessário, já estava incluido na nova versão

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri Oct 02 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 6.07.09 from the freebsd
- security fix

* Wed Aug  5 1998 Jeff Johnson <jbj@redhat.com>
- use -ltermcap so that /bin/tcsh can be used in single user mode w/o /usr.
- update url's

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- updated to 6.07; added BuildRoot
- cleaned up the spec file; fixed source url

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- added termios hacks for new glibc
- added /bin/csh to file list

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Feb 07 1997 Erik Troan <ewt@redhat.com>
 - Provides csh, adds and removes /bin/csh from /etc/shells if csh package
   isn't installed.

Summary: A public domain clone of the Korn shell (ksh).
Summary(pt_BR): Shell Korn de domínio público
Summary(es): Shell Korn de dominio público
Name: pdksh
Version: 5.2.13
Release: 3cl
Copyright: Public Domain
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Source: ftp.cs.mun.ca:/pub/pdksh/pdksh-%{version}.tar.gz
Patch0: pdksh-5.2.13-compat21.patch
BuildRoot: /var/tmp/%{name}-root

%description
The pdksh package contains PD-ksh, a clone of the Korn shell (ksh).
The ksh shell is a command interpreter intended for both interactive
and shell script use.  Ksh's command language is a superset of the
sh shell language.

Install the pdksh package if you want to use a version of the ksh
shell.

%description -l pt_BR
Pdksh, uma reimplementação de ksh, é um interpretador de comandos
destinado tanto para uso interativo como em shell scripts. Sua
linguagem de comandos é um superconjunto da linguagem sh(1) shell.

%description -l es
Pdksh, una ampliación más de ksh, es un interpretador de comandos
destinado tanto al uso interactivo como en shell scripts. Su lenguaje
de comandos es un superconjunto del lenguaje sh(1) shell.

%prep
%setup -q
%patch0 -p1 -b .compat21

%build
#CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr

%configure
make LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{bin,usr/bin,usr/man/man1}

/usr/bin/install -s -c -m755 ksh $RPM_BUILD_ROOT/bin/ksh
/usr/bin/install -c -m644 ksh.1 $RPM_BUILD_ROOT/usr/man/man1/ksh.1
ln -sf /bin/ksh $RPM_BUILD_ROOT/usr/bin/ksh
ln -sf /bin/ksh $RPM_BUILD_ROOT/usr/bin/pdksh
ln -sf ksh.1 $RPM_BUILD_ROOT/usr/man/man1/pdksh.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/ksh" > /etc/shells
else
	if ! grep '^/bin/ksh$' /etc/shells > /dev/null; then
		echo "/bin/ksh" >> /etc/shells
	fi
fi

%postun
if [ ! -f /bin/ksh ]; then
	grep -v /bin/ksh /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%verifyscript

echo -n "Looking for ksh in /etc/shells... "
if ! grep '^/bin/ksh$' /etc/shells > /dev/null; then
    echo "missing"
    echo "ksh missing from /etc/shells" >&2
else
    echo "found"
fi

%files
%defattr(-,root,root)
%doc README NOTES PROJECTS NEWS BUG-REPORTS
/bin/ksh
/usr/bin/ksh
/usr/bin/pdksh
/usr/man/man1/ksh.1
/usr/man/man1/pdksh.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Jeff Johnson <jbj@redhat.com>
- glibc 2.1 doesn't init sys_siglist for 32 <= i < NSIG (#1473)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- upgrade to 5.2.13.

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

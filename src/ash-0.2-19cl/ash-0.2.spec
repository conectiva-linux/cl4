Summary: A smaller version of the Bourne shell.
Summary(pt_BR): Pequena shell bourne de Berkeley
Summary(es): Pequeña shell bourne de Berkeley
Name: ash
Version: 0.2
Release: 19cl
Copyright: BSD
Group: System Environment/Shells
Group(pt_BR): Ambiente do Sistema/Interpretadores de Comandos
Group(es): Ambiente del Sistema/Interpretadores de Comandos
Source: http://sunsite.unc.edu:/pub/Linux/system/shells/ash-linux-0.2.tar.bz2
Patch0: ftp://ftp.redhat.com/pub/ash-0.2-make.patch
Patch1: ash-linux-0.2-glibc21.patch
Prereq: fileutils grep
Buildroot: /var/tmp/ash-root
Conflicts: mkinitrd <= 1.7

%description
The ash shell is a clone of Berkeley's Bourne shell.  Ash
supports all of the standard sh shell commands, but is considerably
smaller than bash.  The ash shell lacks some features (for example,
command-line histories), but needs a lot less memory.

You should install ash if you need a lightweight shell with many of the
same capabilities as the bash shell.

%description -l pt_BR
ash é um clone do shell bourne de Berkeley. Ele suporta todos os
comandos-padrão da Bourne shell e tem a vantagem de suportá-los
com um tamanho consideravelmente menor do que bash.

%description -l es
ash es un clone del shell bourne de Berkeley. Soporta todos los
comandos padrón de la Bourne shell y tiene la ventaja de soportarlos
con un tamaño considerablemente menor del que bash.

%prep
%setup -q -n ash-linux-0.2
%patch0 -p1
%patch1 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 
strip sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1

install -m 755 sh $RPM_BUILD_ROOT/bin/ash
install -m 644 sh.1 $RPM_BUILD_ROOT/usr/man/man1/ash.1
ln -sf ash.1 $RPM_BUILD_ROOT/usr/man/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/bin/bsh

rm -f sh
make STATIC=-static

install -m 755 sh $RPM_BUILD_ROOT/bin/ash.static

%post
if [ ! -f /etc/shells ]; then
	echo "/bin/ash" > /etc/shells
	echo "/bin/bsh" >> /etc/shells
else
	if ! grep '^/bin/ash$' /etc/shells > /dev/null; then
		echo "/bin/ash" >> /etc/shells
	fi
	if ! grep '^/bin/bsh$' /etc/shells > /dev/null; then
		echo "/bin/bsh" >> /etc/shells
	fi
fi

%postun

if [ "$1" = 0 ]; then
	grep -v '^/bin/ash' < /etc/shells | grep -v '^/bin/bsh' > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%verifyscript

for n in ash bsh; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^/bin/${n}\$" /etc/shells > /dev/null; then
	echo "missing"
	echo "${n} missing from /etc/shells" >&2
    else
	echo "found"
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/bin/ash
/bin/ash.static
/bin/bsh
/usr/man/man1/ash.1
/usr/man/man1/bsh.1

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 17)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- build on glibc 2.1

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to correct path on SunSITE.

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made /bin/ash built shared
- added ash.static
- uses a buildroot and %attr

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- statically linked

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- fixed preinstall script to >> /etc/shells for bsh.

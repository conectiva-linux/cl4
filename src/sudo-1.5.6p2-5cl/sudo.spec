Summary: Allows command execution as root for specified users
Summary(pt_BR): Permite que usuários específicos executem comandos como se fossem o root
Summary(es): Permite que usuarios específicos ejecuten comandos como se fueran el root
Name: sudo
Version: 1.5.6p2
Release: 5cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
# was .Z
Source: ftp://ftp.cs.colorado.edu/pub/sudo/cu-sudo.v%{version}.tar.bz2
URL: http://www.courtesan.com/courtesan/products/sudo/
Patch0: sudo-1.5.4-config.patch
Patch1: sudo-1.5.4-path-vi.patch
BuildRoot: /tmp/%{name}-%{version}-root

%description
Sudo (superuser do) allows a system administrator to give certain users 
(or groups of users) the ability to run some (or all) commands as root while 
logging all commands and arguments. Sudo operates on a per-command basis, 
it is not a replacement for the shell. 

%description -l pt_BR
Sudo (superuser do) permite que o administrador do sistema dê a
certos usuários (ou grupos de usuários) a habilidade para rodar
alguns (ou todos) comandos como root, registrando todos os comandos e
argumentos. Sudo opera numa base por comando, não sendo um substituto
para a shell.

%description -l es
Sudo (superuser do) permite que el administrador del sistema
otorga a ciertos usuarios (o grupos de usuarios) la habilidad para
ejecutar algunos (o todos) comandos como root, registrando todos
los comandos y argumentos. Sudo opera en una base por comando,
no siendo un substituto para la shell.

%prep
%setup -q -n sudo.v%{version}
%patch0 -p1
%patch1 -p1

%build
./configure --prefix=/usr -sbindir=/usr/sbin --with-C2 --with-pam
make CFLAGS="$RPM_OPT_FLAGS -DALTERNATE_PATH_VI=\\\"/bin/vi\\\""

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	visudodir=$RPM_BUILD_ROOT/usr/sbin \
	sysconfdir=$RPM_BUILD_ROOT/etc \
#	install_uid=$USER \
#	install_gid=$GROUP

install -d $RPM_BUILD_ROOT/{etc/pam.d,var/{log,run/sudo}}
install sample.pam $RPM_BUILD_ROOT/etc/pam.d/sudo
touch $RPM_BUILD_ROOT/var/log/sudo.log
chmod -R +r $RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr  1 1999 Conectiva <dist@conectiva.com>
- alternate path to vi
- final rebuild for 3.0 spanish edition

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Sep 21 1998 Ian Macdonald <ianmacd@xs4all.nl>
- upgraded to 1.5.6p2
- built with PAM support
- removed SUDO_LDFLAGS="-static" from make: would no longer build with it

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot.

* Mon Apr 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.4-3]
- Buildroot changed to /tmp/sudo-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url and %setup macro,
- removed sudo-1.5.4-buildroot.patch and instead this added few parameters
  to "make install",
- SUDO_LDFLAGS="-static" and CFLAGS="$RPM_OPT_FLAGS" is passed as make 
  arguments,
- removed COPYING from %doc (Copyright statement is in Copyright field),
- removed from %doc *.pod and options.h and added sample.sudoers,
- added /var/log/sudo.log as %ghost file,
- added %verify(not md5) for /etc/sudoers (allow modify this file without
  display warning on verify with using rpm),
- added noreplace parameter for /etc/sudoers %config file,
- removed sudo.v1.5.4-glibc.diff because sudo compiles on glibc 2.0.7,
- added %defattr and %attr macros in %files (allows building package from
  non-root account); %defattr requires rpm >= 2.4.99.

* Fri Jan 23 1998 Ian Macdonald <ianmacd@xs4all.nl>
  [1.5.4-2]
- glibc build was broken; added patch to fix it

* Tue Nov 18 1997 Otto Hammersmith <otto@redhat.com>
- built for glibc, no problems

* Fri Apr 25 1997 Michael Fulbright <msf@redhat.com>
- Fixed for 4.2 PowerTools 
- Still need to be pamified
- Still need to move stmp file to /var/log

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- First version for PowerCD.

%files
%defattr(644, root, root, 700)
%doc BUGS CHANGES HISTORY OPTIONS README RUNSON TODO TROUBLESHOOTING
%doc sample.sudoers
%attr(400, root, root) %verify(not md5) %config(noreplace) /etc/sudoers
%config /etc/pam.d/sudo
%dir /var/run/sudo
%attr(4111, root, root) /usr/bin/sudo
%attr(0111, root, root) /usr/sbin/visudo
%attr(644, root,  man) /usr/man/man[58]/*
%attr(600, root, root) %ghost /var/log/sudo.log

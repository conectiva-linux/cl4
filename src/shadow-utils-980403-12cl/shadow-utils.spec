Summary: Utilities for managing shadow password files and user/group accounts.
Summary(pt_BR): Utilitários para o arquivo de senhas Shadow
Summary(es): Utilitarios para el archivo de contraseñas Shadow
Name: shadow-utils
%define version 980403
Version: %{version}
Release: 12cl
Source0: ftp://ftp.ists.pwr.wroc.pl/pub/linux/shadow/beta/shadow-%{version}.tar.gz
Source1: shadow-970616.login.defs
Source2: shadow-970616.useradd
Source700: shadow-utils-man-pt_BR.tar
Patch0: shadow-980403-redhat.patch
Patch1: shadow-980403-utmp.patch
Patch2: shadow-980403-newlt.patch
Patch3: shadow-980403-nscd.patch
Patch4: shadow-980403-pwlock.patch
Copyright: BSD
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Buildroot: /var/tmp/shadow-root
Obsoletes: adduser

%description
The shadow-utils package includes the necessary programs for
converting UNIX password files to the shadow password format, plus
programs for managing user and group accounts.  The pwconv command
converts passwords to the shadow password format.  The pwunconv command
unconverts shadow passwords and generates an npasswd file (a standard
UNIX password file).  The pwck command checks the integrity of
password and shadow files.  The lastlog command prints out the last
login times for all users.  The useradd, userdel and usermod commands
are used for managing user accounts.  The groupadd, groupdel and
groupmod commands are used for managing group accounts.

%description -l pt_BR
Este pacote inclui os programas necessários para converter
arquivos-padrão UNIX de senha para o formato shadow.  - 'pwconv5'
converte tudo para o formato de senhas do shadow.  - 'pwunconv'
desconverte senhas shadow, gerando um arquivo no diretório corrente
chamado npasswd que é o arquivo-padrão UNIX de senha.  - 'pwck'
checa a integridade da senha e dos arquivos shadow.  - 'lastlog'
mostra o último momento de login de todos os usuários.

Várias páginas de manual estão também incluídas sobre estes
utilitários e senhas shadow em geral.

%description -l es
Este paquete incluye los programas necesarios para convertir
Archivos padrón UNIX de contraseña al formato shadow.  - 'pwconv5'
convierte todo al formato de contraseñas del shadow.  - 'pwunconv'
deshace la conversión de contraseñas shadow, creando un archivo en
el directorio corriente llamado npasswd que es el archivo padrón UNIX
de contraseña.  - 'pwck' chequea la integridad de la contraseña y de
los archivos shadow.  - 'lastlog' enseña el último momento de login
de todos los usuarios.  Están también incluidas, en general, varias
páginas de manual sobre estos utilitarios y contraseñas shadow.

%prep
# This is just a few of the core utilities from the shadow suite...
# packaged up for use w/PAM
%setup -q -n shadow-%{version}
%patch0 -p1 -b .redhat
%patch1 -p1 -b .utmp
%patch2 -p1 -b .newlt
%patch3 -p1 -b .nscd
%patch4 -p1 -b .pwlock

%ifarch armv4l
libtoolize --copy --force
%endif
aclocal
automake
autoconf
autoheader

%build
rm -rf build-$RPM_ARCH ; mkdir build-$RPM_ARCH ; cd build-$RPM_ARCH
CFLAGS="$RPM_OPT_FLAGS" ../configure --prefix=/usr \
	--disable-desrpc --with-libcrypt --disable-shared
make 

%install
rm -rf $RPM_BUILD_ROOT
cd build-$RPM_ARCH
make install prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/default
  install -m 0600 $RPM_SOURCE_DIR/shadow-970616.useradd ./etc/default/useradd
  install -m 0644 $RPM_SOURCE_DIR/shadow-970616.login.defs ./etc/login.defs
  ln -s useradd ./usr/sbin/adduser
  ln -s useradd.8 ./usr/man/man8/adduser.8
  ln -s pwconv.8 ./usr/man/man8/pwunconv.8
  ln -s pwconv.8 ./usr/man/man8/grpconv.8
  ln -s pwconv.8 ./usr/man/man8/grpunconv.8
)


mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/shadow-utils-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf build-$RPM_ARCH

%files
%defattr(-,root,root)
%doc doc/ANNOUNCE doc/CHANGES doc/HOWTO
%doc doc/LICENSE doc/README doc/README.linux
%dir /etc/default
%attr(0644,root,root)	%config /etc/login.defs
%attr(0600,root,root)	%config /etc/default/useradd
/usr/sbin/adduser
/usr/sbin/user*
/usr/sbin/group*
/usr/sbin/grpck
/usr/sbin/pwck
/usr/sbin/*conv
/usr/sbin/chpasswd
/usr/sbin/newusers
/usr/sbin/mkpasswd
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/lastlog
/usr/bin/faillog
/usr/man/man1/chage.1
/usr/man/man1/gpasswd.1
/usr/man/man3/shadow.3
/usr/man/man5/shadow.5
/usr/man/man5/faillog.5
/usr/man/man8/adduser.8
/usr/man/man8/group*.8
/usr/man/man8/user*.8
/usr/man/man8/pwck.8
/usr/man/man8/grpck.8
/usr/man/man8/chpasswd.8
/usr/man/man8/newusers.8
/usr/man/man8/mkpasswd.8
/usr/man/man8/*conv.8
/usr/man/man8/lastlog.8
/usr/man/man8/faillog.8
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- SIGHUP nscd from usermod, too

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added usermod password locking from Chris Adams <cadams@ro.com>

* Thu Apr 08 1999 Bill Nottingham <notting@redhat.com>
- have things that modify users/groups SIGHUP nscd on exit

* Wed Mar 31 1999 Michael K. Johnson <johnsonm@redhat.com>
- have userdel remove user private groups when it is safe to do so
- allow -f to force user removal even when user appears busy in utmp

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- edit out unused CHFN fields from login.defs.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Wed Jan 13 1999 Bill Nottingham <notting@redhat.com>
- configure fix for arm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build against glibc 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- Note that /usr/sbin/mkpasswd conflicts with /usr/bin/mkpasswd;
  one of these (I think /usr/sbin/mkpasswd but other opinions are valid)
  should probably be renamed.  In any case, mkpasswd.8 from this package
  needs to be installed. (problem #823)

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 980403
- redid the patches

* Tue Dec 30 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file
- updated the patch so that new accounts created on shadowed system won't
  confuse pam_pwdb anymore ('!!' default password instead on '!')
- fixed a bug that made useradd -G segfault
- the check for the ut_user is now patched into configure

* Thu Nov 13 1997 Erik Troan <ewt@redhat.com>
- added patch for XOPEN oddities in glibc headers
- check for ut_user before checking for ut_name -- this works around some
  confusion on glibc 2.1 due to the utmpx header not defining the ut_name
  compatibility stuff. I used a gross sed hack here because I couldn't make
  automake work properly on the sparc (this could be a glibc 2.0.99 problem
  though). The utuser patch works fine, but I don't apply it.
- sleep after running autoconf

* Thu Nov 06 1997 Cristian Gafton <gafton@redhat.com>
- added forgot lastlog command to the spec file

* Mon Oct 26 1997 Cristian Gafton <gafton@redhat.com>
- obsoletes adduser

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- modified groupadd; updated the patch

* Fri Sep 12 1997 Cristian Gafton <gafton@redhat.com>
- updated to 970616
- changed useradd to meet RH specs
- fixed some bugs

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

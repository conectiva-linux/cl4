Summary: A free virtual machine for running Java(TM) code.
Summary(pt_BR): Máquina virtual free para rodar código Java(tm)
Summary(es): Máquina virtual free para ejecutar código Java(tm)
Name: kaffe
Version: 1.0.b4
Release: 3cl
Copyright: GPL
Url: http://www.kaffe.org/
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source0: ftp://ftp.transvirtual.com/pub/kaffe/kaffe-%{version}.tar.gz
Patch: kaffe-alpha.patch
Patch2: kaffe-perlpath.patch
Obsoletes: kaffe-bissawt
Buildroot: /var/tmp/kaffe-root

%description
Kaffe is a free virtual machine designed to execute Java(TM) bytecode.
Kaffe can be configured in two modes.  In the first mode, it operates as
a pure bytecode interpreter (not unlike Javasoft's machine).  In the
second mode, it performs "just-in-time" code conversion from the abstract
code to the host machine's native code.  The second mode will ultimately
allow execution of Java code at the same speed as standard compiled code,
while also maintaining the advantages and flexibility of code independence.

Install the kaffe package if you need a Java virtual machine.

%description -l pt_BR
Kaffe é uma máquina virtual projetada para executar bytecode Java.
Esta máquina pode ser configurada em dois modos. Em um modo ela opera
como um interpretador puro de bytecode (como a máquina da JavaSoft);
no segundo modo ela executa conversão de código "just-in-time"
do código abstrato para o código nativo de máquina. Isto permite a
execução de código Java na mesma velocidade que o código compilado,
com as vantagens da flexibilidade e independência de código.

%description -l es
Kaffe es una máquina virtual proyectada para ejecutar bytecode Java.
Esta máquina puede ser configurada en dos modos. En uno,  opera como
un interpretador puro de bytecode (como la máquina de la JavaSoft);
en el segundo modo, ejecuta conversión de código "just-in-time"
del código abstracto para el código nativo de máquina. Esto permite
la ejecución de código Java en la misma velocidad que el código
compilado, con las ventajas de la flexibilidad y independencia
de código.

%prep
%setup -q -n kaffe-1.0b4
%patch -p1 -b .alpha
%patch2 -p1
%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --libdir=/usr/lib/kaffe \
	--libexecdir=/usr/lib/kaffe
# hack hack hack
make || {
  cp -l kaffe/kaffevm/intrp/icode.h kaffe/kaffevm/jit
  make
 }

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	libexecdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	nativedir=$RPM_BUILD_ROOT/usr/lib/kaffe \
	classdir=$RPM_BUILD_ROOT/usr/share/kaffe install
#make prefix=$RPM_BUILD_ROOT/usr libdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	libexecdir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	nativedir=$RPM_BUILD_ROOT/usr/lib/kaffe \
#	classdir=$RPM_BUILD_ROOT/usr/share/kaffe check
strip $RPM_BUILD_ROOT/usr/bin/* || echo
strip $RPM_BUILD_ROOT/usr/lib/kaffe/Kaffe
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README FAQ license.terms developers
/usr/lib/kaffe
/usr/bin/*
/usr/man/*/*
/usr/share/kaffe
/usr/include/kaffe

%changelog
* Wed Jun 23 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- build for alpha (it seems to work...)
- fix paths so it works

* Mon Apr 12 1999 Preston Brown <pbrown@redhat.com>
- according to the kaffe people, b4 is a "massive bugfix release"

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Tue Dec 15 1998 Bill Nottingham <notting@redhat.com>
- add an Obsoletes: for kaffe-bissawt

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- update to 1.0b3
- include alpha patch, but it's still broke

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- added sparc to the list of supported architectures
- update to 1.0b2

* Tue Sep 22 1998 Bill Nottingham <notting@redhat.com>
- don't rename libraries; install them in /usr/lib/kaffe
- remove sparc arch (doesn't work)

* Thu Jul 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.0.b1.
- add sparc arch (alpha has problems kaffe/kaffeevm/support.c:{343,518}

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon May 04 1998 Cristian Gafton <gafton@redhat.com>
- finally their ftp site is up again: updated to 0.10.0
- too bad the Biss-AWT doesn't seem to be maintained anymore... Removed the
  bissawt package
- unfortunately alpha and sparc assembler code that reference registers
  like eax, ebx, etc. makes this package ExclusiveArch: i386

* Tue Dec 09 1997 Cristian Gafton <gafton@redhat.com>
- added kaffe to the file list
- added BuildRoot; cleaned the spec file

* Tue Nov 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- removed pieces with incompatible licenses

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- updated to 0.9.2

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Apr 24 1997 Erik Troan <ewt@redhat.com>
- added libkaffe_vm.so symlink.

* Tue Apr 22 1997 Erik Troan <ewt@redhat.com>
- added manual provide of libkaffe_vm.so (RPM seems a bit broken).

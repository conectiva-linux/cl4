Summary: The compatibility libraries needed by old libc.so.5 applications.
Summary(pt_BR): Biblioteca compartilhada padrão para programas
Summary(es): Biblioteca compartida padrón para programas
Name: libc
Version: 5.3.12
Release: 32cl
Exclusivearch: i386
Exclusiveos: Linux
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: libc-5.3.12-bins.tar.gz
Source1: libc-5.3.12-18.4.src.rpm
Prereq: ldconfig grep fileutils 
Requires: /lib/ld-linux.so.1
Autoreqprov: 0
Provides: libc.so.5 libstdc++.so.27 libg++.so.27 libm.so.5
Buildroot: /var/tmp/libc5-root/

%description
Older Linux systems (including all Red Hat Linux releases between 2.0
and 4.2, inclusive) were based on libc version 5. The libc package
includes the libc5 libraries and other libraries based on libc5.  With
these libraries installed, old applications which need them will be able
to run on your glibc (libc version 6) based system.

The libc package should be installed so that you can run older applications
which need libc version 5.

%description -l pt_BR
Contém as bibliotecas-padrão que são usadas por muitos programas
no sistema. Para salvar espaço em disco e memória, e para
facilitar atualizações, código comum no sistema é deixado em
um lugar e compartilhado entre os programas. Este pacote contém
os mais importantes conjuntos de bibliotecas compartilhadas, a
biblioteca-padrão C, e a biblioteca matemática-padrão. Sem este
pacote um sistema Linux não irá funcionar.

%description -l es
Contiene las bibliotecas padrón que usan muchos programas en el
sistema.  Para guardar espacio en disco y memoria, y para facilitar
actualizaciones, código común en el sistema se deja en un lugar
y se comparte entre los programas. Este paquete contiene los más
importantes conjuntos de bibliotecas compartidas, la biblioteca
padrón C, y la biblioteca matemática padrón. Sin este paquete un
sistema Linux no funcionará.

%prep
%setup -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/i486-linux-libc5/lib
for n in *; do
    install -m 755 $n $RPM_BUILD_ROOT/usr/i486-linux-libc5/lib
done

%post
if ! grep '^/usr/i486-linux-libc5/lib$' /etc/ld.so.conf > /dev/null 2>/dev/null; then
    echo "/usr/i486-linux-libc5/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
if [ "$1" = '0' ]; then
    grep -v '^/usr/i486-linux-libc5/lib$' /etc/ld.so.conf > /etc/ld.so.conf.new 2>/dev/null
    mv /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%files
/usr/i486-linux-libc5/lib

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- add old zlib and libdb to the mess

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 30)

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- rebuild for glibc 2.1

* Wed Nov 04 1998 Cristian Gafton <gafton@redhat.com>
- updated most libraries for security reasons

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- fixed postuninstall script

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Dec 23 1997 Cristian Gafton <gafton@redhat.com>
- updated for the vsyslog() security-fixed libc
- uses a BuildRoot

* Mon Nov 10 1997 Erik Troan <ewt@redhat.com>
- updated Xpm lib to one built w/ dependency info
- added svgalib

* Mon Sep 23 1997 Erik Troan <ewt@redhat.com>
- added ncurses libraries

* Mon Sep 08 1997 Erik Troan <ewt@redhat.com>
- updated X libraries to 3.1.1
- added provides of libm.so.5

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- initial build as compatibility package

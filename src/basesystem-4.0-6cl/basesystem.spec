Summary: The skeleton package which defines a simple Red Hat Linux system.
Summary(pt_BR): Pacote com o esqueleto de um sistema Red Hat simples
Summary(es): Paquete con el esqueleto de un sistema Red Hat simple
Name: basesystem
Version: 4.0
Release: 6cl
Serial: 1
Copyright: public domain
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
Prereq: setup filesystem
BuildRoot: /var/tmp/basesystem-root
BuildArchitectures: noarch

%description
Basesystem defines the components of a basic Conectiva Linux system (for
example, the package installation order to use during bootstrapping).
Basesystem should be the first package installed on a system, and it
should never be removed.

%description -l pt_BR
Apesar deste pacote não conter nenhum arquivo, ele executa uma
importante função. Ele define os componentes de um sistema Red
Hat básico, assim como a ordem de instalação dos pacotes durante
o boot inicial. Ele deve ser o primeiro pacote a ser instalado em
um sistema, e nunca deve ser removido.

%description -l es
A pesar de este paquete no contener ningún archivo, ejecuta una
importante función. Define los componentes de un sistema Red Hat
básico, así como el orden de instalación de los paquetes, mientras
se procesa el arranque inicial. Debe ser el primer paquete a ser
instalado en un sistema, y jamás debe ser quitado.

%files

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Jun 14 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- Serial = 1, Version = 4.0, in pair with the distro version

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- don't require rpm (breaks dependency chain)

* Tue Mar 16 1999 Erik Troan <ewt@redhat.com>
- require rpm

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

Summary: Shows runtime library call information for dynamically linked executables
Summary(pt_BR): Mostra informa��es sobre as chamadas � fun��es de bibliotecas em bin�rios dinamicamente ligados.
Summary(es): Ense�a informaci�n sobre las llamadas a funciones de bibliotecas en binarios din�micamente conectados.
Name: ltrace
Version: 0.3.4
Release: 5cl
Source: ftp://ftp.debian.org/debian/dists/unstable/main/source/utils/ltrace_0.3.4.tar.gz
Copyright: GPL
Group: Development/Debuggers
Group(pt_BR): Desenvolvimento/Depuradores
Group(es): Desarrollo/Depuradores
BuildRoot: /var/tmp/ltrace-root
ExclusiveArch: i386

%description
ltrace is a program that simply runs the specified command until it exits.
It intercepts and records the dynamic library calls which are called by
the executed process and the signals which are received by that process.
It can also intercept and print the system calls executed by the program.

%description -l pt_BR
ltrace � um programa que simplesmente executa um comando especificado at� seu
t�rmino. Ele intercepta e registra as chamadas � fun��es a bibliotecas
compartilhadas feitas pelo programa em execu��o e os sinais recebidos pelo
processo. Tamb�m pode interceptar e mostrar as chamadas ao sistema operacional
feitas pelo programa.

%description -l es
ltrace es un programa que sencillamente ejecuta un comando
especificado hasta su t�rmino. Intercepta y registra las llamadas, a
las funciones de las bibliotecas compartidas, hechas por el programa
en ejecuci�n, y los se�ales recibidos por el proceso. Tambi�n puede
interceptar y ense�ar las llamadas al sistema operativo hechas por
el programa.

%prep
%setup -q
./configure --prefix=/usr

%build
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README TODO BUGS
/usr/bin/ltrace
/usr/man/man1/ltrace.1
/etc/ltrace.conf

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Nov 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- rebuild for 3.0

* Mon Oct 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Mon Sep 21 1998 Preston Brown <pbrown@redhat.com>
- upgraded to 0.3.4

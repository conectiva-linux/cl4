Summary: Generates masks between two files and can use the mask to restore files
Summary(pt_BR): Gera e recupera arquivos mascarados
Summary(es): Genera y recupera archivos enmascarados
Name: rhmask
Version: 1.0
Release: 7cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp.redhat.com:/pub/redhat/code/rhmask/rhmask-1.0.tar.gz
BuildRoot: /var/tmp/rhmask-root

%description
rhmaskR is intended to allow the distribution of files as masks against
other files. This lets new versions of software be freely distributed on
public internet servers but limits their usefulness to those who already
have a copy of the package. It uses a simple XOR scheme for creating
the file mask and uses file size and md5 sums to ensure the integrity
of the result.

%description -l pt_BR
Rhmask tem o objetivo de permitir a distribui��o de arquivos como
m�scaras sobre outros arquivos. Isto permite que novas vers�es de
software sejam distribu�das gratuitamente em servidores p�blicos
internet, mas limita o seu uso completo para aqueles que j� possuem
uma c�pia do pacote. Ele usa um esquema simples XOR para criar
a m�scara do arquivo e usa o tamanho do arquivo e somas md5 para
assegurar a integridade do resultado.

%description -l es
Rhmask tiene el objetivo de permitir la distribuci�n de archivos como
m�scaras sobre otros archivos. Esto permite que nuevas versiones
de software sean distribuidas gratuitamente en servidores p�blicos
internet, pero limita su uso completo para aquellos que ya poseen
una copia del paquete. Usa un esquema sencillo XOR para crear la
m�scara del archivo y usa el tama�o del archivo y somas md5 para
asegurar la integridad del resultado.

%prep
%setup -q -n rhmask

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
strip $RPM_BUILD_ROOT/usr/bin/rhmask

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/man/man1/rhmask.1
/usr/bin/rhmask

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Oct 26 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

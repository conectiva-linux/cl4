Summary: A library for reading and returning lines from a terminal.
Summary(pt_BR): Biblioteca para leitura de linhas de um terminal
Summary(es): Biblioteca para lectura de líneas de un terminal
Name: readline
Version: 2.2.1
Release: 5cl
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://prep.ai.mit.edu/pub/gnu/readline-%{version}.tar.gz
Patch0: readline-2.2.1-shared.patch
Patch1: readline-2.2.1-guard.patch
Prereq: /sbin/install-info /sbin/ldconfig
Prefix: %{_prefix}
Buildroot: /var/tmp/readline-root

%description
The readline library reads a line from the terminal and returns it,
allowing the user to edit the line with standard emacs editing keys.
The readline library allows programmers to provide an easy to use and
more intuitive interface for users.

If you want to develop programs that will use the readline library,
you'll also need to install the readline-devel package.

%description -l pt_BR
A biblioteca "readline" lerá uma linha do terminal e irá retorná-la,
permitindo ao usuário editar a linha com as teclas de edição padrão
emacs. Ele permite ao programador dar ao usuário uma interface mais
fácil de usar e mais intuitiva.

%description -l es
La biblioteca "readline" leerá una línea del terminal y la
recuperará, permitiendo al usuario editar la línea con las teclas
de edición padrón emacs. Permite al programador dar al usuario una
interface más fácil de usar y más intuitiva.

%package devel
Summary: Development files for programs which will use the readline library.
Summary(pt_BR): Arquivo para desenvolver programas que utilizam a biblioteca para leitura de linhas
Summary(es): Archivo para desarrollar programas que utilicen la biblioteca para lectura de líneas
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: readline = %{PACKAGE_VERSION}

%description devel
The readline library will read a line from the terminal and return it.
Use of the readline library allows programmers to provide an easy
to use and more intuitive interface for users.

If you want to develop programs which will use the readline library,
you'll need to have the readline-devel package installed.  You'll also
need to have the readline package installed.

%description -l pt_BR devel
A biblioteca readline lerá uma linha do terminal e a retornará,
usando prompt como prompt. Se prompt é nulo, nenhum prompt é
mostrado. A linha retornada é alocada com malloc(3), devendo o
chamador liberá-la quando terminar. A linha retornada tem o salto
de linha final removido, desta forma somente o texto da linha
é disponibilizado.

%description -l es devel
La biblioteca readline leerá una línea del terminal y la recuperará,
usando prompt como prompt. Si prompt es nulo, ningún prompt se
enseña.  La línea recuperada es alocada con malloc(3), debiendo el
llamador liberarla cuando terminar. La línea recuperada tiene el
salto de línea final quitado, de esta forma solamente el texto de
la línea se pone a disposición.

%prep
%setup -q
%patch0 -p1 -b .shared
%patch1 -p1 -b .guard

%build
#./configure --prefix=/usr
%configure
make static shared

%install
rm -rf $RPM_BUILD_ROOT
make install install-shared prefix=$RPM_BUILD_ROOT/%{_prefix}

( cd $RPM_BUILD_ROOT
  ln -sf libreadline.so.3.0 ./%{_prefix}/lib/libreadline.so
  ln -sf libhistory.so.3.0 ./%{_prefix}/lib/libhistory.so
  gzip -9nf ./%{_prefix}/info/*info*
  rm ./%{_prefix}/info/dir
)
 
%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info /%{_prefix}/info/history.info.gz /%{_prefix}/info/dir
/sbin/install-info /%{_prefix}/info/readline.info.gz /%{_prefix}/info/dir

%postun -p /sbin/ldconfig

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /%{_prefix}/info/history.info.gz /%{_prefix}/info/dir
   /sbin/install-info --delete /%{_prefix}/info/readline.info.gz /%{_prefix}/info/dir
fi

%files
%defattr(-,root,root)
%{_prefix}/man/man*/*
%{_prefix}/info/*info*
%{_prefix}/lib/lib*.so.*

%files devel
%defattr(-,root,root)
%{_prefix}/include/readline
%{_prefix}/lib/lib*.a
%{_prefix}/lib/lib*.so

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri Apr 09 1999 Michael K. Johnson <johnsonm@redhat.com>
- added guard patch from Taneli Huuskonen <huuskone@cc.helsinki.fi>

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- updated to 2.2.1

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package /usr/info/dir

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- devel package moved to Development/Libraries

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.2

* Tue Oct 14 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- added proper sonames

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- updated to readline 2.1

* Tue Jun 03 1997 Erik Troan <ewt@redhat.com>
- built against glibc

Summary: Librarie for PhotoCD images
Summary(pt_BR): Biblioteca para imagens PhotoCD
Summary(es): Biblioteca para imágenes PhotoCD
Name: libpcd
Version: 0.2
Release: 4cl
Copyright: Distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: libpcd-0.2.tar.gz 

%description
Librarie for PhotoCD images

%description -l pt_BR
Biblioteca para imagens PhotoCD

%description -l es
Biblioteca para imágenes PhotoCD

%changelog
* Fri Jun  4 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Sep 17 1998 Marcelo Tosatti <marcelo@conectiva.com>
- Initial Package.

%prep
%setup -n libpcd
%build
./configure
make lib

%install
make install-lib 
%files
/usr/local/lib/libpcd.a
/usr/local/include/pcd.h

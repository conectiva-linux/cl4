Summary: Free TrueType font rasterizer library.
Summary(pt_BR): Biblioteca de renderização de fontes TrueType
Summary(es): Biblioteca de render 3D de fuentes TrueType
Name: freetype
Version: 1.2
Release: 8cl
Copyright: BSD-like
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
# was .gz
Source: freetype-%{version}.tar.bz2
Source1: ttmkfdir-1.0.tar.gz
Buildroot: /var/tmp/%{name}-root

%package devel
Summary: Header files and static library for development with FreeType.
Summary(pt_BR): Arquivos de inclusão e bibliotecas estáticas para desenvolvimento com FreeType.
Summary(es): Archivos de inclusión e bibliotecas estáticas para desarrollo con FreeType.
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description
The FreeType engine is a free and portable TrueType font rendering engine.
It has been developed to provide TT support to a great variety of
platforms and environments. Note that FreeType is a library, not a
stand-alone application, though some utility applications are included.

%description -l pt_BR
FreeType é uma máquina livre e portável para renderização de fontes
TrueType. Ela foi desenvolvida para fornecer suporte TrueType a 
uma grande variedade de plataformas e ambientes. Note que FreeType 
é uma biblioteca e não uma aplicação, apesar que alguns utilitários
são incluídos neste pacote.

%description -l es
FreeType es una máquina libre y portátil para en render de fuentes
TrueType. Fue desarrollada para ofrecer soporte TrueType a una gran
variedad de plataformas y ambientes. Observa que FreeType es una
biblioteca y no una aplicación, a pesar de que algunos utilitarios
se incluyan en este paquete.

%description devel
This package is only needed if you intend to develop or
compile applications which rely on the FreeType library.
If you simply want to run existing applications, you won't
need this package.

%description -l pt_BR devel
Este pacote é necessário se você pretende desenvolver/compilar aplicações
com a biblioteca FreeType. Se você simplesmente deseja rodar aplicações
existentes, você não precisa deste pacote. 

%description -l es devel
Este paquete es necesario, si pretendes desarrollar/compilar
aplicaciones con la biblioteca FreeType. Si, simplemente, deseas
ejecutar aplicaciones existentes, no lo necesitas.

%prep
%setup -q -a 1

%build

libtoolize --copy --force
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=/usr \
	--enable-static --enable-shared \
	--with-locale-dir=/usr/share/locale
make
make -C ttmkfdir-1.0

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install \
	gnulocaledir=$RPM_BUILD_ROOT/usr/share/locale
make -C ttmkfdir-1.0 install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/bin/*
/usr/sbin/*
/usr/lib/libttf.la
/usr/lib/libttf.so*
/usr/share/locale/*
%doc README HOWTO.txt docs

%files devel
/usr/include/*
/usr/lib/libttf.a

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 06 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added pt_BR translations
- Added optimization flags to spec file

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Mon Feb 15 1999 Preston Brown <pbrown@redhat.com>
- added ttmkfdir

* Tue Feb 02 1999 Preston Brown <pbrown@redhat.com>
- update to 1.2

* Thu Jan 07 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to sanitize config.sub and get ARM support
- dispoze of the patch (not necessary anymore)

* Wed Oct 21 1998 Preston Brown <pbrown@redhat.com>
- post/postun sections for ldconfig action.

* Tue Oct 20 1998 Preston Brown <pbrown@redhat.com>
- initial RPM, includes normal and development packages.

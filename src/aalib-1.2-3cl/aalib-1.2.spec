Summary: An ASCII art GFX library
Summary(pt_BR): Uma biblioteca para ASCII art
Summary(es): An ASCII art GFX library
Name: aalib
Version: 1.2
Release: 3cl
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: ftp://ftp.ta.jcu.cz/pub/aa/aalib-1.2.tar.gz

%description
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%description -l pt_BR
Uma biblioteca para trabalhar com ASCII art.

%description -l es
AA-lib is a low level gfx library just as many other libraries are.
The main difference is that AA-lib does not require graphics device. In
fact, there is no graphical output possible. AA-lib replaces those
old-fashioned output methods with powerful ascii-art renderer. Now my
linux boots with a nice penguin logo at secondary display (yes! Like
Win95 does:) AA-lib API is designed to be similar to other graphics
libraries. Learning a new API would be a piece of cake!

%package devel
Summary: headers and static libraries
Summary(pt_BR): Arquivos de inclusão e bibliotecas para a aalib
Summary(es): headers and static libraries
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas

%description devel
The header files and static libraries are only needed for development
of programs using the AAlib.

%description -l pt_BR devel
Bibliotecas e arquivos de inclusão para a aalib

%description -l es devel
The header files and static libraries are only needed for development
of programs using the AAlib.

%prep
%setup -q

%build

unset LINGUAS
export CFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
export LDFLAGS="-s"
./configure --prefix /usr
make

%install

make install
gzip -9 -f /usr/info/aalib.info


%post
/sbin/ldconfig
echo -n `install-info --info-dir=/usr/info /usr/info/aalib.info.gz 2>/dev/null` 2>/dev/null

%postun
/sbin/ldconfig

%preun
echo -n `install-info --delete --info-dir=/usr/info /usr/info/aalib.info.gz 2>/dev/null` 2>/dev/null

%files
%doc README NEWS COPYING AUTHORS ANNOUNCE
/usr/lib/libaa.so.1.0.3
/usr/info/aalib.info.gz
/usr/bin/aafire
/usr/bin/aainfo
/usr/bin/aasavefont
/usr/bin/aatest

%files devel
/usr/include/aalib.h
/usr/lib/libaa.a
/usr/lib/libaa.so

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat May 15 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- aalib adicionada ao Conectiva Linux
- traduções para pt_BR incluídas para Summary, %description e Group

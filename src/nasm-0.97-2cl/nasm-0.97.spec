%define name nasm
%define version 0.97
%define release 2cl
%define prefix /usr

Summary: The Netwide Assembler.
Summary(pt_BR): O "Netwide Assembler"
Summary(es): The Netwide Assembler.
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root
Prefix: %{prefix}
ExclusiveArch: i386

%description
This is a distribution of NASM, the Netwide Assembler. NASM is a
prototype general-purpose x86 assembler. It will currently output
flat-form binary files, a.out, COFF and ELF Unix object files,
Microsoft Win32 and 16-bit DOS object files, OS/2 object files, the
as86 object format, and a home-grown format called RDF.

Also included is NDISASM, a prototype x86 binary-file disassembler
which uses the same instruction table as NASM.

%description -l pt_BR
Este é o NASM, o "Netwide Assembler". o NASM é um assembler para
a familia x86 de processadores. Atualmente, ele sabe gerar binários
puros, a.out, COFF, ELF, Microsoft Win32 e 16 bits DOS, OS/2, as86,
e um formato "caseiro" chamado RDF.

%description -l es
This is a distribution of NASM, the Netwide Assembler. NASM is a
prototype general-purpose x86 assembler. It will currently output
flat-form binary files, a.out, COFF and ELF Unix object files,
Microsoft Win32 and 16-bit DOS object files, OS/2 object files, the
as86 object format, and a home-grown format called RDF.

Also included is NDISASM, a prototype x86 binary-file disassembler
which uses the same instruction table as NASM.

%prep
%setup -q

%build

export CFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
./configure --prefix=%{prefix}
make

%install

install -d $RPM_BUILD_ROOT%{prefix}/bin
install -d $RPM_BUILD_ROOT%{prefix}/man/man1
install -m 755 -o 0 -g 0 nasm $RPM_BUILD_ROOT%{prefix}/bin
install -m 755 -o 0 -g 0 ndisasm $RPM_BUILD_ROOT%{prefix}/bin
install -m 644 -o 0 -g 0 nasm.1 ndisasm.1 $RPM_BUILD_ROOT%{prefix}/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Readme Changes Licence Wishlist doc/
%{prefix}/bin/nasm
%{prefix}/bin/ndisasm
%{prefix}/man/man1/nasm.1
%{prefix}/man/man1/ndisasm.1

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue May 18 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added ExclusiveArch: i386 to spec file
- Added package to Conectiva Linux

* Mon Mar 29 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- First build with RPM (version 0.97)
- Added pt_BR translations

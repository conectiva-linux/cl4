Summary: Bonnie benchmark for Unix filesystems
Summary(pt_BR): Benchmark (teste de performance) Bonnie para Sistemas de Arquivos Unix
Summary(es): Benchmark (prueba de desempeño) Bonnie para Sistemas de Archivos Unix
Name: bonnie
Version: 1.0
Release: 8cl
Source: http://metalab.unc.edu/pub/Linux/system/benchmark/bonnie.tar.gz
Copyright: distributable
Group: Applications/Benchmarks
Group(pt_BR): Aplicações/Teste de Performance
Group(es): Aplicaciones/Teste de Performance
BuildRoot: /tmp/bonnie

%description
Bonnie is a popular performance benchmark that targets various aspects of
Unix filesystems.

%description -l pt_BR
Bonnie é um benchmark (teste de performance) popular que verifica
vários aspectos de sistemas de arquivos Unix

%description -l es
Bonnie es un benchmark (prueba de desempeño) popular que verifica
varios aspectos de sistemas de archivos Unix

%prep
%setup -n bonnie

%build
gcc -O2 -o bonnie bonnie.c

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -o root -g root -s -m 0755 bonnie $RPM_BUILD_ROOT/usr/sbin/bonnie
install -o root -g root -m 744 bonnie.man $RPM_BUILD_ROOT/usr/man/man1/bonnie.1

%files
%doc bonnie.doc
/usr/sbin/bonnie
/usr/man/man1/bonnie.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Dec 10 1998 Conectiva <dist@conectiva.com>
- final rebuild for 3.0

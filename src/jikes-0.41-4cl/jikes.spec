Summary: Java Compiler
Summary(pt_BR): Compilador Java
Summary(es): Compilador Java
Name: jikes
Version: 0.41
Release: 4cl
Copyright: IBM Jikes Compiler Open Source License
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
URL: http://www.ibm.com/research/jikes
Source: jikesos.tar.bz2
BuildRoot: /var/tmp/jikes

%description
JikesTM is a compiler from Java source code to bytecode. If you need
more information, see http://www.alphaworks.ibm.com/formula/jikes,

%description -l pt_BR
Jikes (TM) é um compilador de fontes Java para bytecode. É um compilador
rápido e que segue estritamente os padrões da linguagem Java.
Para mais informações veja http://www.alphaworks.ibm.com/formula/jikes.

%description -l es
Jikes (TM) es un compilador de fuentes Java para bytecode. Es
un compilador rápido y que sigue estrictamente los
patrones del lenguaje Java.  Para más información mira
http://www.alphaworks.ibm.com/formula/jikes.

%prep
%setup -n jikesos

%build
cd jikes/src
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -s jikes/src/jikes $RPM_BUILD_ROOT/usr/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /usr/bin/jikes
%doc README.TXT license.htm jikesos.htm

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Dec 09 1998 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- first package

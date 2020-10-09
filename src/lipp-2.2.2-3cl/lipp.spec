Summary: LDP Getting Started Guide (Spanish translation)
Summary(pt_BR): LDP - Guia de Instala��o (Tradu��o para o Espanhol)
Summary(es): Libro de instalaci�n y guia para nuevos usuarios del sistema Linux
Name: lipp
Version: 2.2.2
Release: 3cl
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Source0: lipp-1.1.txt.gz
Copyright: distributable
BuildRoot: /var/tmp/lipp-root
BuildArchitectures: noarch

%description
A general guide for installing and getting started with Linux.  The
installation sections should be ignored, in favor of the Red Hat
Linux manual.  Although, there is overlap, there is other useful 
information in this guide.

This is the spanish translation of the Linux install guide.

%description -l pt_BR
Um guia gen�rico para instalar e come�ar a trabalhar com o Linux.
A se��o referente � instala��o deve ser ignorada, em favor do 
manual de instala��o do Conectiva Linux. Apesar de ser um pouco
desatualizado, h� informa��es �teis neste guia.
Esta � uma vers�o em espanhol.

%description -l es
Este es un libro de instalaci�n y guia para nuevos usuarios del
sistema Linux, dirigido tanto a los mas noveles en UNIX, como a
los mas expertos. Contiene informaci�n sobre como conseguir el
Linux, la instalaci�n de nuevo software, un tutorial para
principiantes de UNIX y una introducci�n a la administraci�n del
sistema.  Hemos pretendido ser tan gen�ricos como nos ha sido
posible de tal modo que el libro pueda ser aplicable a cualquiera
de las distribuciones de software para Linux.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sat Mar 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- include es description, summary and group

* Tue Mar 16 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- created the package

%install

mkdir -p $RPM_BUILD_ROOT/usr/doc/LDP/lipp
chmod 755 $RPM_BUILD_ROOT/usr/doc/LDP/lipp
cp -a %{SOURCE0} $RPM_BUILD_ROOT/usr/doc/LDP/lipp

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/doc/LDP/lipp

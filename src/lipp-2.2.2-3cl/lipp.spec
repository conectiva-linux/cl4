Summary: LDP Getting Started Guide (Spanish translation)
Summary(pt_BR): LDP - Guia de Instalação (Tradução para o Espanhol)
Summary(es): Libro de instalación y guia para nuevos usuarios del sistema Linux
Name: lipp
Version: 2.2.2
Release: 3cl
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
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
Um guia genérico para instalar e começar a trabalhar com o Linux.
A seção referente à instalação deve ser ignorada, em favor do 
manual de instalação do Conectiva Linux. Apesar de ser um pouco
desatualizado, há informações úteis neste guia.
Esta é uma versão em espanhol.

%description -l es
Este es un libro de instalación y guia para nuevos usuarios del
sistema Linux, dirigido tanto a los mas noveles en UNIX, como a
los mas expertos. Contiene información sobre como conseguir el
Linux, la instalación de nuevo software, un tutorial para
principiantes de UNIX y una introducción a la administración del
sistema.  Hemos pretendido ser tan genéricos como nos ha sido
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

Summary: NLS files used by Motif, Netscape antigo, etc
Summary(pt_BR): Arquivos NLS usados pelo Motif, Netscape, etc.
Summary(es): Archivos NLS usados por el Motif, Netscape, etc.
Name: nls
Version: 1.0
Release: 7cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: nls-1.0.tar.gz
BuildArchitectures: noarch
BuildRoot: /var/tmp/nls-root

%description
This is a package of files used by some older X11R5 binaries such
at Netscape.  It isn't required by versions of Netscape greater than
3.0, however.

%description -l pt_BR
Este é um pacote de arquivos usados por alguns velhos binários
X11R5 como Netscape. Contudo, ele não é necessário para versões do
Netscape superiores ao 3.0.

%description -l es
Este es un paquete de archivos usados por algunos binarios antiguos
X11R5 como Netscape. Además, no hace falta para versiones del
Netscape superiores al 3.0.

%prep 
%setup -q -n nls

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/nls
cp -ar * $RPM_BUILD_ROOT/usr/X11R6/lib/X11/nls

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/lib/X11/nls

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

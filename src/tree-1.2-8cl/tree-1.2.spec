Summary: Prints out a view of a directory tree
Summary(pt_BR): Mostra uma árvore de diretórios
Summary(es): Enseña un árbol de directorios
Name: tree
Version: 1.2
Release: 8cl
Group: Applications/File
Group(pt_BR): Aplicações/Arquivo
Group(es): Aplicaciones/Archivo
Copyright: GPL
Source: ftp://sunsite.unc.edu/pub/Linux/Incoming/tree-1.2.tgz
Patch: tree-1.0-misc.patch
Prefix: /usr
BuildRoot: /var/tmp/tree-root
Summary(de): Druckt eine Ansicht einer Dateihierarchie 
Summary(fr): Affiche une arborescence de répertoires
Summary(tr): Bir dizin aðacýnýn görünümünü listeler

%description
This program is basically a UNIX port of the very useful DOS utility 
'tree', which prints out a view of the specified directory tree, along 
with the files it owns. Includes support for 'color ls'-style listings.

%description -l pt_BR
Este programa é basicamente um porte UNIX do muito prático utilitário
"tree" para DOS. Ele mostra a visualização da árvore do diretório
especificado, junto com os arquivos que pertencem a ele. Inclui
suporte para listas no estilo "color ls".

%description -l es
Este programa es básicamente un porte UNIX del muy práctico
utilitario "tree" para DOS. Enseña la visualización del árbol
del directorio especificado, junto con los archivos que le
pertenecen. Incluye soporte para listados en el estilo "color ls".

%description -l de
Dieses Programm ist im Prinzip ein UNIX-Port des äußerst praktischen
DOS-Utility-Programms tree, das eine Darstellung des gewünschten
Verzeichnisbaums ausgibt, zusammen mit den Dateien, die ihm gehören. 
Beinhaltet auch Unterstützung für 'color ls'-artige Auflistungen.

%description -l fr
Ce programme est à la base un portage sous UNIX de l'utilitaire DOS
'tree', qui  affiche l'arbrescence d'un répertoire spécifié. Il inclue
un support pour des listings de style 'color ls'.

%description -l tr
Bu program kullanýþlý bir DOS aracý olan tree'nin UNIX'e taþýnmýþ biçimidir.
Bir dizin aðacýnýn görünümünü içinde yer alan altdizinler ve dosyalarla
beraber listeler.

%prep
%setup -q
#%patch -p1

%build
rm -f tree
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	MANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/tree
/usr/man/man1/tree.1
%doc README

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 29 1998 Cristian Gafton <gafton@redhat.com>
- installing in /usr/bin

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed src url

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

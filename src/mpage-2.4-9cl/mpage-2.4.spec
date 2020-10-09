Summary: places multiple pages of text onto a single postscript page
Summary(pt_BR): Junta v�rias p�ginas de texto em uma p�gina postscript
Summary(es): Une varias p�ginas de texto en una p�gina postscript
Name: mpage
Version: 2.4
Release: 9cl
Copyright: BSD
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
# was .tgz
Source: ftp://sunsite.unc.edu:/pub/Linux/system/printing/mpage24.tar.bz2
Patch: mpage24-config.patch
Patch1: mpage24-dvips.patch
BuildRoot: /var/tmp/mpage-root
Summary(de): plaziert mehrere Textseiten auf eine einzelne Postscript-Seite
Summary(fr): Place plusieurs pages de texte sur une simple page postscript.
Summary(tr): Birden fazla metin sayfas�n� tek bir PostScript sayfas�na yerle�tirir

%description
mpage formats multiple pages of ASCII text onto a single page of
PostScript. It supports many different layouts for the final pages.

%description -l pt_BR
mpage formata m�ltiplas p�ginas de texto ASCII em uma �nica p�gina
de PostScript. Ele suporta v�rios layouts diferentes para as
p�ginas finais.

%description -l es
mpage formatea m�ltiples p�ginas de texto ASCII en una �nica p�gina
de PostScript. Soporta varios visuales diferentes para las p�ginas
finales.

%description -l de
mpage formatiert mehrere Seiten ASCII-Text in eine einzelne 
PostScript-Seite. Es unterst�tzt eine gro�e Auswahl von Layouts." 

%description -l fr
mpage formate plusieurs pages de texte ASCII en un seule en PostScript.
Il reconnait plusieurs mises en pages.

%description -l tr
mpage �ok sayfal� ASCII metinlerini tek bir PostScript sayfas�na bi�imler.
Sayfan�n son �eklinin de�i�ik bi�imlerde elde edilebilmesine olanak verir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/mpage,man/man1}

make PREFIX=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/mpage

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES Copyright README NEWS TODO
/usr/bin/mpage
/usr/man/man1/mpage.1
/usr/lib/mpage

%changelog
* Mon Jun  7 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Aug 16 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 15 1997 Michael Fulbright <msf@redhat.com>
- (Re)applied patch to correctly print dvips output.

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

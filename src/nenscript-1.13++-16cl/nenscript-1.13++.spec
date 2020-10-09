Summary: converts plain ascii to PostScript
Summary(pt_BR): Converte texto para PostScript
Summary(es): Convierte texto a PostScript
Name: nenscript
Version: 1.13++
Release: 16cl
Copyright: BSD
Group: Applications/Publishing
Group(pt_BR): Aplica��es/Editora��o
Group(es): Aplicaciones/Editoraci�n
Source0: ftp://sunsite.unc.edu/pub/Linux/system/printing/nenscript-1.13++.tar.z
Patch: nenscript-1.13++-config.patch
BuildRoot: /var/tmp/nenscript-root
Summary(de): konvertiert unformatiertes ASCII in PostScript 
Summary(fr): convertit de l'ascii simple en PostScript
Summary(tr): D�z ASCII dosyalar�n� postcript format�na �evirir

%description
nenscript is a print filter.  It can take ASCII input and format it into 
PostScript output and at the same time can do nice transformations like 
putting 2 ASCII pages on one physical page (side by side).

%description -l pt_BR
nenscript � um filtro de impress�o. Ele pode pegar entradas ASCII e
formatar para sa�da em PostScript e ao mesmo tempo pode fazer boas
transforma��es como por duas p�ginas ASCII em uma p�gina f�sica
(lado a lado).

%description -l es
nenscript es un filtro de impresi�n. Puede coger entradas ASCII y
formatear para salida en PostScript y al mismo tiempo puede hacer
buenas transformaciones como poner de las p�ginas ASCII en una
p�gina f�sica (lado a lado).

%description -l de
nenscript ist ein Druckfilter. Es kann ASCII in PostScript
konvertieren und gleichzeitig Umwandlungen ausf�hren, z.B. 
zwei ASCII-Seiten auf einer Seite unterbringen (nebeneinander).

%description -l fr
nenscript est un filtre d'impression. Il prend une entr�e ASCII et la
formate en sortie PostScript tout en pouvant faire des transformations
comme mettre 2 pages ASCII sur une seule page physique (c�te � c�te).

%description -l tr
nenscript normal ASCII dosyalar�n� al�p Postscript format�na d�n��t�r�r. Bu
i�lem s�ras�nda dosya �zerinde baz� sevimli i�lemler de yapabilir. �rnek
olarak iki ASCII sayfas�n� bir sayfa i�erisinde yanyana bas�lmas�n�
sa�layabilir.

%prep
%setup -q
%patch -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make INSTALLDIR=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/nenscript
/usr/man/man1/nenscript.1

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun Oct 25 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated spec file

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Fri Mar 28 1997 Michael Fulbright <msf@redhat.com>
- Removed asc-to-ps.fpi filter from this package, we now use mpage.

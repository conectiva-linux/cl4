Summary: xpdf is a PDF viewer
Summary(pt_BR): Visualizador de arquivos PDF
Summary(es): Visualizador de archivos PDF
Name: xpdf
Version: 0.80
Release: 5cl
Copyright:Distibutable
#Source: ftp://ftp.foolabs.com/pub/xpdf/xpdf-0.80.tgz
# recompressed with bzip2
Source: ftp://ftp.foolabs.com/pub/xpdf/xpdf-0.80.tar.bz2
Source1: xpdf.wmconfig
Source800: xpdf-wmconfig.i18n.tgz
Url: http://www.aimnet.com/~derekn/xpdf/
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
BuildRoot: /var/tmp/xpdf-root

%description
Xpdf is a viewer for Portable Document Format (PDF) files.  (These are also
sometimes also called 'Acrobat' files, from the name of Adobe's PDF
software.) Xpdf is designed to be small and efficient.  It does not use the
Motif or Xt libraries.  It uses standard X fonts.  Xpdf is quite usable on a
486-66 PC running Linux.

%description -l pt_BR
Xpdf é um visualizador de arquivos PDF (Portable Document Format).
(Estes são algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e 
eficiente. Ele usa fontes padrão X e não precisa das bibliotecas
Motif ou Xt.

%description -l es
Xpdf es un visor de archivos PDF (Portable Document Format).
(Estos son algunas veces llamados de archivos 'Acrobat', nombre
del software PDF del Adobe. Xpdf fue proyectado para ser pequeño
y eficiente. Usa fuentes padrón X y no necesita de las bibliotecas
Motif el Xt.

%changelog
* Tue Mar 16 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Tue Dec 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17
- atualizado para 0.80

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
 - updated to 0.7a

* Thu Nov 20 1997 Otto Hammersmith <otto@redhat.com>
- added changelog
- added wmconfig

%prep
%setup

%build
./configure --prefix=/usr --with-gzip
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
make install prefix=$RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig



tar xvfpz $RPM_SOURCE_DIR/xpdf-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%files
%doc CHANGES README
/usr/bin/*
/usr/man/man1/*
%config /etc/X11/wmconfig/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

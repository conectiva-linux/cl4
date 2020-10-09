Name: gimp-manual
Version: 1.0.0
Release: 4cl
Summary: This package includes a HTML version of the gimp manual
Summary(pt_BR): Vers�o HTML do manual do gimp.
Summary(es): Versi�n HTML del manual del gimp.
Group: Documentation
Group(pt_BR): Documenta��o
Group(es): Documentaci�n
Copyright: OpenContent
Source: ftp://manual.gimp.org/pub/manual/GimpUserManual-1.0.0-html.tar.bz2
Source800: wmconfig.i18n.tgz
Buildroot: /var/tmp/gimp-manual-root
BuildArch: noarch

%description
This is release 1.0.0 of the GIMP User's Manual (GUM).  This is the first
stable release of the manual, a product of almost a year of work.  It is
available in HTML, PS, PDF and FM (FrameMaker) source code.  Please read
COPYING for the license terms of the manual.

The manual is about 590 pages long and there have been several imporvments
over previous versions.  Be sure to pay special attention to the new Gallery
chaper which contains many nice images and a hints on how to make them. The
Gallery is a good example of what you can do with the GIMP. All images in
the manual is 100%% pure GIMP images.

The HTML version is suitable for online manual, PS and PDF are suitable if
you want to print it on a regular printer or have a nice looking online
manual.  The FM source code is only useful if you want to contribute to the
Graphic Documentation Project.  Submissions to the GIMP User's manual will
follow under the license agreement in the COPYING file.

The HTML version of the manual, while convenient for  an online manual, is
not the same quality of the PDF or PostScript formats. Improvements will be
made to the HTML version later.  This release was under a time constraint.

For other formats of this manual check ftp://manual.gimp.org/pub/manual

%description -l pt_BR
Esta � a vers�o 1.0.0 do Manual do Usu�rio do GIMP (GUM). � a primeira
vers�o est�vel do manual, produto de quase um ano de trabalho. Est�
dispon�vel em HTML, PS, PDF e c�digo fonte FM (FrameMaker). Por favor
leia o arquivo COPYING para informa��es sobre os termos de licen�a do
manual.

O manual tem mais ou menos 590 p�ginas e v�rias melhorias em rela��o �
vers�o anterior. Certifique-se de ler o cap�tulo "Gallery" que cont�m
muitas imagens bonitas e dicas de como cri�-las. A "Gallery" � um bom
exemplo do que pode ser feito com o GIMP. Todas as imagens no manual
foram feitas exclusivamente com o GIMP.

A vers�o HTML � apropriada para um manual online, enquanto as vers�es
PS e PDF s�o apropriadas para impress�o ou para ter um manual online
com maior qualidade. O c�digo fonte FM � �til somente para os interessados
em contribuir com o Projeto de Documenta��o Gr�fica. As contribui��es
para o Manual do Usu�rio do GIMP ser�o liberadas de acordo com a
licen�a contida no arquivo COPYING.

Apesar da vers�o HTML do manual ser conveniente para ser usada como um
manual on-line, n�o tem a mesma qualidade dos formatos PDF e PostScript.

Para obter outros formatos deste manual visite ftp://manual.gimp.org/pub/manual

%description -l es
Esta es la versi�n 1.0.0 del Manual del Usuario del GIMP (GUM). Es
la primera versi�n estable del manual, producto de casi un a�o
de trabajo. Est� disponible en HTML, PS, PDF y c�digo fuente FM
(FrameMaker). Por favor, lee el archivo COPYING para informaci�n
sobre los t�rminos de la licencia del manual.  El manual tiene m�s
o menos 590 p�ginas y varias mejoras con relaci�n a la versi�n
anterior. Aseg�rate de leer el cap�tulo "Gallery" que contiene
muchas im�genes bonitas y trucos de como crearlas. La "Gallery"
es un buen ejemplo de lo que puede ser hecho con GIMP. Todas
las im�genes en el manual fueron hechas exclusivamente con GIMP.
La versi�n HTML es apropiada para un manual online, en cuanto las
versiones PS y PDF lo son para impresi�n, o para tener un manual
online con una mayor calidad. El c�digo fuente FM es �til solamente
para los interesados en contribuir con el Proyecto de Documentaci�n
Gr�fica. Las contribuciones para el Manual del Usuario del GIMP ser�n
liberadas de acuerdo con la licencia contenida en el archivo COPYING.
A pesar de la versi�n HTML del manual ser conveniente para usarse
como un manual online no tiene la misma calidad de los formatos
PDF y PostScript.  Mejoras se har�n, en el futuro, en la versi�n
HTML. Esta versi�n ha tenido restricciones de tiempo.  Para obtener
otros formatos de este manual visita ftp://manual.gimp.org/pub/manual

%prep
%setup -n GimpUserManaul_v1.0.0

%build
echo Done

%install
rm -rf $RPM_BUILD_ROOT
echo Done

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/
tar xvfpz $RPM_SOURCE_DIR/wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc *
/etc/X11/wmconfig/gimp-manual

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Jun  8 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations
- i18n wmconfig

* Mon Dec 14 1998 Conectiva <dist@conectiva.com>
- final rebuild for 3.0

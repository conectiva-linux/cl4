Name: gimp-manual
Version: 1.0.0
Release: 4cl
Summary: This package includes a HTML version of the gimp manual
Summary(pt_BR): Versão HTML do manual do gimp.
Summary(es): Versión HTML del manual del gimp.
Group: Documentation
Group(pt_BR): Documentação
Group(es): Documentación
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
Esta é a versão 1.0.0 do Manual do Usuário do GIMP (GUM). É a primeira
versão estável do manual, produto de quase um ano de trabalho. Está
disponível em HTML, PS, PDF e código fonte FM (FrameMaker). Por favor
leia o arquivo COPYING para informações sobre os termos de licença do
manual.

O manual tem mais ou menos 590 páginas e várias melhorias em relação à
versão anterior. Certifique-se de ler o capítulo "Gallery" que contém
muitas imagens bonitas e dicas de como criá-las. A "Gallery" é um bom
exemplo do que pode ser feito com o GIMP. Todas as imagens no manual
foram feitas exclusivamente com o GIMP.

A versão HTML é apropriada para um manual online, enquanto as versões
PS e PDF são apropriadas para impressão ou para ter um manual online
com maior qualidade. O código fonte FM é útil somente para os interessados
em contribuir com o Projeto de Documentação Gráfica. As contribuições
para o Manual do Usuário do GIMP serão liberadas de acordo com a
licença contida no arquivo COPYING.

Apesar da versão HTML do manual ser conveniente para ser usada como um
manual on-line, não tem a mesma qualidade dos formatos PDF e PostScript.

Para obter outros formatos deste manual visite ftp://manual.gimp.org/pub/manual

%description -l es
Esta es la versión 1.0.0 del Manual del Usuario del GIMP (GUM). Es
la primera versión estable del manual, producto de casi un año
de trabajo. Está disponible en HTML, PS, PDF y código fuente FM
(FrameMaker). Por favor, lee el archivo COPYING para información
sobre los términos de la licencia del manual.  El manual tiene más
o menos 590 páginas y varias mejoras con relación a la versión
anterior. Asegúrate de leer el capítulo "Gallery" que contiene
muchas imágenes bonitas y trucos de como crearlas. La "Gallery"
es un buen ejemplo de lo que puede ser hecho con GIMP. Todas
las imágenes en el manual fueron hechas exclusivamente con GIMP.
La versión HTML es apropiada para un manual online, en cuanto las
versiones PS y PDF lo son para impresión, o para tener un manual
online con una mayor calidad. El código fuente FM es útil solamente
para los interesados en contribuir con el Proyecto de Documentación
Gráfica. Las contribuciones para el Manual del Usuario del GIMP serán
liberadas de acuerdo con la licencia contenida en el archivo COPYING.
A pesar de la versión HTML del manual ser conveniente para usarse
como un manual online no tiene la misma calidad de los formatos
PDF y PostScript.  Mejoras se harán, en el futuro, en la versión
HTML. Esta versión ha tenido restricciones de tiempo.  Para obtener
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

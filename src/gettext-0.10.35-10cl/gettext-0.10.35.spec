Summary: Libraries and utilties for program national language support
Summary(pt_BR): Bibliotecas e utilit�rios para o programa de suporte de l�nguas locais.
Summary(es): Bibliotecas y utilitarios para el programa de soporte a lenguas locales.
Name: gettext
Version: 0.10.35
Release: 10cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://alpha.gnu.org/pub/gnu/gettext-0.10.35.tar.bz2
Source1: tupdate
Patch0: gettext-0.10-misc.patch
Patch1: gettext-0.10.35-jbj.patch
Patch2: gettext-0.10.35-pt_BR.patch.bz2
Patch3: gettext-0.10.35-hacks.patch
Buildroot: /var/tmp/gettext-root
Summary(de): Libraries und Utilities zum Programmieren von nationaler Sprachunterst�tzung
Summary(fr): Librairies et  utilitaires pour le support de la langue nationnalepar les programmes.
Summary(tr): Yerel dil deste�i i�in kitapl�k ve ara�lar

%description
The gettext library provides an easy to use library and tools for creating,
using, and modifying natural language catalogs. It is a powerfull and simple
method for internationalizing programs.

%description -l pt_BR
A biblioteca gettext oferece uma biblioteca f�cil de usar e
ferramentas para cria��o, uso e modifica��o de cat�logos de linguagem
natural. Ele � um poderoso e simples m�todo de internacionaliza��o
de programas.

%description -l es
La biblioteca gettext nos ofrece una biblioteca f�cil de usar
y herramientas para creaci�n, uso y modificaci�n de cat�logos
de lenguaje natural. Es un potente y sencillo m�todo de
internacionalizaci�n de programas.

%description -l de
Die gettext-Library enth�lt eine einfach anzuwendende Library und Tools
zum Erstellen, Verwenden und �ndern von nat�rlichsprachigen-Kataloge. Es ist
ein einfaches und leistungsf�higes Verfahren zum Lokalisieren von Programmen.

%description -l fr
La librarie gettext fournit des outils et une librairie simple � utiliser
pour manipuler, cr�er, et modifier des catalogues de langage naturel. C'est
une m�thode simple et puissante pour internationnaliser les programmes.

%description -l tr
gettext, yerel dil deste�inde kullan�lan kataloglar� de�i�tirebilmek i�in,
kolayca kullan�labilen kitapl�k ve ara�lar� sa�lar. Bu, programlar�
uluslararas�la�t�rmak i�in s�k�a ba�vurulan, kuvvetli bir y�ntemdir.

%package tupdate
Summary: perl script, similar to msgmerge
Summary(pt_BR): Script Perl, similar ao msgmerge
Summary(es): Script perl, similar a lo msgmerge
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas

%description tupdate
perl script, similar to msgmerge

%description -l pt_BR tupdate
Script Perl, similar ao msgmerge

%description -l es tupdate
Script perl, similar a lo msgmerge

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
#%patch0 -p1 -b .misc
%patch1 -p1 -b .jbj
%patch2 -p1
%patch3 -p1

%build
unset LINGUAS
aclocal
automake
autoconf
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \
	--enable-shared --with-included-gettext $RPM_ARCH-conectiva-linux
make

%install
rm -rf $RPM_BUILD_ROOT

make install prefix=$RPM_BUILD_ROOT/usr

# Install /usr/bin/gettextize
( cd misc
  make install-exec prefix=$RPM_BUILD_ROOT/usr
)

# Install libgettext.h, the "--with-gnu-gettext" libintl.h from compile.
( cd $RPM_BUILD_ROOT
  mv ./usr/include/{libintl,libgettext}.h

  rm -f ./usr/info/dir
  gzip -9nf ./usr/info/*
  strip ./usr/bin/* || :
)

cp $RPM_SOURCE_DIR/tupdate $RPM_BUILD_ROOT/usr/bin
mkdir $RPM_BUILD_ROOT/bin
mv $RPM_BUILD_ROOT/usr/bin/gettext $RPM_BUILD_ROOT/bin
ln -sf /bin/gettext $RPM_BUILD_ROOT/usr/bin/gettext

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/gettext.info.gz /usr/info/dir

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/gettext.info.gz /usr/info/dir
fi

%files
%defattr(-,root,root)
/bin/gettext
/usr/share/gettext
/usr/share/locale/*/LC_MESSAGES/gettext.mo
/usr/info/*
/usr/bin/gettext
/usr/bin/gettextize
/usr/bin/msgcmp
/usr/bin/msgcomm
/usr/bin/msgfmt
/usr/bin/msghack
/usr/bin/msgmerge
/usr/bin/msgunfmt
/usr/bin/xgettext
/usr/share/aclocal/*

%files tupdate
/usr/bin/tupdate

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 24 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Adjusted the patch to add pt_BR translation to use ALL_LINGUAS,
  instead of LINGUAS
- unset LINGUAS
- added /usr/bin/msghack to file list

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Mar 11 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- gettext goes to /bin, as required by initscripts i18n (/usr/bin/gettext
  stays as a symlink)
- tupdate goes to a separate package, so that gettext doesn't requires perl

* Sun Nov 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR.po
- env var LINGUAS was missing

* Thu Oct 08 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- tupdate is back! :)

* Mon Oct 05 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- include the aclocal support files

* Fri Sep  3 1998 Bill Nottingham <notting@redhat.com>
- remove devel package (functionality is in glibc)

* Tue Sep  1 1998 Jeff Johnson <jbj@redhat.com>
- update to 0.10.35.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- add gettextize.
- create devel package for libintl.a and libgettext.h.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Nov 02 1997 Cristian Gafton <gafton@redhat.com>
- added info handling
- added misc-patch (skip emacs-lisp modofications)

* Sat Nov 01 1997 Erik Troan <ewt@redhat.com>
- removed locale.aliases as we get it from glibc now
- uses a buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- Built against glibc

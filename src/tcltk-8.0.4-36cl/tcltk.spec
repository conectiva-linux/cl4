%define	tclvers	8.0.4
%define	expvers	5.28
%define	itclvers	3.0.1

Summary: A Tcl/Tk development environment: tcl, tk, tix, tclX, expect, and itcl
Summary(pt_BR): tcl, tk, tix, tclX e expect
Summary(es):  tcl, tk, tix, tclX y expect
Name: tcltk
Version: %{tclvers}
Release: 36cl
Source0: ftp://ftp.scriptics.com/pub/tcl/tcl8_0/tcl%{tclvers}.tar.bz2
Source1: ftp://ftp.scriptics.com/pub/tcl/tcl8_0/tk%{tclvers}.tar.bz2
Source2: ftp://ftp.cme.nist.gov/pub/expect/expect.tar.bz2
Source3: ftp://ftp.neosoft.com/pub/tcl/TclX/tclX%{tclvers}.tar.bz2
Source4: ftp://ftp.xpi.com/pub/ioi/Tix4.1.0.006.tar.bz2
Source5: ftp://ftp.tcltk.com/pub/itcl/itcl%{itclvers}.tar.bz2
Patch0: tcltk-8.0-ieee.patch
Patch1: tcl8.0.3-glibc21.patch
Patch2: expect-5.24-mkpasswd.patch
Patch3: expect-5.26-alpha.patch
Patch4: expect-5.26-glibc21.patch
Patch5: expect-5.28-jbj.patch
Patch6: expect-5.28-pty.patch
Copyright: BSD
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Buildroot: /var/tmp/%{name}-root

%description
Tcl is a simple scripting language designed to be embedded into
other applications.  Tcl is designed to be used with Tk, a widget
set, which is provided in the tk package.  This package also includes
tclsh, a simple example of a Tcl application.

%description -l pt_BR
Pacote fonte para tcl, tk, tix, tclX e expect. Os pacotes binários
incluem descrições das funcionalidades fornecidas por cada parte
deste pacote.

%description -l es
Paquete fuente para tcl, tk, tix, tclX y expect. Los paquetes
binarios incluyen descripciones de las funcionalidades ofrecidas
por cada parte de este paquete.

%package -n tcl
#Version: 8.0.3
Summary: An embeddable scripting language.
Summary(pt_BR): TCL, com bibliotecas compartilhadas
Summary(es): TCL, con bibliotecas compartidas
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
URL: http://www.scriptics.com

%description -n tcl
Tcl is a simple scripting language designed to be embedded into
other applications.  Tcl is designed to be used with Tk, a widget
set, which is provided in the tk package.  This package also includes
tclsh, a simple example of a Tcl application.

If you're installing the tcl package and you want to use Tcl for
development, you should also install the tk and tclx packages.

%description -l pt_BR -n tcl
TCL é uma linguagem de scripting simples que é projetada para
ser embutida em outras aplicações. Este pacote inclui o tclsh, um
exemplo simples de aplicação tcl. TCL é muito popular para escrever
pequenas aplicações gráficas porque o conjunto de widgets TK é bem
integrado a ela.

%description -l es -n tcl
TCL es un lenguaje de scripting sencillo que está proyectado para ser
empotrado en otras aplicaciones. Este paquete incluye el tclsh, un
ejemplo sencillo de aplicación tcl. TCL es muy popular para escribir
pequeñas aplicaciones gráficas, pues el conjunto de widgets TK se
integra bien a él.

%package -n tk
#Version: 8.0.3
Summary: Tk GUI toolkit for Tcl, with shared libraries
Summary(pt_BR): Toolkit Tk para Tcl, com bibliotecas compartilhadas
Summary(es): Toolkit Tk para Tcl, con bibliotecas compartidas
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
Requires: ldconfig
URL: http://www.scriptics.com

%description -n tk
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -l pt_BR -n tk
Tk é um conjunto de widgets X Window projetado para trabalhar
intimamente com a linguagem de scripting tcl. Lhe permite escrever
programas simples com interface gráfica completa em pouco mais tempo
do que se leva para escrever uma interface modo texto. Aplicações
Tcl/Tl podem rodar também nas plataformas Windows e Macintosh.

%description -l es -n tk
Tk es un conjunto de widgets X Window proyectado para trabajar
íntimamente con el lenguaje de scripting tcl. Te permite escribir
programas sencillos con interface gráfica completa en poco más
tiempo de lo que se lleva para escribir una interface modo
texto. Aplicaciones Tcl/Tl pueden ejecutarse también en las
plataformas Windows y Macintosh.

%package -n expect
Version: %{expvers}
Summary: A tcl extension for simplifying program-script interaction.
Summary(pt_BR): Extensão tcl para permitir interação entre programas e scripts
Summary(es): Extensión tcl para permitir interacción entre programas y scripts
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes

%description -n expect
Expect is a tcl extension for automating interactive applications such
as telnet, ftp, passwd, fsck, rlogin, tip, etc.  Expect is also useful
for testing the named applications.  Expect makes it easy for a script
to control another program and interact with it.

Install the expect package if you'd like to develop scripts which interact
with interactive applications.  You'll also need to install the tcl
package.

%description -l pt_BR -n expect
Expect é uma ferramenta para automatizar aplicações interativas
como telnet, ftp, passwd, fsck, rlogin, tip, etc. Ele torna fácil
controlar e interagir com outros programas utilizando script.

%description -l es -n expect
Expect es una herramienta para automatizar aplicaciones interactivas
como telnet, ftp, passwd, fsck, rlogin, tip, etc. Vuelve  fácil el
control y intercambio con otros programas utilizando script.

%package -n tclx
#Version: 8.0.3
Summary: Tcl/Tk extensions for POSIX systems.
Summary(pt_BR): Extensões a tcl e tk para sistemas POSIX
Summary(es): Extensiones a tcl y tk a sistemas POSIX
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes
URL: http://www.neosoft.com/

%description -n tclx
TclX is a set of extensions which make it easier to use the Tcl
scripting language for common UNIX/Linux programming tasks.  TclX
enhances Tcl support for files, network access, debugging, math, lists,
and message catalogs.  TclX can be used with both Tcl and Tcl/Tk
applications.

Install TclX if you are developing applications with Tcl/Tk.  You'll
also need to install the tcl and tk packages.

%description -l pt_BR -n tclx
TclX é um conjunto de extensões a TCL que a tornam mais adequada
a tarefas de programação comuns no Unix. Ele adiciona ou melhora
o suporte a arquivos, acesso a rede, depuração, matemática, listas
e catálogos de mensagens. Pode ser usada em aplicações tcl e tcl/tk.

%description -l es -n tclx
TclX es un conjunto de extensiones a TCL que la hace más adecuada
a tareas de programación comunes en el Unix. Adiciona o mejora el
soporte a archivos, acceso a red, depuración, matemática, listas
y catálogos de mensajes. Se puede usar en aplicaciones tcl y tcl/tk.

%package -n tix
Version: 4.1.0.6
Summary: A set of capable widgets for Tk.
Summary(pt_BR): Muitos metawidgets (como notepads) para tk
Summary(es): Muchos metawidgets (como notepads) para tk
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes

%description -n tix
Tix (Tk Interface Extension), an add-on for the Tk widget set, is an
extensive set of over 40 widgets.  In general, Tix widgets are more
complex and more capable than the widgets provided in Tk.  Tix widgets
include a ComboBox, a Motif-style FileSelectBox, an MS Windows-style
FileSelectBox, a PanedWindow, a NoteBook, a hierarchical list, a
directory tree and a file manager.

Install the tix package if you want to try out more complicated widgets
for Tk.  You'll also need to have the tcl and tk packages installed.

%description -l pt_BR -n tix
Tix é um adicional ao conjunto de widgets tk que adiciona muitos
widgets complexos que são construídos com blocos de construção tk. Os
widgets extras incluem: combo box, seleção de arquivos, notebooks,
controles de rotação, janelas paned e caixas de listas hierárquicas.

%description -l es -n tix
Tix es un adicional al conjunto de widgets tk que adiciona muchos
widgets complejos que son construidos con bloques de construcción tk.
Los widgets extras incluyen: combo box, selección de archivos,
notebooks, controles de rotación, ventanas paned y cajas de listas
jerárquicas.

%package -n itcl
Version: %{itclvers}
Summary: object oriented mega widgets for tcl
Summary(pt_BR): Componentes (widgets) orientados a objeto para o tcl
Summary(es): Componentes (widgets) orientados a objeto para tcl
Group: Development/Languages
Group(pt_BR): Desenvolvimento/Linguagens
Group(es): Desarrollo/Lenguajes

%description -n itcl
[incr Tcl] is an object-oriented extension of the Tcl language.  It
was created to support more structured programming in Tcl.  Tcl scripts
that grow beyond a few thousand lines become extremely difficult to
maintain.  This is because the building blocks of vanilla Tcl are
procedures and global variables, and all of these building blocks
must reside in a single global namespace.  There is no support for
protection or encapsulation.

[incr Tcl] introduces the notion of objects.  Each object is a bag
of data with a set of procedures or "methods" that are used to
manipulate it.  Objects are organized into "classes" with identical
characteristics, and classes can inherit functionality from one
another.  This object-oriented paradigm adds another level of
organization on top of the basic variable/procedure elements, and
the resulting code is easier to understand and maintain.

%description -l pt_BR -n itcl
O [incr Tcl] é uma extensão orientada a objetos para a linguagem Tcl.
Foi criada para permitir uma programação mais estruturada em Tcl.
As scripts Tcl que crescem até algumas milhares de linhas se tornam
extremamente difíceis de manter. Isto é devido a necessidade de todos
os elementos do Tcl puro serem procedimentos e variáveis globais que
devem se localizar em um único espaço de nomes global. Não existe
suporte a proteção ou encapsulamento.

O [incr Tcl] introduz a noção de objetos. Cada objeto é um conjunto
de dados com um conjunto de procedimentos ou "métodos" que são usados
para manipulá-lo. Os objetos são organizados em "classes" com 
características idênticas e classes podem herdar funcionalidade umas
das outras. Este paradigma orientado a objetos adiciona outro nível
de organização por cima dos elementos básicos variável/procedimento e
o código resultante é mais compreensível e fácil de manter.

%description -l es -n itcl
[incr Tcl] es una extensión orientada a objetos para el lenguaje Tcl.
Fue creada para permitir una programación más estructurada en Tcl.
Las scripts Tcl que crecen hasta algunas millares de líneas se
vuelven extremamente difíciles de mantener. Esto es debido a la
necesidad de todos los elementos del Tcl puro ser procedimientos
y variables globales que deben localizarse en un único espacio
de nombres global. No existe soporte a protección o encapsulado.
[incr Tcl] introduce la noción de objetos. Cada objeto es un conjunto
de datos con un conjunto de procedimientos o "métodos" que son
usados para manipularlo. Los objetos son organizados en "clases"
con características idénticas y clases pueden heredar funcionalidad,
unas de las otras. Este paradigma, orientado a objetos, adiciona
otro nivel de organización por encima de los elementos básicos
variable/procedimiento y el código resultante es más comprensible
y fácil de mantener.

%prep

%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5

cd tcl%{tclvers}
#%patch0 -p2 -b .ieee
%patch1 -p2 -b .glibc21
cd ..

cd expect-%{expvers}
%patch2 -p2 -b .mkpasswd
%patch3 -p2 -b .alpha
%patch4 -p2 -b .glibc21
%patch5 -p2 -b .jbj
cd ..

# XXX this was only needed with the IEEE patch0
#cd tcl%{tclvers}/unix
#autoconf
#cd ../../
#cd tk%{tclvers}/unix
#autoconf

#==========================================
%build

# make the libraries reentrant
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_REENTRANT"

#------------------------------------------
# Tcl
#
cd tcl%{tclvers}/unix
#libtoolize --copy --force
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --enable-shared --enable-gcc

%configure --enable-shared --enable-gcc
make
cd ../..

#------------------------------------------
# Tk
#
cd tk%{tclvers}/unix
#libtoolize --copy --force
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --enable-shared --enable-gcc

%configure --enable-shared --enable-gcc
make
cd ../..

#------------------------------------------
# tclX
#
cd tclX%{tclvers}/unix
#libtoolize --copy --force
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --enable-shared

%configure --enable-shared --enable-gcc
make
cd ../..

#------------------------------------------
# Expect
#
cd expect-%{expvers}
#libtoolize --copy --force
#CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr \

%configure \
    --enable-shared --enable-gcc \
    --with-tclconfig=../tcl%{tclvers}/unix \
    --with-tkconfig=../tk%{tclvers}/unix \
    --with-tclinclude=../tcl%{tclvers}/generic \
    --with-tkinclude=../tk%{tclvers}/generic

# XXX drill out HAVE_OPENPTY for now
perl -pi -e 's,#define HAVE_OPENPTY 1,/* #undef HAVE_OPENPTY */,' expect_cf.h || :
# XXX drill in HAVE_PTMX for now
perl -pi -e 's,/* #undef HAVE_PTMX */,#define HAVE_PTMX 1' expect_cf.h || :

make

cd ..

#------------------------------------------
# Tix
#
cd Tix4.1.0/unix
#libtoolize --copy --force
#./configure --prefix=/usr --disable-cdemos --enable-shared

%configure --enable-shared --enable-gcc --disable-cdemos

cd tk8.0
#libtoolize --copy --force
#./configure --prefix=/usr --disable-cdemos --enable-shared \
#	--with-tcl=../../../tcl%{tclvers} --with-tk=../../../tk%{tclvers}

%configure --enable-shared --enable-gcc --disable-cdemos \
    --with-tcl=../../../tcl%{tclvers} \
    --with-tk=../../../tk%{tclvers}
make
cd ../../..

#------------------------------------------
# itcl
#
cd itcl%{itclvers}
#libtoolize --copy --force
#./configure --prefix=/usr --enable-shared

%configure --enable-shared --exec-prefix=/foo --enable-gcc
make
cd ..

#==========================================
%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

#------------------------------------------
# Tcl
#
cd tcl%{tclvers}/unix
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtcl8.0.so $RPM_BUILD_ROOT/usr/lib/libtcl.so
ln -sf tclsh8.0 $RPM_BUILD_ROOT/usr/bin/tclsh
cd ../..
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | sort > tcl.files

#------------------------------------------
# Tk
#
cd tk%{tclvers}/unix
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtk8.0.so $RPM_BUILD_ROOT/usr/lib/libtk.so
ln -sf wish8.0 $RPM_BUILD_ROOT/usr/bin/wish
cd ../..
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | cat - tcl.files \
	| sort | uniq -u > tk.files

#------------------------------------------
# TclX
#
cd tclX%{tclvers}/unix
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtkx%{tclvers}.so $RPM_BUILD_ROOT/usr/lib/libtkx.so
ln -sf libtclx%{tclvers}.so $RPM_BUILD_ROOT/usr/lib/libtclx.so
cd ../..
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | cat - tcl.files tk.files \
	| sort | uniq -u > tclx.files

#------------------------------------------
# Expect
#
cd expect-%{expvers}
make prefix=$RPM_BUILD_ROOT/usr install
cd ..
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | cat - tcl.files tk.files tclx.files \
	| sort | uniq -u > expect.files

# for files in expect.files, sed the #! at the top...
for n in `cat expect.files`; do
	if head -1 $n | grep '#!'; then
		cp -a $n $n.in
		sed "s|$RPM_BUILD_ROOT||" < $n.in > $n
		rm -f $n.in
	fi
done

#------------------------------------------
# Tix
#
cd Tix4.1.0/unix
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib make prefix=$RPM_BUILD_ROOT/usr install
cd ../..
mv $RPM_BUILD_ROOT/usr/man/mann/tixwish.1 $RPM_BUILD_ROOT/usr/man/man1/tixwish.1
ln -sf libtix4.1.8.0.so $RPM_BUILD_ROOT/usr/lib/libtix.so
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | cat - tcl.files tk.files tclx.files expect.files\
	| sort | uniq -u > tix.files

for n in `cat tix.files`; do
        if head -1 $n | grep '#!'; then
                cp -a $n $n.in
                sed "s|$RPM_BUILD_ROOT||" < $n.in > $n
		rm -f $n.in
        fi
done

#------------------------------------------
# itcl
#
cd itcl%{itclvers}
make INSTALL_ROOT=$RPM_BUILD_ROOT exec_prefix=/usr install
ln -sf libitk3.0.so $RPM_BUILD_ROOT/usr/lib/libitk.so
ln -sf libitcl3.0.so $RPM_BUILD_ROOT/usr/lib/libitcl.so
cd ..
(find $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT/usr/include \
	$RPM_BUILD_ROOT/usr/man -type f -o -type l;
 find $RPM_BUILD_ROOT/usr/lib/*) | cat - tcl.files tk.files tclx.files expect.files tix.files \
	| sort | uniq -u > itcl.files

for n in `cat itcl.files`; do
        if head -1 $n | grep '#!'; then
                cp -a $n $n.in
                sed "s|$RPM_BUILD_ROOT||" < $n.in > $n
		rm -f $n.in
        fi
done

#------------------------------------------
# this is too annoying to watch
set +x
for n in *.files; do
	mv $n $n.in
	sed "s|.*/usr|/usr|" < $n.in | while read file; do
	    if [ -d $RPM_BUILD_ROOT/$file ]; then
		echo -n '%dir '
	    fi
	    echo $file
	done > $n
done
set -x

#Strip the binaries
strip $RPM_BUILD_ROOT/usr/bin/* || :

#==========================================
%post -p /sbin/ldconfig -n tcl
%post -p /sbin/ldconfig -n tk
%post -p /sbin/ldconfig -n expect
%post -p /sbin/ldconfig -n tclx
%post -p /sbin/ldconfig -n tix
%post -p /sbin/ldconfig -n itcl

%postun -p /sbin/ldconfig -n tcl
%postun -p /sbin/ldconfig -n tk
%postun -p /sbin/ldconfig -n expect
%postun -p /sbin/ldconfig -n tclx
%postun -p /sbin/ldconfig -n tix
%postun -p /sbin/ldconfig -n itcl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f tcl.files -n tcl
%files -f tk.files -n tk
%files -f tclx.files -n tclx
%files -f expect.files -n expect
%files -f tix.files -n tix
%files -f itcl.files -n itcl

%changelog
* Mon Jun 28 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- sources recompressed

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x
- Added Requires: ldconfig to expect

* Thu Apr  8 1999 Jeff Johnson <jbj@redhat.com>
- use /usr/bin/write in kibitz (#1320).
- use cirrus.sprl.umich.edu in weather (#1926).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 28)

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- whoops, exec-prefix for itcl was set to '/foo', changed to '/usr'.

* Tue Feb 16 1999 Jeff Johnson <jbj@redhat.com>
- expect does unaligned access on alpha (#989)
- upgrade tcl/tk/tclX to 8.0.4
- upgrade expect to 5.28.
- add itcl 3.0.1

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to allow building on the arm
- build for glibc 2.1
- strip binaries

* Thu Sep 10 1998 Jeff Johnson <jbj@redhat.com>
- update tcl/tk/tclX to 8.0.3, expect is updated also.

* Mon Jun 29 1998 Jeff Johnson <jbj@redhat.com>
- expect: mkpasswd needs delay before sending password (problem #576)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- fixed expect binaries exec permissions

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to Tix 4.1.0.006
- updated version numbers of tcl/tk to relflect includsion of p2

* Wed Mar 25 1998 Cristian Gafton <gafton@redhat.com>
- updated tcl/tk to patch level 2
- updated tclX to 8.0.2

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed filelist for tix... replacing path to the expect binary in scripts
  was leaving junk files around.

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- added patch to remove libieee test in configure.in for tcl and tk.
  Shoudln't be needed anymore for glibc systems, but this isn't the "proper" 
  solution for all systems
- fixed src urls

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- removed version numbers from descriptions

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to tcl/tk 8.0 and related versions of packages

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- fixed dangling tclx/tkx symlinks

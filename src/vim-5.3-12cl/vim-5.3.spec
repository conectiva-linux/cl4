Summary: VIsual editor iMproved
Summary(pt_BR): Editor visual incrementado
Summary(es): Editor visual incrementado
Name: vim
Version: 5.3
Release: 12cl
Copyright: freeware
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
#Source0: ftp://ftp.oce.nl/pub/vim/unix/vim-%{version}-src.tar.gz
#Source1: ftp://ftp.oce.nl/pub/vim/unix/vim-%{version}-rt.tar.gz
# recompactados com bzip2
Source0: ftp://ftp.oce.nl/pub/vim/unix/vim-%{version}-src.tar.bz2
Source1: ftp://ftp.oce.nl/pub/vim/unix/vim-%{version}-rt.tar.bz2
Source2: vimx.wmconfig
Source3: vimrc
Source4: cvim
Source800: vim-wmconfig.i18n.tgz
Patch0: vim-4.2-speed_t.patch
Patch1: vim-5.1-vimnotvi.patch
Patch2: vim-5.1-tutor.patch
Buildroot: /var/tmp/vim-root
Summary(de): VIsual editor iMproved
Summary(fr): editeur VIM : VIsual editor iMproved.
Summary(tr): Geliþmiþ bir vi sürümü
#BuildPrereq: /d/misc/scripts/gzipman

%description
The VIsual editor iMproved is an updated and feature-added clone of the 'vi' 
editor that comes with almost all UN*X systems. It adds multiple windows,
multi-level undo, block highliting, and many other features to the standard
vi program.

%description -l pt_BR
O editor Visual Melhorado é um versão atualizada e com novas
características adicionais do mundialmente famoso 'vi' que acompanha
praticamente todos os sistemas UN*X. Ele possibilita trabalhar com
múltiplas janelas, vários níveis de desfazer, blocos enfatizados,
e muitas outras características do 'vi'.

%description -l es
El editor Visual Mejorado es una versión actualizada y con nuevas
características adicionales del mundialmente famoso 'vi' que acompaña
prácticamente todos los sistemas UN*X. Posibilita trabajar con
múltiples ventanas, varios niveles de deshacer, bloques enfatizados,
y otras muchas características del 'vi'.

%package common
Summary: Files needed by any vim editor
Summary(pt_BR): Arquivos necessários ao editor vim
Summary(es): Archivos necesarios al editor vim
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores

%description common
The VIsual editor iMproved is an updated and feature-added clone of the 'vi' 
editor that comes with almost all UN*X systems. It adds multiple windows,
multi-level undo, block highliting, and many other features to the standard
vi program.

The vim-common package contains files (such as help) that are needed by any
vim binary in order to run.

%description -l pt_BR common
O pacote vim-common contém os arquivos que são necessários
por todos os binários vim.

%description -l es common
El paquete vim-common contiene los archivos (como la ayuda) que
son necesarios para todos los binarios vim.

%package minimal
Summary: a vi-like editor.
Summary(pt_BR): Um editor tipo vi
Summary(es): Un editor tipo vi
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: vim-common
Obsoletes: vim
Obsoletes: vim-color

%description minimal
The VIsual editor iMproved is an updated and feature-added clone of the 'vi' 
editor that comes with almost all UN*X systems. It adds multiple windows,
multi-level undo, block highliting, and many other features to the standard
vi program.

The vim-minimal package installs a version of vim into /bin/vi that is
suitable for running when only the root partition is present.

%description -l pt_BR minimal
O pacote vim-minimal instala uma versão do vim em /bin/vi que é adequada
para execução quando somente a partição raiz estiver presente.

%description -l es minimal
El paquete vin-minimal instala una versión del vim en /bin/vi
que es adecuada a ejecución cuando solamente la partición raíz
está presente.

%package enhanced
Summary:  VIsual editor iMproved with all sorts of finery
Summary(pt_BR): Editor VI melhorado
Summary(es): Editor VI mejorado
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: vim-common
Obsoletes: vim-color

%description enhanced
The VIsual editor iMproved is an updated and feature-added clone of the 'vi' 
editor that comes with almost all UN*X systems. It adds multiple windows,
multi-level undo, block highliting, and many other features to the standard
vi program.

This package contains a version of vim which has many of the extra features
that have recently been introduced to vim such as perl and python
interpreters.

%description -l pt_BR enhanced
Este pacote contém uma versão do vim que tem muitas características extras
que foram recentemente introduzidas como interpretadores perl e python.

%description -l es enhanced
Este paquete contiene una versión del vim que tiene muchas
características extras que fueron recientemente introducidas como
interpretadores perl y python.

%package X11
Summary: VIM with X-Windows support
Summary(pt_BR): VIM com suporte a X-Window
Summary(es): VIM con soporte a X-Window
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: vim-common
Summary(de): VIM mit X-Windows-Support 
Summary(fr): VIM avec gestion X Window
Summary(tr): VIM için X11 desteði

%description X11
The VIsual editor iMproved is an updated and feature-added clone of the 'vi' 
editor that comes with almost all UN*X systems. It adds multiple windows,
multi-level undo, block highliting, and many other features to the standard
vi program.

This package is a version of VIM with the X-Windows libraries linked in,
allowing you to run VIM as an X-Windows application with a full GUI
interface and mouse support.  You just run 'gvim'.

%description -l pt_BR X11
Este pacote contém uma versão do VIM ligado com bibliotecas X-Window,
lhe permitindo executar o VIM como uma aplicação X-Window com interface
completamente gráfica e suporte a mouse. Para executá-lo digite 'gvim'.

%description -l es X11
Este paquete contiene una versión del VIM vinculada a bibliotecas
X-Window, que te permite ejecutar el VIM como una aplicación
X-Window con interface completamente gráfica y soporte a ratón. Para
ejecutarlo teclea 'gvim'.

%description -l de X11
Dieses Paket ist eine Version von VIM, mit gelinkten X-Windows-Libraries,
das es eerlaubt, VIM als eine X-Windows-Applikation mit einer kompletten
GUI-Schnittfläche und mit Mausunterstützung zu betreiben. Sie brauchen nur
'gvim' zu betreiben.

%package help
Summary: VIM help files
Summary(pt_BR): Arquivos de ajuda do vim
Summary(es): Archivos de ayuda del vim
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: vim-common

%description help
VIM help files, available using :h

%description -l pt_BR help
Arquivos de ajuda para o vim, disponíveis através de :h

%description -l es help
Archivos de ayuda para vim, disponibles a través de :h

%package syntax
Summary: VIM language syntax highlighting files
Summary(pt_BR): Arquivos para destacar a sintaxe de linguagens de programação quando editados no vim
Summary(es): Archivos para destacar la sintaxis de lenguajes de programación cuando editados en vim
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
Requires: vim-common

%description syntax
VIM language syntax highlighting files. Lots of languages already supported:

2html, ada, amiga, asm, asmh8300, asmselect, asn, atlas,
awk, basic, bib, c, clean, clipper, cobol, colortest, cpp,
csh, css, cterm, dcl, diff, dosbatch, dosini, dracula, dtd,
eiffel, elmfilt, esqlc, expect, exports, fortran, fvwm, gp,
help, hitest, html, idl, inform, java, javacc, javascript,
jgraph, lace, lex, lilo, lisp, lite, lotos, lss, mail,
make, man, maple, matlab, mf, mib, model, modula2, mp,
msql, muttrc, nasm, nosyntax, nroff, objc, ocaml, pascal,
pcap, perl, php3, phtml, pike, pmfile, po, pod, postscr,
pov, procmail, prolog, purifylog, python, rc, rexx, sather,
scheme, scripts, sdl, sgml, sh, sicad, simula, skill, slang,
slrnrc, slrnsc, sm, spec, sql, st, syntax, tags, tcl, tex,
tf, tsalt, uil, verilog, vgrindefs, vhdl, vim, viminfo, vrml,
whitespace, xdefaults, xmath, xml, xpm, yacc and zsh.

%description -l pt_BR syntax
Arquivos para destacar a sintaxe de linguagens
de programação quando editados no vim. 

Veja as linguagens já suportadas:

2html, ada, amiga, asm, asmh8300, asmselect, asn, atlas,
awk, basic, bib, c, clean, clipper, cobol, colortest, cpp,
csh, css, cterm, dcl, diff, dosbatch, dosini, dracula, dtd,
eiffel, elmfilt, esqlc, expect, exports, fortran, fvwm, gp,
help, hitest, html, idl, inform, java, javacc, javascript,
jgraph, lace, lex, lilo, lisp, lite, lotos, lss, mail,
make, man, maple, matlab, mf, mib, model, modula2, mp,
msql, muttrc, nasm, nosyntax, nroff, objc, ocaml, pascal,
pcap, perl, php3, phtml, pike, pmfile, po, pod, postscr,
pov, procmail, prolog, purifylog, python, rc, rexx, sather,
scheme, scripts, sdl, sgml, sh, sicad, simula, skill, slang,
slrnrc, slrnsc, sm, spec, sql, st, syntax, tags, tcl, tex,
tf, tsalt, uil, verilog, vgrindefs, vhdl, vim, viminfo, vrml,
whitespace, xdefaults, xmath, xml, xpm, yacc e zsh.

%description -l es syntax
Archivos para destacar la sintaxis de lenguajes de programación,
cuando editados en vim.  Mira los lenguajes ya soportados: 2html,
ada, amiga, asm, asmh8300, asmselect, asn, atlas, awk, basic, bib, c,
clean, clipper, cobol, colortest, cpp, csh, css, cterm, dcl, diff,
dosbatch, dosini, dracula, dtd, eiffel, elmfilt, esqlc, expect,
exports, fortran, fvwm, gp, help, hitest, html, idl, inform, java,
javacc, javascript, jgraph, lace, lex, lilo, lisp, lite, lotos,
lss, mail, make, man, maple, matlab, mf, mib, model, modula2, mp,
msql, muttrc, nasm, nosyntax, nroff, objc, ocaml, pascal, pcap,
perl, php3, phtml, pike, pmfile, po, pod, postscr, pov, procmail,
prolog, purifylog, python, rc, rexx, sather, scheme, scripts, sdl,
sgml, sh, sicad, simula, skill, slang, slrnrc, slrnsc, sm, spec,
sql, st, syntax, tags, tcl, tex, tf, tsalt, uil, verilog, vgrindefs,
vhdl, vim, viminfo, vrml, whitespace, xdefaults, xmath, xml, xpm,
yacc e zsh.

%description -l de
Der Visual-Editor iMproved ist ein aktualisierter und erweiterter Klon des 
vi-Editors, der mit praktisch allen UN*X-Systemen ausgeliefert wird. 
Er bringt mehrere Fenster, mehrstufige Widerrufen-Funktion, Block-Markierung
und viele weitere Zusatzfunktionen im Vergleich zum Standard-vi-Programm. 

%description -l fr
L'éditeur VIsuel aMélioré est un clone mis à jour et doté de caractéristiques
supplémentaires de l'éditeur « vi » fourni avec pratiquement tous les systèmes
UN*X. Il ajoute les fenêtres mutltiples, l'annulation a plusieurs niveaux, la
mise en évidence des blocs et autres caractéristiques au vi de base.

%description -l tr X11
Bu pakette VIM'in X ortamý ve fare desteði içeren sürümü bulunmaktadýr.
gvim yazarak çalýþtýrabilirsiniz.

%description -l tr
Standart vi metin düzenleyicisinin geliþmiþ hali; daha fazla komut, birden
fazla pencere desteði ve blok iþaretleme yetenekleri içerir.

%prep
%setup -q -b 1
%patch0 -p1 -b .4.2
%patch1 -p1 -b .vim
%patch2 -p1 -b .tutor

%build
cd src

./configure --prefix=/usr --enable-pythoninterp --enable-perlinterp --with-x=yes --enable-gui=athena --exec-prefix=/usr/X11R6
make 
cp vim gvim
make clean

./configure --prefix=/usr --enable-pythoninterp --enable-perlinterp --enable-gui=no --exec-prefix=/usr
make
cp vim enhanced-vim
make clean

./configure --prefix='${DEST}'/usr --with-x=no --disable-pythoninterp --disable-perlinterp --with-tlib=termcap --enable-gui=no --exec-prefix=/
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1,share/vim,X11R6/bin}

cd src
make prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/ install
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/usr/bin
make installmacros DEST=$RPM_BUILD_ROOT
install -s -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim

( cd $RPM_BUILD_ROOT
  mv -f ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/view
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vim ./usr/bin/vi
  ln -sf vim ./usr/bin/ex
  rm -f ./usr/man/man1/rvim.1
  ln -sf vim.1 ./usr/man/man1/vi.1
  ln -sf vim.1 ./usr/man/man1/rvi.1
  ln -sf vim.1 ./usr/man/man1/gvim.1
  ln -sf gvim ./usr/X11R6/bin/vimx
  mkdir -p ./etc/X11/wmconfig
  install -m644 $RPM_SOURCE_DIR/vimx.wmconfig ./etc/X11/wmconfig/gvim
  install -s -m644 $RPM_SOURCE_DIR/vimrc ./usr/share/vim/vimrc
)

gzipman $RPM_BUILD_ROOT/usr/man/

rm -f $RPM_BUILD_ROOT/usr/share/vim/bugreport.vim
rm -f $RPM_BUILD_ROOT/usr/share/vim/menu.vim

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig




tar xvfpz $RPM_SOURCE_DIR/vim-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%doc README*.txt gvimrc_example bugreport.vim macros/README.txt 
%doc menu.vim mswin.vim termcap tools/README.txt tutor vimrc_example

/usr/share/vim/macros
/usr/man/man1/vim.1.gz
/usr/man/man1/ex.1.gz
/usr/man/man1/vi.1.gz
/usr/man/man1/view.1.gz
/usr/man/man1/rvi.1.gz
/usr/man/man1/rview.1.gz
/usr/bin/xxd
/usr/man/man1/xxd.1.gz
%config /usr/share/vim/vimrc

%files help
/usr/share/vim/doc

%files syntax
/usr/share/vim/syntax

%files minimal
%defattr(-,root,root)
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
/usr/bin/vim
/usr/bin/vi
/usr/bin/ex

%files X11
%defattr(-,root,root)
%config(missingok) /etc/X11/wmconfig/gvim
/usr/X11R6/bin/gvim
/usr/X11R6/bin/vimx
/usr/man/man1/gvim.1.gz

%changelog
* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- vimrc: checks if package vim-syntax has been installed to do syntax on

* Wed Jun 30 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- included our vimrc as default config in /usr/share/vim/
- with recent termcap/terminfo fixes, regular vim (mininal and enhanced)
  works in xterm/console in color, so vim-color package removed.
- removed man vim.1 from vim-X11 (already on vim-common)
- compressed man pages

* Wed Dec 10 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- final rebuild for 3.0
- created two more sub-packages: vim-help & vim-syntax
- removed duplicated files (syntas in /usr/doc/ and in /usr/share)

* Tue Oct 27 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- wmconfig translated to pt_BR

* Tue Sep 15 1998 Michael Maher <mike@redhat.com>
- removed '--with-tlib=termcap' so that color-vim works

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.3.

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in Toshio's changes
- color-vim: changed "--disable-p" to "--disable-perlinterp --with-tlib=termcap"
- added minimal rvi/rview and man pages.
- move Obsoletes to same package as executable.

* Thu Aug 06 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Break the package apart similar to the way the netscape package was
  broken down to handle navigator or communicator: The vim package is
  Obsolete, now there is vim-common with all the common files, and a
  package for each binary: vim-minimal (has /bin/vi compiled with no
  frills), vim-enhanced (has /usr/bin/vim with extra perl and python
  interpreters), and vim-X11 (has /usr/X11R6/bin/gvim compiled with
  GUI support.)
- Enable the perl and python interpreters in the gui version (gvim).

* Tue Jun 30 1998 Michael Maher <mike@redhat.com>
- Fixed tutor help.
- cvim package added.  Thanks to Stevie Wills for finding this one :-)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Donnie Barnes <djb@redhat.com>
- added patch to turn off the "vi compatibility" by default.  You can
  still get it via the -C command line option

* Thu Apr 23 1998 Donnie Barnes <djb@redhat.com>
- removed perl and python interpreters (sorry, but those don't belong
  in a /bin/vi and having two vi's seemed like overkill...complain
  to suggest@redhat.com if you care)

* Fri Apr 17 1998 Donnie Barnes <djb@redhat.com>
- fixed buildroot bug

* Sat Apr 11 1998 Donnie Barnes <djb@redhat.com>
- updated from 4.6 to 5.1
- moved to buildroot

* Sun Nov 09 1997 Donnie Barnes <djb@redhat.com>
- fixed missing man page

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry to vim-X11

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- upgraded from 4.5 to 4.6

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- Upgraded to 4.5
- Added ex symlinks

* Tue Mar 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added view symlink.

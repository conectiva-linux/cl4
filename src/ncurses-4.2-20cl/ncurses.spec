Summary: A CRT screen handling and optimization package.
Summary(pt_BR): Biblioteca de controle de terminal curses
Summary(es): Biblioteca de control de terminal curses
Name: ncurses
Version: 4.2
Release: 20cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: ftp://ftp.clark.net/pub/dickey/ncurses/ncurses-4.2.tar.bz2
Source1: ftp://ftp.clark.net/pub/dickey/ncurses/4.2/patch-4.2-990213.sh
Source2: ncurses-linux
Source3: ncurses-linux-m
Source700: ncurses-man-pt_BR.tar
Patch0: ncurses-4.2-arm.patch
Patch1: ncurses-4.2-rh.patch
Patch2: ncurses-4.2-setuid2.patch
Patch3: ncurses-4.2-headercpp.patch
Patch4: ncurses-4.2-fixxterm.patch
BuildRoot: /var/tmp/%{name}-root

%description
The curses library routines are a terminal-independent method of
updating character screens with reasonable optimization.  The
ncurses (new curses) library is a freely distributable replacement
for the discontinued 4.4BSD classic curses library.

%description -l pt_BR
As rotinas da biblioteca curses fornecem ao usuário um método
independente de terminal para atualização das telas de caracteres com
otimização razoável. Essa implementação é "novo curses" (ncurses)
e é o substituto aprovado para os clássicos curses 4.4BSD, que
estão se tornando obsoletos.

%description -l es
Las rutinas de la biblioteca curses ofrecen al usuario un método
independiente de terminal para actualización de las pantallas
de caracteres con optimización razonable. Este soporte es "nuevo
curses" (ncurses) y es el substituto aprobado para los clásicos
curses 4.4BSD, que se quedaban desfasados.

%package devel
Summary: The development files for applications which use ncurses.
Summary(pt_BR): Bibliotecas de desenvolvimento para ncurses
Summary(es): Bibliotecas de desarrollo para ncurses
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: ncurses = %{PACKAGE_VERSION}

%description devel
The header files and libraries for developing applications that use
the ncurses CRT screen handling and optimization package.

Install the ncurses-devel package if you want to develop applications
which will use ncurses.

%description -l pt_BR devel
Este pacote inclui as bibliotecas e arquivos de inclusão necessários
ao desenvolvimento de aplicações que usam ncurses.

%description -l es devel
Este paquete incluye las bibliotecas y archivos de inclusión
necesarios al desarrollo de aplicaciones que usan ncurses.

%prep
%setup -q
sh %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .fixxterm
find . -name "*.orig" -exec rm -f {} \;

%build
CFLAGS="$RPM_OPT_FLAGS -DPURE_TERMINFO" ./configure \
	--prefix=/usr --with-install-prefix=$RPM_BUILD_ROOT \
	--with-normal --with-shared --with-debug --with-profile \
	--without-cxx --without-ada $RPM_ARCH-conectiva-linux
make

%install
rm -rf $RPM_BUILD_ROOT
make install includedir=/usr/include/ncurses
ln -s ../l/linux $RPM_BUILD_ROOT/usr/share/terminfo/c/console
ln -s ncurses/curses.h $RPM_BUILD_ROOT/usr/include/ncurses.h
for I in curses unctrl eti form menu panel term; do
	ln -sf ncurses/$I.h $RPM_BUILD_ROOT/usr/include/$I.h
done
%ifarch sparc
install -m644 %SOURCE2 $RPM_BUILD_ROOT/usr/share/terminfo/l/linux
install -m644 %SOURCE3 $RPM_BUILD_ROOT/usr/share/terminfo/l/linux-m
%endif
strip $RPM_BUILD_ROOT/usr/bin/* || :
strip $RPM_BUILD_ROOT/usr/doc/ncurses-devel-4.2/test/* || :


gzip -9f $RPM_BUILD_ROOT/usr/man/man*/*




mkdir -p $RPM_BUILD_ROOT/usr/man/pt_BR/
tar xvf $RPM_SOURCE_DIR/ncurses-man-pt_BR.tar -C $RPM_BUILD_ROOT/usr/man/pt_BR/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README ANNOUNCE
%attr(755,root,root) /usr/lib/lib*.so.*
/usr/share/terminfo
/usr/share/tabset
/usr/bin/*
/usr/man/man1/*
/usr/man/man5/*
/usr/man/man7/*
%attr(0644,root,root) /usr/man/pt_BR/man*/*

%files devel
%defattr(-,root,root)
%doc c++ test
/usr/lib/lib*.so
/usr/lib/lib*.a
/usr/include/ncurses/*.h
/usr/include/*.h
/usr/man/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jun 27 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- redone fixxterm patch with khome=\E[7~ and kend=\E[8~ in tunne
  with our app-defaults/XTerm
- recompressed source; compressed man pages

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- make sure ALL binaries are stripped (incl. test binaries)

* Thu Mar 25 1999 Preston Brown <pbrown@redhat.com>
- made xterm terminfo stuff MUCH better.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 16)

* Sat Mar 13 1999 Cristian Gafton <gafton@redhat.com>
- fixed header for C++ compiles

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- add terminfo entries for linux/linux-m on sparc (obsolete termfile_sparc).

* Thu Feb 18 1999 Cristian Gafton <gafton@redhat.com>
- updated patchset from original site

* Thu Dec 03 1998 Cristian Gafton <gafton@redhat.com>
- don't build the C++ demo code
- update patch set to the current as of today (redid all the individual
  patches in a single one)

* Wed Oct 14 1998 Cristian Gafton <gafton@redhat.com>
- make sure to strip the binaries

* Wed Sep 23 1998 Cristian Gafton <gafton@redhat.com>
- added another zillion of patches. The spec file *is* ugly
- defattr

* Mon Jul 20 1998 Cristian Gafton <gafton@redhat.com>
- added lots of patches. This spec file is starting to look ugly

* Wed Jul 01 1998 Alan Cox <alan@redhat.com>
- Fix setuid trusting. Open termcap/info files as the real user.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- added terminfo entry for the poor guys using lat1 and/or lat-2 on their
  consoles... Enjoy linux-lat ! Thanks, Erik !

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- new patch to get xterm-color and nxterm terminfo entries
- aliased them to rxvt, as that seems to satisfy everybody

* Sun Apr 12 1998 Cristian Gafton <gafton@redhat.com>
- added %clean section

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- removed /usr/lib/terminfo symlink - we shouldn't need that

* Mon Apr 06 1998 Cristian Gafton <gafton@redhat.com>
- updated to 4.2 + patches
- added BuildRoot

* Sat Apr 04 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt with egcs on alpha

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- version 7 didn't rebuild properly on the Alpha somehow -- no real changes
  are in this version

* Tue Dec 09 1997 Erik Troan <ewt@redhat.com>
- TIOCGWINSZ wasn't used properly

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, linked shared libs against -lc

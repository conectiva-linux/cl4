Summary: curses terminal control library
Summary(pt_BR): Biblioteca de controle de terminal curses
Summary(es): Biblioteca de control de terminal curses
Name: ncurses3
Version: 1.9.9e
Release: 12cl
# was .gz
Source: sunsite.unc.edu:/pub/Linux/libs/ncurses-1.9.9e.tar.bz2
Patch0: ncurses-1.9.9e-nohome.patch
Patch1: ncurses-1.9.9e-shared.patch
Patch2: ncurses-1.9.9e-winsize.patch
Patch3: ncurses-1.9.9e-rh.patch
Patch4: ncurses-1.9.9e-share.patch
Patch5: ncurses-1.9.9e-setuid.patch
Patch6: ncurses-1.9.9e-winsz.patch
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Buildroot: /var/tmp/ncurses3-root
Conflicts: slang < 0.99.38-4
Summary(de): curses-Terminal-Control-Library
Summary(fr): La bibliothéque de contrôle de terminal curses.
Summary(tr): Terminal kontrol kitaplýðý

%description
The curses library routines give the user a terminal-independent method of
updating character screens with reasonable optimization.  This
implementation is ``new curses'' (ncurses) and is the approved replacement
for 4.4BSD classic curses, which is being discontinued. 

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

%description -l de
Die curses-Library-Routinen geben dem Benutzer eine Terminal-unabhängige 
Methode zur optimierten Aktualisierung von zeichenbasierenden 
Bildschirminhalten an die Hand. Die vorliegende Implementierung ist NEW 
CURSES (ncurses), die offizielle Nachfolgerversion für 4.4BSC (die 
klassische curses-Version), welche nicht weitergeführt wird. 

%description -l fr
Les routines de la bibliothèque curses donnent à l'utilisateur une méthode
indépendante du terminal pour la mise à jour des écrans en mode texte avec une
optimisation correcte. Ceci est l'implantation du « nouveau curses » (ncurses)
et est le remplacement du curses 4.4BSD classique qui est abandonné.

%description -l tr
curses kitaplýðý ile kullanýcýya kullanýlan terminal tipinden baðýmsýz olarak
karakter tabanlý ekranlara eriþim olanaðý saðlanabilmektedir. Bu uyarlama
'new curses' (ncurses), BSD deki klasik curses'in geliþmiþ halidir.

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Thu Aug 13 1998 Cristian Gafton <gafton@redhat.com>
- remove testing for TIOCGWINSZ on console; we know we are okay (this used
  to break ncurses when run through the build system)

* Wed Jul 01 1998 Alan Cox <alan@redhat.com>
- open TERMINFO/TERMCAP files as real user if setuid

* Tue May 05 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Tue May 05 1998 Cristian Gafton <gafton@redhat.com>
- conflicts with older versions of slang

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- don't use the share patch for now; it's broken

* Mon Apr 20 1998 Cristian Gafton <gafton@redhat.com>
- package renamed to ncurses3 and we keep only the runtime libs

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- version 7 didn't rebuild properly on the Alpha somehow -- no real changes
  are in this version

* Tue Dec 09 1997 Erik Troan <ewt@redhat.com>
- TIOCGWINSZ wasn't used properly

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, linked shared libs against -lc

%prep
%setup -q -n ncurses-1.9.9e
%patch0 -p1 -b .nohome
%patch1 -p1 -b .shared
# we need to always include <sys/ioctl.h> on glibc, or TIOCGWINSZ doesn't
# get defined
%patch2 -p1 -b .winsize
%patch3 -p1 -b .rh
#%patch4 -p1 -b .share
%patch5 -p1 -b .share
%patch6 -p1 -b .winsz

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS -DPURE_TERMINFO" ./configure --prefix=/usr \
	--with-normal --with-shared  --with-datadir=/usr/share/terminfo
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	includedir=$RPM_BUILD_ROOT/usr/include/ncurses \
	datadir=$RPM_BUILD_ROOT/usr/share/terminfo

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
/usr/lib/lib*.so.*

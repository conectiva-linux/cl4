Summary: A library of Python code used by various Red Hat Linux programs.
Summary(pt_BR): Biblioteca de código python usada por vários programas Red Hat
Summary(es): Biblioteca de código python usada por varios programas Red Hat
Name: pythonlib
Version: 1.22
Release: 5cl
Copyright: GPL
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source: pythonlib-1.22.tar.gz
Patch0: pythonlib-Conf.patch 
Patch1: pythonlib-makefile.patch 
Requires: python
BuildArchitectures: noarch
BuildRoot: /var/tmp/pythonlib-root

%description
The pythonlib package contains Python code used by a variety of
Red Hat Linux programs.  Pythonlib includes code needed for
multifield listboxes and entry widgets with non-standard keybindings,
among other things.

%description -l pt_BR
Este pacote contém o código usado por uma variedade de programas
Red Hat.  Inclui código para caixas de listas multicampo e widgets de
entrada de dados com associações de teclas não padrão, entre outros.

%description -l es
Este paquete contiene el código usado por una variedad de programas
Red Hat.  Incluye código para cajas de listas multicampo y widgets de
entrada de datos con asociaciones de teclas no padrón, entre otros.

%prep
%setup -q
%patch -p1 -b .kernelcfg
%patch1 -p1

%build

%install
make install LIBDIR=$RPM_BUILD_ROOT/usr/lib/rhs/python/

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/rhs/python

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Fri May 21 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Mon Mar 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0, incorportated changes, changed spec file.

* Thu Feb 11 1999 Peter Hanecak <hanecak@megaloman.sk>
- updated to build as non-root user

* Fri Jul 10 1998 Michael Maher <mike@redhat.com> 
- patched Conf.py so that kernelcfg works.
- added Buildroot.

* Fri Nov 07 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added some stuff to deal with -k

* Tue Nov 04 1997 Michael K. Johnson <johnsonm@redhat.com>
- do not require tkinter; apps that explicitly use tkinter through
- pythonlib should require tkinter themselves.

* Mon Nov 03 1997 Michael K. Johnson <johnsonm@redhat.com>
- require tkinter

* Fri Oct 31 1997 Michael K. Johnson <johnsonm@redhat.com>
- ConfFstab for cabaret

* Mon Sep 29 1997 Michael K. Johnson <johnsonm@redhat.com>

Major changes for new version of netcfg.
- Clone files keep differences in some way appropriate to the type of file.
- RCS management of almost all files (all but password-type files) -- just
  create a subdirectory called RCS in any directory where you want to
  monitor changes made by control-panel tools that use pythonlib.  That
  can also be a symlink, but watch for filename conflicts.
- Smart chatfile handling that knows something about the contents of a
  chatfile.
- Far better algorithm for finding free user and group ids: first do the
  old sparse search, then if that fails, search for first free id.  This
  algorithm is used for both user and group ids.
- EntryBox class is a toplevel that provides a single entry in a modal manner.

Also made it a noarch package.

* Mon Aug 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added fix for shadow files.  (Not a CVS branch; change made in master as well)

* Mon Jun 02 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added proper error raising and error-on-missing files for kernelcfg.

* Mon Apr 21 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fields terminated only by separator or end of line.

* Fri Mar 28 1997 Michael K. Johnson <johnsonm@redhat.com>
- Fixed quoted ampersand in ConfShellVar

* Wed Mar 12 1997 Michael K. Johnson <johnsonm@redhat.com>

Fixed quoted equals in ConfShellVar

* Wed Mar 05 1997 Michael K. Johnson <johnsonm@redhat.com>

Changed to /etc/ppp/pap-secrets

* Wed Feb 26 1997 Michael K. Johnson <johnsonm@redhat.com>

Added class for managing /etc/pap-secrets.
Improved class for managing /etc/sysconfig/static-routes

Summary: Fonts for the GhostScript interpreter
Summary(pt_BR): Fontes para o interpretador GhostScript
Summary(es): Fuentes para el interpretador GhostScript
Name: ghostscript-fonts
Version: 5.10
Release: 6cl
License: GPL
Icon: ghost.gif
Group: Applications/Publishing
Group(pt_BR): Aplicações/Editoração
Group(es): Aplicaciones/Editoración
BuildRoot: /var/tmp/gsfonts-root
# was .gz
Source: prep.ai.mit.edu:/pub/gnu/ghostscript-fonts-other-5.10.tar.bz2
Requires: ghostscript
BuildArchitectures: noarch

%description
These fonts can be used by the GhostScript interpreter during text
rendering. They are in addition to the shared fonts between GhostScript 
and X11.

%description -l pt_BR
Estas fontes podem ser usadas pelo interpretador GhostScript durante
renderizações de textos.

%description -l es
Estas fuentes pueden ser usadas por el interpretador GhostScript
al tiempo que se realiza el render de textos.

%prep
%setup -q -c ghostscript-fonts-5.10

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/fonts/default/ghostscript
cp * $RPM_BUILD_ROOT/usr/share/fonts/default/ghostscript

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/fonts/default/ghostscript

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 18 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Feb  1 1999 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- renamed package to be consistent with new ghostscript.

* Fri Nov 13 1998 Preston Brown <pbrown@redhat.com>
- removed the std fonts...now shared between X11 and gs with URW fonts pkg.

* Thu Jul  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 4.03.

* Mon May 04 1998 Erik Troan <ewt@redhat.com>
- set the owner and group of all of the files to 0.0

* Tue Sep 23 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

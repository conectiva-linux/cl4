Summary: GNU patch Utilities
Summary(pt_BR): Utilitários de patch (atualização) da GNU
Summary(es): Utilitarios de patch (actualización) de la GNU
Name: patch
Version: 2.5.3
Release: 5cl
Copyright: GPL
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
# was .gz
Source: ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.bz2
Buildroot: /tmp/%{name}-%{version}-root
%description
Patch is a program to aid in patching programs.  :-)
You can use it to apply 'diff's.  Basically, you can use
diff to note the changes in a file, send the changes to
someone who has the original file, and they can use 'patch'
to combine your changes to their original.

%description -l pt_BR
Patch é um programa para ajudar a reparar (patching) programas. Você
pode usá-lo para aplicar "diff's". Basicamente, você pode usar diff
para anotar mudanças em um arquivo, mandar as mudanças a alguém que
possui o arquivo original, e eles podem usar "patch" para combinar
suas mudanças ao original deles.

%description -l es
Patch es un programa para ayudar a reparar (patching)
programas. Puedes usarlo para aplicar "diff's". Básicamente, puedes
usar diff para anotar cambios en un archivo, mandar los cambios a
alguien que posee el archivo original, y estos pueden usar "patch"
para combinar sus cambios a su original.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}
install -s patch $RPM_BUILD_ROOT/usr/bin
install patch.man $RPM_BUILD_ROOT/usr/man/man1/patch.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS README AUTHORS ChangeLog
%attr(755, root, root) /usr/bin/patch
%attr(644, root,  man) /usr/man/man1/patch.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sun May 17 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- AUTHORS, ChangeLog added to %doc,
- added -q %setup parameter,
- spec file rewrited for using Buildroot,
- added %clean section,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

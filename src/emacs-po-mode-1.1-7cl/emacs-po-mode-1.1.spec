Name: emacs-po-mode
Version: 1.1 
Release: 7cl
Source: po-mode.tgz
Patch: po-mode.el.patch
Copyright: GPL
Group: Applications/Editors
Group(pt_BR): Aplicações/Editores
Group(es): Aplicaciones/Editores
BuildRoot: /var/tmp/po-mode
Requires: emacs
BuildArchitectures: noarch
Summary: For helping GNU gettext lovers to edit PO files with emacs
Summary(pt_BR): Facilita a edição de arquivos PO (internacionalização) com o emacs
Summary(es): Facilita la edición de archivos PO (internacionalización) con emacs

%description
This package provides the tools meant to help editing PO files,
as documented in the GNU gettext user's manual.  See this manual
for user documentation, which is not repeated here.

%description -l pt_BR
Este pacote provê as ferramentas para ajudar na edição de arquivos
PO, como documentado no manual do usuário do GNU gettext. Veja este
manual para a documentação de uso, a qual não é incluída aqui.

%description -l es
Este paquete suministra las herramientas para ayudar en la edición
de archivos PO, como documentado en el manual del usuario del
GNU gettext.  Mira este manual para la documentación de uso, que
no se incluye aquí.

%prep

%setup -n po-mode
%patch -p1

%build

%install

mkdir -p $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/
cp po-mode.el $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README LEIAME THANKS ChangeLog
/usr/share/emacs/site-lisp/po-mode.el

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Fri Dec 11 1998 Conectiva <dist@conectiva.com>
 final rebuild for 3.0

# Note that this is NOT a relocatable package
%define ver      0.1.1b
%define rel      2cl
%define prefix   /usr

Summary: Spanish verbs conjugator
Summary(pt_BR): Conjugador de verbos em espanhol
Summary(es): Conjugador de verbos en español
Name: gnomecompjugador
Version: %ver
Release: %rel
Copyright: GPL
Group: Applications/Productivity
Group(pt_BR): Aplicações/Produtividade
Group(es): Aplicaciones/Productividad
# was .gz
Source0: gnomecompjugador.tar.bz2
Source1: gnomecompjugador.desktop
BuildRoot: /var/tmp/gnomecompjuga
URL: http://aries27.uwaterloo.ca/~dmg/comp-jugador/

%description
Comp-jugador is a Spanish verbs conjugator. It is able to conjugate
all the verbs in the official Spanish language (as in the Diccionario
de la Real Academia). It contains close to 10,000 verbs.

%description -l pt_BR
Conjugador de verbos em espanhol. É capaz de conjugar todos os
verbos do idioma espanhol oficial (conforme o Dicionário da Academia
Real). Contém aproximadamente 10.000 verbos.

%description -l es
Comp-jugador es un conjugador de verbos en español. Puede conjugar todos
los verbos en el lenguaje español oficial (como en el Diccionario
de la Real Academia). Contiene cerca de 10.000 verbos.

%prep
%setup -q

export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
unset LINGUAS
if [ -x ./configure ] ; then
  ./configure --prefix=%{prefix}
else
  ./autogen.sh --prefix=%{prefix}
fi

%build
./configure --prefix=%{prefix}
make

%install
make install prefix=$RPM_BUILD_ROOT/%{prefix}
mkdir -p $RPM_BUILD_ROOT/%{prefix}/share/gnome/apps/Applications/
install -m 644 $RPM_SOURCE_DIR/gnomecompjugador.desktop $RPM_BUILD_ROOT/%{prefix}/share/gnome/apps/Applications/

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{prefix}/share/gnome/gnomecompjugador
%{prefix}/share/gnome/gnomecompjugador/comp-jugador.gdbm
%{prefix}/bin/gnomecompjugador
%{prefix}/share/gnome/apps/Applications/gnomecompjugador.desktop
%doc ANNOUNCE AUTHORS ChangeLog Comp-jugador README NEWS TODO

%changelog
* Fri Jun 11 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 05 1999 Conectiva <dist@conectiva.com>
- initial package


%define ver 0.9.36
%define prefix /usr/X11R6

Summary: X11 Window Manager
Summary(pt_BR): Gerenciador de Janelas X11
Summary(es): Administrador de Ventanas X11
Name: icewm 
Version: %ver
Release: 5cl
Copyright: LGPL
Group: User Interface/Desktops
Group(pt_BR): Interface do Usuário/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
# was .gz
Source: icewm-%ver.src.tar.bz2
URL: http://www.kiss.uni-lj.si/~k4fr0235/icewm/
BuildRoot: /tmp/build-icewm-%ver

%description
Window Manager for X Window System. Can emulate the look of Windows'95,
OS/2 Warp 3,4, Motif. Tries to take the best features of the above systems.
Features multiple workspaces, opaque move/resize, task bar, window list,
mailbox status, digital clock. Fast and small.

%description -l pt_BR
Gerenciador de Janelas para o X Window. Pode emular a aparência
do Windows'95, OS/2 Warp 3 e 4 e o Motif. Tenta usar as melhores
características dos sistemas citados. Características: vários
ambientes de trabalho, movimentação/redimensionamento opaco,
barra de tarefas, lista de janelas, status da caixa de entrada do
correio e relógio digital. É rápido e pequeno.

%description -l es
Administrador de Ventanas para el X Window. Puede emular la
apariencia del Windows'95, OS/2 Warp 3 y 4 y el Motif. Intenta usar
las mejores características de los sistemas citados. Características:
varios ambientes de trabajo, movimiento/ redimensionamiento opaco,
barra de tareas, lista de ventanas, estado de la caja de entrada
del correo y reloj digital. Rápido y pequeño.

%prep

%setup

%build
unset LINGUAS
export CC=egcs
export CXX=egcs
./config --with-i18n --with-imlib --with-gnome 
make PREFIX=%{prefix}

%install
make PREFIX=$RPM_BUILD_ROOT%{prefix} ETCDIR=$RPM_BUILD_ROOT/etc/X11/icewm install

#%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING CHANGES TODO BUGS icewm.lsm FAQ doc/*.html doc/icewm.sgml
%{prefix}/lib/X11/icewm/
%{prefix}/bin/icewm
%{prefix}/bin/icewmhint
%{prefix}/bin/icewmbg

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Mar 25 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated to 0.9.36

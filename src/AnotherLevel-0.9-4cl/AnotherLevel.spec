Summary: A customized configuration of the fvwm2 window manager.
Summary(pt_BR): Arquivos de configura��o de Desktop
Summary(es): Archivos de configuraci�n de Desktop
Name: AnotherLevel
Version: 0.9
Release: 4cl
Copyright: distributable
Group: User Interface/Desktops
Group(pt_BR): Interface do Usu�rio/Ambientes de Trabalho
Group(es): Interfaz del Usuario/Tablero del escritorio
Source: AnotherLevel-0.9.tar.gz
Requires: m4, fvwm2, wmpixmaps, wmconfig > 0.3
BuildArchitectures: noarch
BuildRoot: /var/tmp/AnotherLevel-root
Obsoletes: TheNextLevel

%description 
AnotherLevel is a custom configuration of the popular fvwm2
window manager. Fvwm stands for (?) virtual window manager.
You can fill in the blank for the 'f': fast, flexible, 
friendly and fabulous all could apply. This window manager
is based on TheNextLevel desktop configuration, created
by Greg J. Badros, which won the 1996 Red Hat Desktop 
Contest.

AnotherLevel is designed to be easily configured by the 
user.

%description -l pt_BR
AnotherLevel � a pr�xima vers�o do TheNextLevel.  O desktop
TheNextLevel foi criado por Greg J. Badros e foi o vencedor
do Concurso de Desktop feito pela Red Hat em 1996. Ele tem uma
poderosa e atrativa configura��o para o fvwm que funciona com
o fvwm2. Esta vers�o teve muitas transforma��es, assim n�s a
chamamos AnotherLevel. Alguma documenta��o est� dispon�vel em
/usr/doc/AnotherLevel em formato html.

Este desktop � facilmente configurado. Muitos atributos podem
ser redefinidos, simplesmente copiando o
/etc/X11/AnotherLevel/fvwm2rc.defines para o diret�rio do usu�rio
como .fvwm2rc.defines e modificando-se este arquivo apropriadamente.

%description -l es
AnotherLevel es la pr�xima versi�n del TheNextLevel.  desktop
TheNextLevel fue creado por Greg J. Badros y fue el vencedor
del Concurso de Desktop hecho por la Red Hat en 1996. Tiene
una eficaz y atractiva configuraci�n para fvwm que funciona con
fvwm2. Esta versi�n ha tenido muchas transformaciones, as� nosotros
la llamamos AnotherLevel. Alguna documentaci�n est� disponible
en /usr/doc/AnotherLevel en formato html.  Este desktop
se configura f�cilmente. Muchos atributos pueden ser redefinidos,
simplemente copiando el /etc/X11/AnotherLevel/fvwm2rc.defines
para el directorio del usuario como .fvwm2rc.defines y modificando
este archivo apropiadamente.

%prep
%setup -c -q

%build
echo "No build necessary"

%install
TOPDIR=$RPM_BUILD_ROOT make install
mkdir -p $RPM_BUILD_ROOT/etc/X11/TheNextLevel
ln -sf ../AnotherLevel/fvwm2rc.m4 \
	$RPM_BUILD_ROOT/etc/X11/TheNextLevel/.fvwm2rc.m4

mkdir -p $RPM_BUILD_ROOT/etc/X11/gdm/Sessions
install -m 755 AnotherLevel.session \
	$RPM_BUILD_ROOT/etc/X11/gdm/Sessions/AnotherLevel

%files
%defattr(-,root,root)
%doc Sample.Xmodmap
%dir /etc/X11/AnotherLevel
%config /etc/X11/AnotherLevel/*
/etc/X11/TheNextLevel
/etc/X11/gdm/Sessions/AnotherLevel
/usr/share/icons/*.xpm
/usr/share/icons/mini/*.xpm
/usr/man/*/*
/usr/X11R6/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

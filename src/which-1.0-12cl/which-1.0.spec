Summary: Finds a program 'which' is in one of the directories on your PATH
Summary(pt_BR): Localiza um programa que est� em um dos diret�rios de seu PATH. Mostra rota completa.
Summary(es): Localiza un programa que est� en uno de los directorios de su PATH. Ense�a ruta completa.
Name: which
Version: 1.0
Release: 12cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplica��es/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/a/bin/which.tar.gz
Prefix: /usr
Buildroot: /var/tmp/which-root
Summary(de): Findet ein Programm in einem der Verzeichnisse in Ihrem PATH
Summary(fr): Recherche un programme dans l'un des r�pertoires de votre PATH.
Summary(tr): PATH'de bulunan bir dosyan�n yerini bulmay� sa�layan bir ara�

%changelog
* Thu May 27 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 22 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%description
Give it a program name, and it tells you if it is on your 'PATH'.

For example, 'which ls' would print '/bin/ls', because the ls program,
which is in one of the directories listed in your PATH environment
variable, is located in the /bin directory.

%description -l pt_BR
D� a ele um nome de programa, e ele lhe dir� se est� no seu 'PATH'.
Por exemplo, 'which ls' poderia imprimir '/bin/ls', porque o programa
ls, que est� em um dos diret�rios listados na vari�vel de ambiente
PATH, est� localizado no diret�rio /bin.

%description -l es
Tu le das un nombre de programa, y el te dir� si est� en su 'PATH'.
Por ejemplo, 'which ls' podr�a imprimir '/bin/ls', porque el programa
ls, que est� en uno de los directorios listados en la variable de
ambiente PATH, est� localizado en el directorio /bin.

%description -l de
Geben Sie ihm einen Programmnamen, und es sagt Ihnen, ob sich
dieser in Ihrem PATH befindet. 

Beispielsweise w�rde 'which ls' das Ergebnis '/bin/ls' liefern, weil
sich das ls-Programm, das in einem der Verzeichnisse in Ihrer
PATH-Umgebungsvariable abgelegt ist, sich im /bin-Verzeichnis
befindet.

%description -l fr
Donnez lui un nom de programme, et il vous dit s'il est dans votre 'PATH'.

Par exemple 'which ls' afficherait '/bin/ls', car le programme ls, qui
se trouve dans un des r�pertoires list�es dans votre variable d'environnement
PATH, est situ� dans le r�pertoire /bin/.

%description -l tr
which bir komut veya program�n PATH'inizde bulunup bulunmad���n� belirtir.

%prep
%setup -n which

%build
make DESTDIR=/usr/bin

%install
mkdir -p $RPM_BUILD_ROOT/usr/man/man1 $RPM_BUILD_ROOT/usr/bin
mkdir blah
cp -f Makefile blah
install -c -m 0444 which.1 $RPM_BUILD_ROOT/usr/man/man1/which.1
install -c -s -m 0755 which $RPM_BUILD_ROOT/usr/bin/which

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Makefile which.c blah
/usr/bin/which
/usr/man/man1/which.1

Summary: Finds a program 'which' is in one of the directories on your PATH
Summary(pt_BR): Localiza um programa que está em um dos diretórios de seu PATH. Mostra rota completa.
Summary(es): Localiza un programa que está en uno de los directorios de su PATH. Enseña ruta completa.
Name: which
Version: 1.0
Release: 12cl
Copyright: distributable
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
Source: ftp://sunsite.unc.edu/pub/Linux/distributions/slackware/source/a/bin/which.tar.gz
Prefix: /usr
Buildroot: /var/tmp/which-root
Summary(de): Findet ein Programm in einem der Verzeichnisse in Ihrem PATH
Summary(fr): Recherche un programme dans l'un des répertoires de votre PATH.
Summary(tr): PATH'de bulunan bir dosyanýn yerini bulmayý saðlayan bir araç

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
Dê a ele um nome de programa, e ele lhe dirá se está no seu 'PATH'.
Por exemplo, 'which ls' poderia imprimir '/bin/ls', porque o programa
ls, que está em um dos diretórios listados na variável de ambiente
PATH, está localizado no diretório /bin.

%description -l es
Tu le das un nombre de programa, y el te dirá si está en su 'PATH'.
Por ejemplo, 'which ls' podría imprimir '/bin/ls', porque el programa
ls, que está en uno de los directorios listados en la variable de
ambiente PATH, está localizado en el directorio /bin.

%description -l de
Geben Sie ihm einen Programmnamen, und es sagt Ihnen, ob sich
dieser in Ihrem PATH befindet. 

Beispielsweise würde 'which ls' das Ergebnis '/bin/ls' liefern, weil
sich das ls-Programm, das in einem der Verzeichnisse in Ihrer
PATH-Umgebungsvariable abgelegt ist, sich im /bin-Verzeichnis
befindet.

%description -l fr
Donnez lui un nom de programme, et il vous dit s'il est dans votre 'PATH'.

Par exemple 'which ls' afficherait '/bin/ls', car le programme ls, qui
se trouve dans un des répertoires listées dans votre variable d'environnement
PATH, est situé dans le répertoire /bin/.

%description -l tr
which bir komut veya programýn PATH'inizde bulunup bulunmadýðýný belirtir.

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

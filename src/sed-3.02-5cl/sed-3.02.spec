Summary: GNU Stream Editor
Summary(pt_BR): Editor de stream da GNU
Summary(es): Editor de stream de la GNU
Name: sed
Version: 3.02
Release: 5cl
Copyright: GPL
Group: Applications/Text
Group(pt_BR): Aplicações/Texto
Group(es): Aplicaciones/Texto
# was .gz
Source0: ftp://prep.ai.mit.edu/pub/gnu/sed-%{version}.tar.bz2
Prereq: info
Buildroot: /var/tmp/sed-root
Summary(de): GNU Stream Editor
Summary(fr): Éditeur de flot de GNU
Summary(tr): GNU dosya iþleme aracý

%description
Sed copies the named files (standard input default) to the standard output, 
edited according to a script of commands.

%description -l pt_BR
Sed copia os arquivos nomeados (arquivos da entrada padrão por
default) para a saída padrão, editado de acordo com um script
de comandos.

%description -l es
Sed copia los archivos nombrados (archivos de la entrada padrón por
por defecto) para la salida padrón, editado de acuerdo con un script
de comandos.

%description -l de
Sed kopiert die genannten Dateien (Standardeingabe-Einstellung) nach
Bearbeitung anhand eines Befehlsskripts auf die Standardausgabe.  

%description -l fr
sed copie les fichiers indiqués (l'entrée standard par défaut), modifiés en 
fonction d'un script de commandes, vers la sortie standard.

%description -l tr
Sed, belirtilen dosyalarý, verilen komutlara göre iþleyerek standart çýktýya
kopyalar. Genellikle, metin dosyalarýnda bir katarýn yerine baþka bir katar
yazmakta kullanýlýr.

%prep
%setup -q

%build

./configure --prefix=/usr --exec-prefix=/usr

make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr exec_prefix=$RPM_BUILD_ROOT/usr install

( cd $RPM_BUILD_ROOT
  mkdir bin
  mv usr/bin/sed bin/sed
  rmdir usr/bin
  gzip -9nf usr/info/sed.info*
  rm -f usr/info/dir
)

%post
/sbin/install-info /usr/info/sed.info.gz /usr/info/dir

%preun
if [ $1 = 0 ]; then
   /sbin/install-info --delete /usr/info/sed.info.gz /usr/info/dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ANNOUNCE BUGS NEWS README TODO
/bin/sed 
/usr/info/sed.info*
/usr/man/man1/sed.1

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed May 26 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.02

* Sun Jul 26 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.01

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- removed references to the -g option from the man page that we add

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups
- added BuildRoot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

Summary: ELF object file access library
Summary(pt_BR): Biblioteca para acesso a arquivos objeto ELF
Summary(es): Biblioteca para acceso a archivos objeto ELF
Name: libelf
Version: 0.6.4
Release: 5cl
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Excludearch: alpha
Source: ftp://ftp.ocslink.com/pub/systems/linux/libs/libelf-0.6.4.tar.gz
Buildroot: /var/tmp/libelf-root
Summary(de): Objektdateizugriffs-Library ELF
Summary(fr): Librairie d'acc�s au fichiers objets ELF.
Summary(tr): ELF ara kod eri�im kitapl���

%description
This library gives you access to the internals of the ELF object
file format.  It lets you poke around in the various different
sections of an ELF file, check out the symbols, etc.

%description -l pt_BR
Esta biblioteca fornece acesso a dados internos do formato de arquivo
objeto ELF. Ele permite visualizar v�rias se��es diferentes de um
arquivo ELF, observar os s�mbolos, etc.

%description -l es
Esta biblioteca ofrece acceso a datos internos del formato de
archivo objeto ELF. Permite visualizar varias secciones diferentes
de un archivo ELF, observar los s�mbolos, etc.

%description -l de
Diese Library gibt Ihnen Zugang zum Inneren des ELF-Objekt-
Dateiformats. Sie k�nnen damit in den verschiedenen Teilen 
einer ELF-Datei umherstochern, die Symbole �berpr�fen und �hnliches. 

%description -l fr
Cette biblioth�que donne acc�s aux donn�es internes du format
de fichier objet ELF. Elle permet de se d�placer dans les
diff�rentes parties d'un fichier ELF, de v�rifier les symboles, etc.

%description -l tr
Bu kitapl�k, ELF ara kod dosyas� i�eri�ine eri�imi sa�lar. ELF dosyalar�n�n
�e�itli yerleri ile oynama, sembolleri kontrol etme gibi olanaklar sunar.

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Oct 24 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Fri May 01 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr


* Fri Oct 31 1997 Michael K. Johnson <johnsonm@redhat.com>

- upgraded to 0.6.4
- buildroot

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure
make

%install
make install prefix=$RPM_BUILD_ROOT/usr

%files
%doc README
/usr/lib/libelf.a
/usr/include/libelf/*

Summary: XM, MOD, MTM, S3M, STM, ULT, IT and UNI module player
Summary(pt_BR): Reprodutor de arquivos de som XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Summary(es): Reproductor de archivos de sonido XM, MOD, MTM, S3M, STM, ULT, IT e UNI
Name: mikmod
Version: 3.0.3
Release: 6cl
Copyright: Distributable
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
# was .gz
Source: ftp://sunsite.unc.edu/pub/Linux/apps/sound/players/mikmod-3.0.3.tar.bz2
Source1: mikmod.wmconfig
Source800: mikmod-wmconfig.i18n.tgz
Patch0: alpha.patch
Url: http://www.freenet.tlh.fl.us/~amstpi/mikmod.html
Obsoletes: tracker
Buildroot: /var/tmp/mikmod-tmp

%description

One of the best and most well known MOD players around (for unix).
Play MOD (and their brethren) songs.  

 MikMod is a portable modules player originally written by
 Jean-Paul Mikkers (MikMak) for DOS. It has 
 subsequently been hacked by many hands and now runs on 
 many platforms, this particular distribution intended
 to compile fairly painlessly in a Unix (Linux) environment.
 It uses the OSS /dev/dsp driver including in all recent 
 kernels for output, and will also write wav files. 
 Supported file formats include mod, stm, s3m, mtm, xm,
 and it.  The player uses ncurses for console output and
 supports transparent loading from gzip/pkzip/zoo archives
 and the loading/saving of playlists.


%description -l pt_BR
Um dos melhores e mais conhecido reprodutor de MOD para Unix.
Reproduz músicas em formato MOD.

  O MikMod é um reprodutor portável de módulos originalmente
  escrito por Jean-Paul Mikkers (MikMak) para o DOS. Ele
  foi subseqüentemente modificado por muitas mãos e agora
  roda em muitas plataformas, com esta distribuição 
  projetada para compilar sem problemas em um ambiente
  Unix (Linux).
  Ele usa o driver /dev/dsp OSS incluso em todos os
  kernel recentes para saída e também escreve arquivos wav.
  Os formatos de arquivos suportados incluem: mod, stm, s3m,
  mtm, xm e it. O reprodutor usa ncurses para saída no
  console e suporta carga transparente de arquivos gzip/pkzip/zoo
  e carga/gravação de listas de músicas para reprodução.

%description -l es
Uno de los mejores y más conocido reproductor de MOD para Unix.
Reproduce músicas en formato MOD.  MikMod es un reproductor portátil
de módulos originalmente escrito por Jean-Paul Mikkers (MikMak)
para el DOS. Fue sucesivamente modificado por muchas manos y ahora
se ejecuta en muchas plataformas, con esta distribución proyectada
para compilar sin problemas en un ambiente Unix (Linux).  Usa el
driver /dev/dsp OSS incluso en todos los kernel recientes para
salida y también escribe archivos wav.  Los formatos de archivos
soportados incluyen: mod, stm, s3m, mtm, xm y it. El reproductor
usa ncurses para salida en la pantalla y soporta carga transparente
de archivos gzip/pkzip/zoo y carga/grabación de listas de músicas
para reproducción.

%prep
%setup -q 

%ifarch alpha
%patch0 -p1 -b .orig
%endif 

%build
./build-mikmod.linux.sh

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install -m 755 -s mikmod $RPM_BUILD_ROOT/usr/bin/

#install -m 644 -o root -g root $RPM_SOURCE_DIR/mikmod.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/mikmod

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/



tar xvfpz $RPM_SOURCE_DIR/mikmod-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc docs/* README.UNIX README.TXT license.txt  mikmod-3.0.3.lsm
/usr/bin/mikmod
/etc/X11/wmconfig/mikmod

%changelog
* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Wed Nov 11 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations
- mikmod.wmconfig.pt_BR

* Fri Sep 04 1998 Michael Maher <mike@redhat.com>
- added patch for alpha

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- built package; obsoletes the ancient tracker program.


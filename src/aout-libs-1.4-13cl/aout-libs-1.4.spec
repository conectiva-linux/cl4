Summary: Compability libraries for old a.out applications
Summary(pt_BR): Bibliotecas de compatibilidade para aplica��es a.out
Summary(es): Bibliotecas de compatibilidad para aplicaciones a.out
Name: aout-libs
Version: 1.4
Release: 13cl
Exclusivearch: i386
Exclusiveos: Linux
Copyright: distributable
Group: System Environment/Libraries
Group(pt_BR): Ambiente do Sistema/Bibliotecas
Group(es): Ambiente del Sistema/Bibliotecas
Source0: aout.sources.tar.bz2
Source1: libc-4.7.2.tar.bz2
Autoreqprov: no
Prereq: ldconfig grep fileutils mktemp
Summary(de): Kompatibilit�ts-Libraries f�r alte a.out-Applikationen 
Summary(fr): Biblioth�ques de compatibilit�s pour les anciennes applications a.out"
Summary(tr): Eski a.out uygulamalar� i�in gereken kitapl�klar
BuildRoot: /var/tmp/aout-libs-build/

%changelog
* Wed Jun 30 1999 Guilherme Manika <gwm@conectiva.com>
- Checks if ld.so.conf exists, else create it (cleaner output on installs)
- Hopefully removed a /tmp race from postun
- Now builds in BuildRoot, not on the system itself

* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Thu Dec 10 1998 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- added prereqs for scripts

%description
Old Linux systems used a format for programs and shared libraries called
a.out while newer ones use the ELF format. In order to run old a.out
format programs, you need the a.out format libraries which this package
provide. With it, you are to run most a.out format packages for text,
X, and SVGAlib modes.

%description -l pt_BR
Sistemas Linux antigos usavam um formato para programas e bibliotecas
compartilhadas chamado a.out enquanto os novos sistemas utilizam
o formato ELF. Para rodar programas no velho formato a.out, voc�
precisa das bibliotecas de formato a.out que este pacote oferece. Com
ele, voc� pode rodar programas em formato a.out nos modos texto,
X e SVGAlib.

%description -l es
Los sistemas Linux antiguos usaban un formato para programas y
bibliotecas compartidas llamado a.out en cuanto que los nuevos
sistemas utilizan el formato ELF. Para ejecutarse programas en el
formato antiguo a.out, necesitas de las bibliotecas de formato a.out
que este paquete ofrece.  Con �l, tu puedes ejecutar programas en
formato a.out en los modos texto, X y SVGAlib.

%description -l de
Alte Linux-Systeme benutzten 'a.out', ein Format f�r Programme und
gemeinsam genutzte Libraries, neuere Systeme verwenden 'ELF'. Um
alte a.out-Programme ausf�hren zu k�nnen, ben�tigen Sie die in diesem
Paket enthaltenen a.out-Format-Libraries. Damit k�nnen Sie die meisten
Pakete f�r Text-, X- und SVGAlib-Modi ausf�hren.

%description -l fr
Les vieux syst�mes Linux utilisaient un format appel� a.out pour les
programmes et les librairies partag�es, alors que les plus r�cents
utilisent le format ELF. Pour faire tourner les vieux programmes a.out
vous avez besoin des librairies au format a.out fournies par ce package.
Avec cela vous pourrez faire tourner la plupart des packages a.out en 
mode texte, X, ou SVGAlib.

%description -l tr
Eski Linux sistemleri programlar ve payla��lan kitapl�klar i�in a.out
bi�imini kullan�rlard�. Daha yeni sistemler ise, ELF bi�imini
kullan�yorlar. a.out bi�imindeki programlar� ko�turabilmek i�in, bu
paketin sa�lad��� a.out kitapl�klar� gerekiyor.

%prep
%setup -n aout

%build

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/i486-linuxaout/lib
mkdir -p $RPM_BUILD_ROOT/usr/X11R6
for n in *; do
    install -m 755 $n $RPM_BUILD_ROOT/usr/i486-linuxaout/lib
done
cd $RPM_BUILD_ROOT/usr
ln -sf X11R6 X11
ln -sf X11R6 X386

%clean
rm -fr $RPM_BUILD_ROOT

%post
if [ ! -f /etc/ld.so.conf ]; then
  touch /etc/ld.so.conf
fi

if ! grep '^/usr/i486-linuxaout/lib$' /etc/ld.so.conf > /dev/null; then
    echo "/usr/i486-linuxaout/lib" >> /etc/ld.so.conf
fi
/sbin/ldconfig

%postun
    TEMPFILE=`mktemp /tmp/aout-libs.XXXXXX`
    grep -v '^/usr/i486-linuxaout/lib$' /etc/ld.so.conf > $TEMPFILE
    cp $TEMPFILE /etc/ld.so.conf
    rm $TEMPFILE
    unset TEMPFILE
/sbin/ldconfig


%files
/usr/i486-linuxaout/lib/*
/usr/X11
/usr/X386

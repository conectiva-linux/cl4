Summary: GNU time Utility
Summary(pt_BR): Utilitário time da GNU
Summary(es): Utilitario time de la GNU
Name: time
Version: 1.7
Release: 10cl
Copyright: GPL
Group: Applications/System
Group(pt_BR): Aplicações/Sistema
Group(es): Aplicaciones/Sistema
#Source: ftp://prep.ai.mit.edu/pub/gnu/time-1.7.tar.gz
# recompactado com bzip2
Source: ftp://prep.ai.mit.edu/pub/gnu/time-1.7.tar.bz2
Prefix: /usr
Summary(de): GNU-Time-Utility 
Summary(fr): Utilitaire time de GNU
Summary(tr): GNU zamanlama aracý
BuildRoot: /var/tmp/time-root

%description
The 'time' utility is used as a sort of 'stopwatch' to time the execution
of a specified command. It can aid in the optimization of programs for
maximum speed, as well as a number of other uses.

%description -l pt_BR
O utilitário 'time' é usado como uma espécie de cronômetro para
medir o tempo de execução de um comando especificado. Ele pode
ajudar na otimização de programas para velocidade máxima, assim
como vários outros usos.

%description -l es
El utilitario 'time' se usa como una especie de cronómetro para
medir el tiempo de ejecución de un comando especificado. Puede
ayudar en la optimización de programas para velocidad máxima,
así como varios otros usos.

%description -l de
Das TIME-Utility wird als eine Art Stoppuhr zum Messen der Ausführung eines
bestimmten Befehls benutzt. Es dient in erster Linie der Optimierung von
Programmen für maximale Geschwindigkeit, hat aber daneben eine Vielzahl
anderer Anwendungen. 

%description -l fr
L'utilitaire « time » sert de chronomètre pour mesurer le temps d'exécution
d'une commande donnée. Il peut aider à l'optimisation de programmes pour
obtenir une vitesse maximale et a beaucoup d'autres uilisations.

%description -l tr
time, bir uygulamanýn çalýþma zamanýnýn ölçülmesi için kronometre gibi
kullanýlýr. Genellikle programlarýn hýz açýsýndan iyileþtirilmesinde
yararlý olur.

%changelog
* Thu Jun 10 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Oct 28 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations


* Mon Aug 10 1998 Erik Troan <ewt@redhat.com>
- buildrooted and defattr'd
* Mon Apr 27 1998 Prospector System <bugs@redhat.com>

- translations modified for de, fr, tr

* Mon Oct 27 1997 Cristian Gafton <gafton@redhat.com>
- fixed info handling

* Thu Oct 23 1997 Cristian Gafton <gafton@redhat.com>
- updated the spec file; added info file handling

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s

%install
make prefix=$RPM_BUILD_ROOT/usr install
gzip -9nf $RPM_BUILD_ROOT/usr/info/time.info
strip $RPM_BUILD_ROOT/usr/bin/time

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/install-info /usr/info/time.info.gz /usr/info/dir \
	--entry="* time: (time).		GNU time Utility" 

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --delete /usr/info/time.info.gz /usr/info/dir \
	--entry="* time: (time).		GNU time Utility" 
fi

%files
%doc NEWS README
/usr/bin/time
/usr/info/time.info*

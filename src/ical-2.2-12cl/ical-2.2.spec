Summary: Calender application made with Tcl/Tk
Summary(pt_BR): Aplicação de calendário feita em Tcl/Tk
Summary(es): Aplicación de calendario hecha en Tcl/Tk
Name: ical 
Version: 2.2
Release: 12cl
# was .gz
Source: http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/icalbins/ical-%{PACKAGE_VERSION}.tar.bz2
Source1: ical.wmconfig
Source800: ical-wmconfig.i18n.tgz
Patch0: ical-2.2-newtcl.patch
Url: http://www.research.digital.com/SRC/personal/Sanjay_Ghemawat/ical/home.html
Copyright: distributable
Group: Applications/Productivity
Group(pt_BR): Aplicações/Produtividade
Group(es): Aplicaciones/Productividad
BuildRoot: /var/tmp/ical-root
Summary(de): Kalenderanwendung erstellt mit Tcl/Tk
Summary(fr): Application de calendrier faite avec Tcl/Tk.
Summary(tr): Grafik takvim ve randevu uyarý uygulamasý

%description
ical is a popular X-based calendar/scheduler application which 
can help you keep track of single events and recurring events
(daily, weekly, monthly, or yearly), and sets off alarms to warn
you of appointments.

%description -l pt_BR
A ical é uma popular aplicação calendário/agenda baseada em X a
qual pode ajudar você a organizar eventos simples ou recorrentes
(diariamente, semanalmente, mensalmente ou anualmente), e toca o
alarme para lembrá-lo de seus compromissos.

%description -l es
ical es una popular aplicación calendario/agenda basada en X
que puede ayudarte a organizar eventos sencillos o recurrentes
(diariamente, semanalmente, mensualmente o anualmente), y suena el
alarme para acordarte de tus obligaciones.

%description -l de
ical ist eine beliebte Kalender/Planer-Applikation auf, die Ihnen 
hilft, einzelne Ereignisse oder regelmäßige Termine (täglich, 
wöchentlich, monatlich oder jährlich auftretend) im Auge zu behalten 
und auf Wunsch mit Hilfe des Weckerfunktion zu signalisieren. 

%description -l fr
ical est une application calendrier/ordonnanceur sous X qui permet
de conserver les événements simples et récurrents (quotidien, hebdomadaire,
mensuel ou annuel) et de configurer des alarmes de rappels.

%description -l tr
ical, tek ya da düzenli yinelenen olaylarý (günlük, haftalýk, aylýk ve yýllýk)
izlemekte kullanýlan ve randevular için uyarýcý bir alarmý olan, X tabanlý bir
takvim uygulamasýdýr.

%prep
%setup -q
%patch0 -p1

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/ical-%{PACKAGE_VERSION}
#install -m 644 $RPM_SOURCE_DIR/ical.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/ical

mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig/





tar xvfpz $RPM_SOURCE_DIR/ical-wmconfig.i18n.tgz -C $RPM_BUILD_ROOT/etc/X11/wmconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc doc/ical.html doc/ical.doc 
%doc doc/interface.html doc/interface.doc
/usr/bin/ical-%{PACKAGE_VERSION}
/usr/bin/ical
/usr/man/man1/ical.1
/usr/lib/ical
/etc/X11/wmconfig/ical

%changelog
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Jun  9 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Mon Mar 15 1999 Conectiva <dist@conectiva.com>
- i18n wmconfig

* Mon Dec 07 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- regerado com o egcs 1.0.3a e binutils 2.9.1.0.17

* Tue Oct 27 1998 Conectiva <dist@conectiva.com>
- added pt_BR translations

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- patch to build against the latest tcltk

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed wmconfig entry

* Thu Oct 23 1997 Otto Hammersmith <otto@redhat.com>
- replaced references to the version number with %{PACKAGE_VERSION}

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- updated to version 2.2, which is supposed to work with Tcl/Tk 8.0
- added wmconfig entry

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- Update version

* Tue Sep 30 1997 Erik Troan <ewt@redhat.com>
- build against tcl/tk 8.0

* Fri Aug 22 1997 Erik Troan <ewt@redhat.com>
- built against glibc

Summary: Red Hat Sound system 
Summary(pt_BR): Sistema de som da Red Hat
Summary(es): Sistema de sonido de Red Hat
Name: rhsound 
Version: 1.7
Release: 7cl
Copyright: distributable
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
Source: rhsound-%{PACKAGE_VERSION}.tar.gz
Source1: sound.init
BuildArchitectures: noarch
Prereq: chkconfig
AutoReqProv: no
Requires: aumix
BuildRoot: /tmp/rhsound

%changelog
* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start

* Sat Mar 13 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- /etc/rc.d/init.d/functions call added to /etc/rc.d/init.d/sound

* Fri Mar 12 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initscripts i18n
- added Group, Summary and %description translations

* Sun Oct 25 1998 Arnaldo Carvalho de Melo <acme@conectiva.com>
- added pt_BR translations
- sound.init traduzido para pt_BR

* Fri Oct  2 1998 Bill Nottingham <notting@redhat.com>

- more documentation updates

* Mon Sep 21 1998 Bill Nottingham <notting@redhat.com>

- update documentation

* Tue Sep  8 1998 Bill Nottingham <notting@redhat.com>

- fixed fix

* Wed Sep  2 1998 Bill Nottingham <notting@redhat.com>

- fixed to work for (some) non-OSS modules

* Wed Nov 13 1997 Mike Wangsmo <wanger@redhat.com>

- sent error to /dev/null when no sound is configured

* Mon Nov 11 1997 Mike Wangsmo <wanger@redhat.com>

- changed chkconfig description

* Fri Nov 07 1997 Mike Wangsmo <wanger@redhat.com>

- modified init scripts to record mixer settings for non-modular sound 
- made this a noarch package

* Fri Oct 31 1997 Michael Fulbright <msf@redhat.com>

- how appropriate on this day to make it modprobe modules in a service!
- added check to not run aumix -S if no sound modules loaded

* Wed Oct 29 1997 Mike Wangsmo <wanger@redhat.com>

- restructured the sound system to be run as a init service.
- first version

%description
The fake "service" created by rhsound allows sound modules to be
loaded in contrallable runlevels and preserves mixer settings on
shutdown/restarts

%description -l pt_BR
O serviço falso criado por rhsound permite que os módulos de som
sejam carregados pelos scripts de inicialização e preserva as
configurações do mixer entre shutdowns e restarts da máquina.

%description -l es
El servicio falso creado por rhsound permite que los módulos
de sonido se carguen por los scripts de arranque y preserva las
configuraciones del mixer entre shutdowns y restarts de la máquina.

%prep
%setup -n rhsound

%install
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d

install -m755 $RPM_SOURCE_DIR/sound.init $RPM_BUILD_ROOT/etc/rc.d/init.d/sound

#%post
#/sbin/chkconfig --add sound

%preun 
if [ $1 = 0 ]; then
    # execute this only if we are NOT doing an upgrade
    /sbin/chkconfig --del sound 
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.modules README.modules.usage
%config /etc/rc.d/init.d/sound

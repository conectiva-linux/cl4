Summary: Text-mode tool for setting up NIS and shadow passwords.
Summary(pt_BR): Ferramenta de interface texto para configuração de senhas shadow e NIS
Summary(es): Text-mode tool for setting up NIS and shadow passwords.
Name: authconfig
%define version 1.8
Version: %{version}
Release: 2cl
Copyright: GPL
ExclusiveOS: Linux
Group: System Environment/Base
Group(pt_BR): Ambiente do Sistema/Base
Group(es): Ambiente del Sistema/Base
BuildRoot: /var/tmp/%{name}-root
Source: %{name}-%{version}.tar.gz
Source1: authconfig-pt_BR.po

%description 
Authconfig is a terminal mode program for setting up Network
Information Service (NIS) and shadow (more secure) passwords
on your system. Authconfig also configures the system to
automatically turn on NIS at system startup.

%description -l pt_BR
O authconfig é um programa de interface texto para configurar
o NIS e senhas shadow no seu sistema. O authconfig também pode
inicializar o NIS no boot do sistema.

%description -l es
Authconfig is a terminal mode program for setting up Network
Information Service (NIS) and shadow (more secure) passwords
on your system. Authconfig also configures the system to
automatically turn on NIS at system startup.

%prep
%setup -q

%build
cp $RPM_SOURCE_DIR/authconfig-pt_BR.po po/pt_BR.po
make

%install
make INSTROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root)/usr/sbin/authconfig
%attr(-,root,root)/usr/man/man8/authconfig.8
%attr(-,root,root)/usr/share/locale/*/LC_MESSAGES/authconfig.mo

%changelog
* Sat Jun 28 1999 Guilherme Manika <gwm@conectiva.com>
- Added pt_BR translation

* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Rodrigo Parra Novo <rodarvus@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- release for Red Hat Linux 6.0

* Thu Apr 01 1999 Preston Brown <pbrown@redhat.com>
- don't report errors about NIS fields not being filled in if not enabled

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- fix typo
- change domainname at nis start and stop

* Tue Mar 23 1999 Preston Brown <pbrown@redhat.com>
- fixed man page

* Wed Mar 17 1999 Matt Wilson <msw@redhat.com>
- fixed rewriting /etc/yp.conf
- restarts ypbind so that new changes take effect

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- just make the NIS part of configuration grayed out if NIS is not installed

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- static buffer sizes increased.

* Tue Mar  9 1999 Matt Wilson <msw@redhat.com>
- removed build opts because of problems on alpha

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Don't rewrite ypbind.conf if you're not configuring NIS

* Mon Feb  8 1999 Matt Wilson <msw@redhat.com>
- Don't configure NIS if /etc/ypbind.conf does not exist.

* Sat Feb  6 1999 Matt Wilson <msw@redhat.com>
- changed "/sbin/chkconfig --add ypbind" to
  "/sbin/chkconfig --level 345 ypbind on"
- added checks for null nis domains and servers if nis is enabled or if
  not using broadcast.
- added newt entry filter for spaces in domains

* Sat Feb  6 1999 Matt Wilson <msw@redhat.com>
- changed command line options to match user interface
- added --help

* Thu Feb  4 1999 Matt Wilson <msw@redhat.com>
- Rewrote UI to handle geometry management properly
- MD5 passwords do not require shadow passwords, so made them independent

* Wed Feb 03 1999 Preston Brown <pbrown@redhat.com>
- initial spec file

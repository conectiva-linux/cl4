Summary: Extra scripts for i18n development
Summary(pt_BR): Scripts extras para internacionalização de programas (i18n)
Summary(es): Scripts extras para internacionalización de programas
Name: gettext-extras
Version: 1.2
Release: 2cl
Group: Development/Tools
Group(pt_BR): Desenvolvimento/Ferramentas
Group(es): Desarrollo/Herramientas
Source: gettext-extras-%{version}.tar.gz
Copyright: GPL
BuildRoot: /var/tmp/gettext-extras
BuildArch: noarch

%description
Extra scripts for i18n development

%description -l pt_BR
Scripts extras para internacionalização de programas (i18n)

%description -l es
Scripts extras para internacionalización de programas

%prep
%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/conectiva/xgettext_sh
mkdir -p $RPM_BUILD_ROOT/usr/bin

cp xgettext_sh $RPM_BUILD_ROOT/usr/bin
cp xgettext_sh.py $RPM_BUILD_ROOT/usr/lib/conectiva/xgettext_sh
touch $RPM_BUILD_ROOT/usr/lib/conectiva/xgettext_sh/xgettext_sh.pyc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/xgettext_sh
%dir /usr/lib/conectiva/xgettext_sh
/usr/lib/conectiva/xgettext_sh/xgettext_sh.py
%verify(not md5 mtime size) /usr/lib/conectiva/xgettext_sh/xgettext_sh.pyc

%changelog
* Mon Jun 21 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon May 31 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- supports the extra functions from initscripts as i18n string marker

* Tue Mar 23 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Sat Mar 13 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- header fixed

* Wed Mar 10 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- initial version

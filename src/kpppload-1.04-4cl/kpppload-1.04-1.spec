%define version 1.04
%define kdename kpppload
%define kderelease 4cl
Summary: A PPP Link Monitor
Summary(pt_BR): Programa para monitoração de linhas PPP
Summary(es): A PPP Link Monitor
Name: %{kdename}
Version: %{version}
Release: %{kderelease}
Source: %{kdename}-%{version}.tar.gz
Copyright: GPL
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
BuildRoot: /var/tmp/%{kdename}-buildroot
Requires: qt >= 1.42 kdesupport
Prefix: /usr

%description
Monitors the load on your PPP connection.  Looks a lot like xload.

%description -l pt_BR
O kpppload monitora a sua conexão XXX. Ele é semelhante ao xload.

%description -l es
Monitors the load on your PPP connection.  Looks a lot like xload.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
# the package comes with bad dependencies!
find . -name \*.o | xargs rm -f
find . -name \*.moc | xargs rm -f
find . -name .deps | xargs rm -fr

%build
export KDEDIR=/usr
./configure \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT
make clean
make CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"

%install
make install-strip prefix=$RPM_BUILD_ROOT/usr

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' \
	-e '/\/applnk\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{kdename}

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{kdename}

%files -f ../file.list.%{kdename}

%changelog
* Tue Jun 15 1999 Conectiva <dist@conectiva.com>
- Added to Conectiva Linux
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Sat Feb 06 1999 Preston Brown <pbrown@redhat.com>
- rebuilt against new libstdc++

* Thu Jan 07 1999 Preston Brown <pbrown@redhat.com>
- changed over to use /usr as the root

* Sat Dec 12 1998 Preston Brown <pbrown@redhat.com>
- initial, rather bare RPM adapted to our stringent standards. :)

%define kdeprefix /usr
%define version 0.3.3
%define kdename aktion
%define kderelease 1cl
Name: %{kdename}
Summary: aKtion - Movie player for KDE
Summary(pt_BR): O aKtion é um reprodutor de filmes para o kde
Summary(es): aKtion - Movie player for KDE
Version: %{version}
Release: %{kderelease}
Source: %{kdename}.tgz
Group: Applications/Multimedia
Group(pt_BR): Aplicações/Multimídia
Group(es): Aplicaciones/Multimedia
BuildRoot: /var/tmp/%{kdename}-buildroot
Copyright: GPL
Requires: qt >= 1.42 kdesupport xanim >= 27070
Prefix: /usr

%description
Movie player for the K Desktop Environment.  Requires 'xanim' to function.

%description -l pt_BR
O aKtion é um reprodutor de filmes para o kde. Precisa do xanim.

%description -l es
Movie player for the K Desktop Environment.  Requires 'xanim' to function.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
export KDEDIR=%{kdeprefix}
./configure \
	--prefix=$KDEDIR \
	--with-install-root=$RPM_BUILD_ROOT
make CXXFLAGS="$RPM_OPT_FLAGS"

%install
make install-strip prefix=$RPM_BUILD_ROOT%{kdeprefix}

# remove conflicting mime types
rm -rf $RPM_BUILD_ROOT%{kdeprefix}/share/mimelnk

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
* Sun Jun 20 1999 Conectiva <dist@conectiva.com>
- Recompiled with glibc 2.1.x, egcs 1.1.x, rpm 3.0.x and kernel 2.2.x

* Mon Apr 05 1999 Preston Brown <pbrown@redhat.com>
- upgrade to bugfix version 0.3.3

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Feb 05 1999 Preston Brown <pbrown@redhat.com>
- new version, built against new libstdc++

* Thu Jan 07 1999 Preston Brown <pbrown@redhat.com>
- moved to /usr from /opt/kde

* Sat Dec 12 1998 Preston Brown <pbrown@redhat.com>
- first package attempt.

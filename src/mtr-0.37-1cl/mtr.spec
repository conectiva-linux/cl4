%define	name	mtr
%define	version	0.37
%define	release	1cl

Summary: Ping/Traceroute network diagnostic tool
Summary(pt_BR): Ferramenta para diagnóstico da rede, combinando ping/traceroute
Summary(es): Herramienta para diagnóstico de red, combinando ping/traceroute
Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Copyright: GPL
Url: http://www.BitWizard.nl/mtr
# was .gz
Source:	%{name}-%{version}.tar.bz2
Buildroot: /tmp/%{name}-%{version}-root
Icon: %{name}.gif

%description
Mtr is a network diagnostic tool which combines Ping and
Traceroute into one program. Mtr also has two interfaces:
An ncurses interface, useful for using Mtr from a telnet
session and a Gtk interface if you are using X.

%description -l pt_BR
O mtr é uma ferramenta para diagnóstico da rede que combina
ping e traceroute em um programa. Tem duas interfaces, uma
ncurses, útil para uso em sessões telnet/ssh e uma gtk para
uso no X Window.

%description -l es
mtr es una herramienta para diagnóstico de la red que combina ping
y traceroute en un programa. Tiene dos interfaces, una ncurses, útil
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.

%package gtk
Summary: Ping/Traceroute network diagnostic tool - GTK Interface
Summary(pt_BR): Interface GTK para o mtr
Summary(es): Interface GTK para mtr
Group: Applications/Internet
Group(pt_BR): Aplicações/Internet
Group(es): Aplicaciones/Internet
Requires: mtr

%description gtk
Mtr is a network diagnostic tool which combines Ping and
Traceroute into one program. Mtr also has two interfaces:
An ncurses interface, useful for using Mtr from a telnet
session and a Gtk interface if you are using X Windows.

This is the GTK interface for mtr.

%description -l pt_BR gtk
O mtr é uma ferramenta para diagnóstico da rede que combina
ping e traceroute em um programa. Tem duas interfaces, uma
ncurses, útil para uso em sessões telnet/ssh e uma gtk para
uso no X Window.

Esta é a interface GTK para o mtr.

%description -l es gtk
mtr es una herramienta para diagnóstico de la red que combina ping y
traceroute en un programa. Tiene dos interfaces, una ncurses, útil
para uso en sesiones telnet/ssh y una gtk para uso en el X Window.
Esta es la interface GTK para mtr.

%prep

%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
	./configure --prefix=/usr
make
strip mtr
mv mtr mtr-gtk
make distclean

CFLAGS="$RPM_OPT_FLAGS" \
	./configure --prefix=/usr --with-gtk-prefix=/no_gtk
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT/usr/{X11R6/bin,sbin,share/pixmaps,man/man8}
make prefix=$RPM_BUILD_ROOT/usr install-strip
install -s -m 755 mtr-gtk $RPM_BUILD_ROOT/usr/X11R6/bin
install -m 644 img/mtr_icon.xpm $RPM_BUILD_ROOT/usr/share/pixmaps
gzip -9f $RPM_BUILD_ROOT/usr/man/man8/mtr.8

# Remove suid bit from /usr/sbin/mtr
chmod 755 $RPM_BUILD_ROOT/usr/sbin/mtr

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING FORMATS INSTALL NEWS README SECURITY TODO
/usr/sbin/mtr
/usr/man/man8/*.8.gz

%files gtk
%defattr(-,root,root)
%doc AUTHORS COPYING FORMATS INSTALL NEWS README SECURITY TODO
/usr/X11R6/bin/mtr-gtk
/usr/share/pixmaps/mtr_icon.xpm

%changelog
* Fri Jun 04 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- updated from 0.33 to 0.37

* Mon Apr 19 1999 Conectiva <dist@conectiva.com>
- final rebuild for 3.0 server edition
- Removed suid bit from mtr-gtk and mtr

* Fri Mar 19 1999 Conectiva <dist@conectiva.com>
- added Group, Summary and %description translations

* Wed Mar 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.33-1]
- v0.33
- Fixed the Linux glibc resolver problems.
- Fixed the off-by-one problem with -c option.

* Mon Mar  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.32-1]
- v0.32
- Fixed the FreeBSD bug detection stuff.

* Fri Mar  5 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.31-1]
- v0.31
- Fixed a few documentation issues. -- Matt
-  Changed the autoconf stuff to find the resolver library on
     Solaris. -- REW
-  Cleaned up the autoconf.in file a bit. -- Matt.

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.30-1]
- Build gtk version against gtk+-1.2.0
- v0.30
- Fixed a typo in the changelog (NEWS) entry for 0.27. :-)
- added use of "MTR_OPTIONS" environment variable for defaults.

* Wed Mar  3 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.29-1]
- v0.29 Lots of stuff.
- Neato overview display by David Sward.
- FreeBSD does wrong in the kernel the same that Solaris/x86 (see
    note for 0.27 does right. It forces mtr to send bad packets....
- Adjusted "not too much at once" algorithm. Now probing
    continues as long as not more than 5 hosts are unknown.
    Returning packets usually allow us to do the first sweep
    in one go.

* Tue Nov  3 1998 Fryguy_ <fryguy@falsehope.com>
  [mtr-0.28-2]
- Divided mtr rpm to mtr and mtr-gtk

* Mon Nov  2 1998 Fryguy_ <fryguy@falsehope.com>
  [mtr-0.28-1]
- v0.27
        Fixed bug that showed up on Solaris/x86.
        Gimp mainloop now runs as it's supposed to.

- v0.26
        Added "-n" flag for numeric output.
        fixed IP numbers displaying backwards.
        GTK mainloop now runs at 10 packets per second.
          - That's too much if there are only 3 hosts
          - that's too little if there are 20 hosts.
        -> Someone tell me how to change the "ping-timeout"
           callback time in gtk. Can't find it in the docs.
        The default for "hostname" is now "localhost" so that
        you can start mtr without any arguments and later
        fill in the host you want to trace to.

* Wed Oct 28 1998 Fryguy_ <fryguy@falsehope.com>
  [mtr-0.25-1]
- v0.25
        Included two "raw" formats. One for separating GUI from
        the setuid program, and one suitable for later parsing and
        displaying. Volunteers wanted to separate the GTK
        backend. Thanks to Bertrand Leconte for contributing
        the format that's now called "split".

- v0.24
        Fixed number of probes. Accidentally was counted per
        packet sent instead of per round of packets.

- v0.23
        Fixed Sparc alignment problem with statmalloc

- v0.22
        Roger has take over maintenance.
        mtr now uses an "int" to pass options to the kernel.
        Makes things work on Solaris and *BSD I'm told.
        mtr doesn't fire off a flurry of packets when a new
        second comes around. Instead they are spaced evenly
        around the whole second. This allows people with a
        relatively slow first link to do meaningful measurements
        of whatever is behind that.

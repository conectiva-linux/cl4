Summary: The InterNetNews (INN) system, an Usenet news server.
Summary(pt_BR): INN, InterNet News System (servidor news)
Summary(es): INN, InterNet News System (servidor news)
Name: inn
Version: 2.2
Release: 15cl
Copyright: GPL
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)
Source0: ftp://ftp.isc.org/isc/inn/inn-%{version}.tar.bz2
Source1: inn-default-active
Source2: inn-default-distributions
Source3: inn-default-newsgroups
Source4: inn-cron-expire
Source5: inn-cron-rnews
Source6: inn-etc-nnrp.access
Source7: inn-cron-nntpsend
Source8: innd.init
Source9: ftp://ftp.exit109.com/users/jeremy/cleanfeed-latest.tar.gz
Source10: ftp://ftp.isc.org/pub/pgpcontrol/pgpverify-1.10
Source18: innd.init.i18n
Patch0: inn-2.2-rh.patch
Patch1: inn-sec.patch
Patch2: inn-2.2-frsize.patch
Buildroot: /var/tmp/%{name}-root
Prereq: chkconfig grep textutils sed fileutils sh-utils
Requires: cleanfeed

%description
INN (InterNetNews) is a complete system for serving Usenet news and/or
private newsfeeds.  INN includes innd, an NNTP (NetNews Transport
Protocol) server, and nnrpd, a newsreader that is spawned for each client. 
Both innd and nnrpd vary slightly from the NNTP protocol, but not in ways
that are easily noticed.

Install the inn package if you need a complete system for serving and
reading Usenet news.  You may also need to install inn-devel, if you are
going to use a separate program which interfaces to INN, like newsgate or
tin.

%description -l pt_BR
INN é um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informações sobre a configuração do INN em /usr/doc -- leia.

%description -l es
INN es un servidor de news, que puede ser configurado para manipular
USENET news bien como newsfeeds privadas. Existe un *Montón* de
información sobre la configuración del INN en /usr/doc -- léela.

%package devel
Summary: The INN (InterNetNews) library.
Summary(pt_BR): Biblioteca INN
Summary(es): Biblioteca INN
Group: Development/Libraries
Group(pt_BR): Desenvolvimento/Bibliotecas
Group(es): Desarrollo/Bibliotecas
Requires: inn = %{version}

%description devel
The inn-devel package contains the INN (InterNetNews) library, which
several programs that interface with INN need in order to work (for
example, newsgate and tin).

If you are installing a program which must interface with the INN
news system, you should install inn-devel.

%description -l pt_BR devel
Esta biblioteca é requerida por vários programas que tem interface
com o INN, como o newsgate ou tin.

%description -l es devel
Esta biblioteca es requerida por varios programas que tienen
interface con INN, como el newsgate o tin.

%package -n inews
Summary: Sends Usenet articles to a local news server for distribution.
Summary(pt_BR): Programa Inews (usado para postagem pelo inn e trn)
Summary(es): Programa Inews (usado para franqueo por inn y trn)
Group: System Environment/Daemons
Group(pt_BR): Ambiente do Sistema/Servidores
Group(es): Ambiente del Sistema/Servidores (Daemons)

%description -n inews
The inews program is used by some news programs (for example, inn and
trn) to post Usenet news articles to local news servers.  Inews reads an
article from a file or standard input, adds headers, performs some
consistency checks and then sends the article to the local news server
specified in the inn.conf file.

Install inews if you need a program for posting Usenet articles to local
news servers.

%description -l pt_BR -n inews
O programa inews é usado por alguns leitores de news para postar
mensagens. Ele faz alguma consistência checando e reformatando
headers, e enviando o artigo para o servidor de news especificado
no inn.conf.

%description -l es -n inews
El programa inews se usa por algunos lectores de news para postar
mensajes. Hace alguna consistencia chequeando y reformateando
headers, y enviando el artículo para el servidor de news especificado
en el inn.conf.

%prep
%setup -q -a 9
%patch0 -p1 -b .rh
%patch1 -p1 -b .sec
%patch2 -p1 -b .frsize

%build
rm -f config.cache
libtoolize --copy --force
./configure --prefix=/usr  \
	--sysconfdir=/etc/news \
	--with-log-dir=/var/log/news --with-spool-dir=/var/spool/news\
	--with-db-dir=/var/lib/news --with-run-dir=/var/run/news \
	--with-etc-dir=/etc/news --with-tmp-dir=/tmp \
	--with-perl --enable-shared \
	--enable-tagged-hash --enable-merge-to-groups \
	--with-news-user=news --with-news-group=news \
	--with-news-master=news --enable-pgp-verify
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# -- Install man pages needed by suck et al.
mkdir -p $RPM_BUILD_ROOT/usr/include/inn
for f in clibrary.h configdata.h dbz.h libinn.h
do
    install -c -m 0644 -o 0 -g 0 ./include/$f $RPM_BUILD_ROOT/usr/include/inn
done

mkdir -p $RPM_BUILD_ROOT/etc/rc.d
mv $RPM_BUILD_ROOT/usr/bin/rc.news $RPM_BUILD_ROOT/etc/rc.d

file $RPM_BUILD_ROOT/usr/bin/* $RPM_BUILD_ROOT/usr/bin/*/* 2>/dev/null | \
	grep ELF | cut -d':' -f1 | xargs -l strip
touch $RPM_BUILD_ROOT/var/lib/news/subscriptions
chown news.news $RPM_BUILD_ROOT/var/lib/news/subscriptions
chmod 644 $RPM_BUILD_ROOT/var/lib/news/subscriptions

install -m 644 -o news -g news $RPM_SOURCE_DIR/inn-default-active \
        $RPM_BUILD_ROOT/var/lib/news/active
install -m 644 -o news -g news $RPM_SOURCE_DIR/inn-default-distributions \
        $RPM_BUILD_ROOT/var/lib/news/distributions
install -m 644 -o news -g news $RPM_SOURCE_DIR/inn-default-newsgroups \
        $RPM_BUILD_ROOT/var/lib/news/newsgroups

mkdir -p $RPM_BUILD_ROOT/etc/cron.hourly $RPM_BUILD_ROOT/etc/cron.daily
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/inn-cron-expire \
        $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-expire
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/inn-cron-rnews \
        $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-rnews
install -m755 -o 0 -g 0 $RPM_SOURCE_DIR/inn-cron-nntpsend \
        $RPM_BUILD_ROOT/etc/cron.hourly/inn-cron-nntpsend

install -m440 -o news -g news $RPM_SOURCE_DIR/inn-etc-nnrp.access \
        $RPM_BUILD_ROOT/etc/news/nnrp.access

mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 755 $RPM_SOURCE_DIR/innd.init.i18n \
	$RPM_BUILD_ROOT/etc/rc.d/init.d/innd

rm -f $RPM_BUILD_ROOT/var/lib/news/history
touch $RPM_BUILD_ROOT/var/lib/news/history
touch $RPM_BUILD_ROOT/var/lib/news/.news.daily
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/bin/makehistory\
	-a $RPM_BUILD_ROOT/var/lib/news/active \
	-i -r -f $RPM_BUILD_ROOT/var/lib/news/history || :
chown news.news $RPM_BUILD_ROOT/var/lib/news/*
chmod 644 $RPM_BUILD_ROOT/var/lib/news/*
chown news.news $RPM_BUILD_ROOT/var/lib/news/.news.daily
chmod 644 $RPM_BUILD_ROOT/var/lib/news/.news.daily

# rnews needs to be able to write to UUCP spool areas for news over UUCP
chown uucp.news $RPM_BUILD_ROOT/usr/bin/rnews
chmod 4550 $RPM_BUILD_ROOT/usr/bin/rnews

umask 002
touch $RPM_BUILD_ROOT/var/log/news/news.notice
touch $RPM_BUILD_ROOT/var/log/news/news.crit
touch $RPM_BUILD_ROOT/var/log/news/news.err
touch $RPM_BUILD_ROOT/var/lib/news/active.times
chown news.news $RPM_BUILD_ROOT/var/lib/news/active.times
chown -R news.news $RPM_BUILD_ROOT/var/log/news

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

#Build filelist
find $RPM_BUILD_ROOT -type f -or -type l | \
	sed -e "s|$RPM_BUILD_ROOT||g" | \
	sed 's|^/etc|%config &|' | \
	sed 's|^/var/lib/news/|%config(noreplace) &|' | \
	sed 's|.*innshellvar|%config &|' | \
	sed 's|/var/log/news|%ghost &|' > files.list
grep -v inews files.list | \
	egrep -v "\.(h|so|a|la)$" | \
	grep -v "/man3/" > files.main
grep inews files.list > files.inews
egrep "\.(h|so|a|la)$" files.list > files.devel
grep "/man3/" files.list >> files.devel

# conectiva
chmod a-s $RPM_BUILD_ROOT/usr/bin/inndstart

%clean
rm -rf $RPM_BUILD_ROOT
rm -f files.list files.main files.devel files.inews

%post
#/sbin/chkconfig --add innd

umask 002
touch /var/log/news/news.notice
touch /var/log/news/news.crit
touch /var/log/news/news.err
[ -f /var/lib/news/active.times ] || {
    touch /var/lib/news/active.times
    chown news.news /var/lib/news/active.times
}
chown -R news.news /var/log/news*
if [ -f /etc/syslog.conf ]; then
  if ! grep -q INN /etc/syslog.conf; then
    sed 's/mail.none;/mail.none;news.none;/' < /etc/syslog.conf > /etc/syslog.conf.inn
    mv /etc/syslog.conf.inn /etc/syslog.conf

    echo '' \
       >> /etc/syslog.conf
    echo '#' \
       >> /etc/syslog.conf
    echo '# INN' \
       >> /etc/syslog.conf
    echo '#' \
       >> /etc/syslog.conf
    echo 'news.=crit                                        /var/log/news/news.crit'   >> /etc/syslog.conf
    echo 'news.=err                                         /var/log/news/news.err'    >> /etc/syslog.conf
    echo 'news.notice                                       /var/log/news/news.notice' >> /etc/syslog.conf
    fi
  if [ -f /var/run/syslog.pid ]; then
    kill -HUP `cat /var/run/syslog.pid` 2> /dev/null ||:
  fi
else
  # syslog.conf does not exist

  echo "mail.none /var/log/messages" \
     >  /etc/syslog.conf.inn
  echo "" \
     >> /etc/syslog.conf.inn
  echo "# INN" \
     >> /etc/syslog.conf.inn
  echo "news.=crit                                      /var/log/news/news.crit"     >> /etc/syslog.conf.inn
  echo "news.=err                                       /var/log/news/news.err"      >> /etc/syslog.conf.inn
  echo "news.notice                                     /var/log/news/news.notice"   >> /etc/syslog.conf.inn
fi
if [ `cat /etc/news/inn.conf | grep '^server:' | wc -l` -lt 1 ]; then
  echo "server: `hostname -f`" >> /etc/news/inn.conf
fi

if [ -f /var/lib/news/history ]; then
        cd /var/lib/news
        /usr/bin/makehistory -i -r
        for i in dir hash index pag; do
                [ -f history.n.$i ] && mv history.n.$i history.$i
        done
        chown news.news history.*
        chmod 644 history.*
else
        cd /var/lib/news
        cp /dev/null history
        /usr/bin/makehistory -i
        for i in dir hash index pag; do
                [ -f history.n.$i ] && mv history.n.$i history.$i
        done
        chown news.news history history.*
        chmod 644 history history.*
fi

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del innd
    if [ -f /var/lib/news/history.dir ]; then
       rm -f /var/lib/news/history.*
    fi
fi

%files -f files.main
%dir /usr/bin/control
%dir /usr/bin/filter
%dir /usr/bin/rnews.libexec
%dir /usr/bin/auth
%dir /etc/news
%dir /var/spool/news
%dir /var/spool/news/articles
%dir /var/spool/news/overview
%dir /var/spool/news/archive
%dir /var/spool/news/incoming
%dir /var/spool/news/incoming/bad
%dir /var/spool/news/outgoing
%dir /var/spool/news/uniover
%dir /var/spool/news/innfeed
%dir /var/log/news
%dir /var/log/news/OLD
%dir /var/lib/news
%dir /var/run/news

%doc samples
%doc README* ChangeLog CONTRIBUTORS COPYRIGHT HISTORY

%files devel -f files.devel

%files -n inews -f files.inews

%changelog
* Sun Jun 20 1999 Wanderlei Antonio Cavassin <cavassin@conectiva.com>
- init script with i18n support and one bug fixed

* Sun Jun 20 1999 Arnaldo Carvalho de Melo <acme@conectiva.com>
- chkconfig --add removed, so that the user has to enable the service start
- sources recompressed

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Sun Jun 13 1999 Jeff Johnson <jbj@redhat.com>
- mark /var/lib/news/* as %config(noreplace) (#3425)

* Fri Jun 11 1999 Marcelo Tosatti <marcelo@conectiva.com>
- removed suid bit from /usr/bin/inndstart

* Thu Jun 10 1999 Dale Lovelace <dale@redhat.com>
- change su news to su - news (#3331)

* Wed Jun  2 1999 Jeff Johsnon <jbj@redhat.com>
- complete trn->inews->inn dependency (#2646)
- use f_bsize rather than f_frsize when computing blocks avail (#3154).
- increase client timeout to 30 mins (=1800) (#2833).
- add missing includes to inn-devel (#2904).

* Mon May 31 1999 Jeff Johnson <jbj@redhat.com>
- fix owner and permissions on /var/lib/news/.news.daily (#2354).

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- fixed paths in cron jobs, check to see that innd is enabled

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- path to makehistory corrected.

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- fixed permissions on rnews for uucp

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- make sure init scripts get packaged up, fix other minor bugs
- major fixups to innd.conf for denial of service attacks, sanity, etc.
- make sure history gets rebuilt in an upgrade (added to post section)
- many thanks go out to mmchen@minn.net for these suggestions.

* Fri Feb 19 1999 Cristian Gafton <gafton@redhat.com>
- prereq all the stuff we need in the postinstall scripts

* Sat Feb  6 1999 Bill Nottingham <notting@redhat.com>
- strip -x bits from docs/samples (bogus dependencies)

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- innd.init chkconfig entry was incorrect (problem #855)

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- susbsys name must be identical to script name (problem #700)

* Mon Jun 29 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed startinnfeed paths

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed innfeed patched to be perl-version independent

* Wed Apr 15 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed sfnet.* entries in control.ctl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- moved cleanfeed to its own package

* Thu Apr 09 1998 Bryan C. Andregg <bandregg@redhat.com>
- added insync patches
- added cleanfeed
- added innfeed

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- abuse buildroot to simplify the file list
- built against Manhattan

* Tue Mar 24 1998 Bryan C. Andregg <bandregg@redhat.com>
- updated to inn 1.7.2
- Added REMEMBER_TRASH and Poison patch

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to inn 1.7
- added chkconfig support to the initscripts
- orginally released as release 2, leving release 1 if a 4.2.x upgrade
  is ever necessary 
- don't start it in any runlevel (by default)
- added inndcomm.h

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Aug 05 1997 Elliot Lee <sopwith@redhat.com>
- Applied the 1.5.1sec and 1.5.1sec2 patches
- Applied 3 more unoff patches.
- Removed insanity in /etc/cron.hourly/inn-cron-nntpsend, it now
  just runs nntpsend as news.

* Wed Apr 02 1997 Erik Troan <ewt@redhat.com>
- Patch from CERT for sh exploit.
- Changed /usr/ucb/compress reference to /usr/bin/compress

* Mon Mar 17 1997 Erik Troan <ewt@redhat.com>
- Removed inews.1 from main inn package (it's still in the inews packaeg)
- Fixed references to /usr/spoo in sendbatch
- added "-s -" to crosspost line in newsfeeds
- /var/lib/news/active.time is now created as news.news
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are mode 0440 
- included a better rc script which does a better job of shutting down news
- updated /etc/rc.d/rc.news output look like the rest of our initscripts
- hacked sendbatch df stuff to work on machines w/o a separate /var/spool/news

* Tue Mar 11 1997 Erik Troan <ewt@redhat.com>
- added chmod to make sure rnews is 755
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are news.news not root.news
  or root.root
- install an empty /var/lib/news/.news.daily as a config file
- added dbz/dbz.h as /usr/include/dbz.h
- added /usr/bin/inews link to /usr/lib/news/inews
- changed INEWS_PATH to DONT -- I'm not sure this is right though
- turned off MMAP_SYNC
- added a ton of man pages which were missing from the filelist
- increased CLIENT_TIMEOUT to (30 * 60)
- added a postinstall to create /var/lib/news/active.times if it doesn't
  already exist
- patched rc.news to start inn w/ -L flag
- pulled news.init into a separate source file rather then creating it through
  a patch
- added /etc/rc.d/rc5.d/S95news to the file list
- remove pid files from /var/lock/news/* on shutdown
- use /var/lock/subsys/news rather then /var/lock/subsys/inn or things
  don't shutdown properly

* Mon Mar 10 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- changed devel package description to include tin.
- the devel package missed libinn.h
- moved libinn.3 man-page to the devel package
- moved changelog up
- in %post some echo statements were messed up. if we put the redirection
  staements in a different line than the echo command we really should use
  a backslash to thell the shell :-)
- in %install a chmod line referenced the same directory twice.
- changed inn-1.5.1-redhat.patch: The patch for news.daily had a side effect.
  as EXPIREOVERFLAGS was set to '-a', expireover would break if there were
  articles to be removed, as '-a' can't be used if '-z' is specified...
  Now there is a separate 'eval expireover -a' after the first eval. Dirty
  but works.

* Wed Feb 26 1997 Erik Troan <ewt@redhat.com>
- Added a /usr/bin/rnews symlink to /usr/lib/news/rnews as other programs like
  to use it.

* Tue Feb 25 1997 Elliot Lee <sopwith@cuc.edu>
- Fixed rnews path in /etc/cron.daily/inn-cron-rnews
- Added overview! and crosspost lines to /etc/news/newsfeeds
- Fixed nntpsend.ctl path in /usr/lib/news/bin/nntpsend, and set a saner
  nntpsend.ctl config file.
- Added automated inn.conf 'server: ' line creation in %post
- Added misc. patches from ftp.isc.org/isc/inn/unoff-patches/1.5
- Removed -lelf from config.data LIBS
- Made RPM_OPT_FLAGS work.
- Bug in rpm meant that putting %post after %files made it not run. Moved
  %post up.
- Added /etc/cron.hourly/inn-cron-nntpsend to send news every hour.
- Fixed most of the misc permissions/ownership stuff that inncheck
  complained about.

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Incorporated changes from <drdisk@tilx01.ti.fht-esslingen.de> which fixed
  some paths and restored the cron jobs which disappeared in the 1.5.1
  switch. He also made the whole thing use a buildroot and added some files
  which were missing from the file list.

/* configuration file - precompile options */
#define USE_NET
#undef BG_ON_START
#define GTK_1_1
#undef GTKEDITOR_PATCH

/* F keys bindings, usualy from 65470 to 65480 */
#define F_KEYS /* enable key bindings */
#ifdef GDK_F1
#define F1 GDK_F1
#define F2 GDK_F2
#define F3 GDK_F3
#define F4 GDK_F4
#define F5 GDK_F5
#define F6 GDK_F6
#define F7 GDK_F7
#define F8 GDK_F8
#define F9 GDK_F9
#define F10 GDK_F10
#define F11 GDK_F11
#else
#define F1 65470
#define F2 65471
#define F3 65472
#define F4 65473
#define F5 65474
#define F6 65475
#define F7 65476
#define F8 65477
#define F9 65478
#define F10 65479
#define F11 65480
#endif
#undef SHOW_KEY_CODES /* print keys pressed */

/* Highlighting styles */
#define HTML_RED 50
#define HTML_GREEN 50
#define HTML_BLUE 200

#define SH_RED 10
#define SH_GREEN 200
#define SH_BLUE 10

#define ONLY_KEYWORDS

#define HTML_COMMENTS_START "<"
#define HTML_COMMENTS_END ">"
#define HTML_KEYWORDS "JavaScript\\|VBScript"

#define C_COMMENTS_START "/\\*"
#define C_COMMENTS_END "\\*/"
#define C_KEYWORDS "while\\|for\\|if\\|else"

#define PERL_COMMENTS_START "#"
#define PERL_COMMENTS_END "\\n/"
#define PERL_KEYWORDS "print\\|if\\|until\\|elsif\\|else\\|unless\\|while\\|for\\|foreach\\|continue\\|goto\\|last\\|next\\|redo\\|do\\|bless\\|caller\\|import\\|package\\|require\\|return\\|sub\\|tie\\|tied\\|untie\\|use\\|integer\\|abs\\|atan2\\|exp\\|int\\|cos\\|log\\|rand\\|sin\\|sqrt\\|time\\|srand\\|chr\\|gmtime\\|hex\\|ord\\|oct\\|localtime\\|pack\\|vec\\|unpack\\|chomp\\|chop\\|eval\\|index\\|length\\|substr\\|each\\|grep\\|join\\|uc\\|pop\\|shift\\|map\\|split\\|splice\\|read\\|sprintf\\|select\\|write\\|die\\|exec\\|eval\\|dump"

#define JAVA_COMMENTS_START "//"
#define JAVA_COMMENTS_END "\\n/"
#define JAVA_KEYWORDS "abstract\\|boolean\\|break\\|byte\\|byvalue\\|case\\|cast\\|catch\\|char\\|class\\|const\\|continue\\|default\\|do\\|double\\|else\\|extends\\|false\\|final\\|finally\\|float\\|for\\|future\\|generic\\|goto\\|if\\|implements\\|import\\|inner\\|instanceof\\|int\\|interface\\|long\\|native\\|new\\|null\\|operator\\|outer\\|package\\|private\\|protected\\|public\\|rest\\|return\\|short\\|static\\|super\\|switch\\|synchronized\\|this\\|throw\\|throws\\|transient\\|true\\|try\\|var\\|void\\|volatile\\|while"

/* proxy */

#undef USE_SOCKS /* you need to add -lsocks5 to the makefile for this */

/* ftp settings */

#define FTP_USERNAME "anonymous"
#define FTP_PASSWORD "ftpsh@localhost.arpa"

/* international support */

#undef INTERNATIONAL /* set locale */

/* paths */

#define NETSCAPE "/usr/local/bin/netscape -remote"
#define EMACS "/usr/bin/emacs"
#define DES "/bin/des"
#define IDEA "/bin/idea"
#define XTERM "/usr/X11R6/bin/xterm"
#define AWK "awk"
#define SED "sed"
#define VI "/usr/bin/vi"
#define SAY "say"
#define CVS "cvs"
#define GDB "xterm -e gdb"
#define LPR "lpr"
#define XRN "xrn"

/* mail path */

#ifdef __FreeBSD__
#define MAIL_PATH "/var/mail"
#else
#define MAIL_PATH "/var/spool/mail"
#endif

#define _USE_LOCAL_CONFIG



/*
 * Compile Time options
 */
/*
 * Disables ALOT of options below to make the client smaller
 */
/* #undef BITCHX_LITE */

/*
 * Enable LinkLook. This is deprecated as well as dangerous
 */
#define WANT_LLOOK                                        1

/*
 * Enable plugins on supported OS's
 */
#define WANT_DLL                                          1

/*
 * Enable OperView window support
 */
#define WANT_OPERVIEW                                     1

/*
 * Enable builtin cdcc which is a XDCC file offer clone
 */
#define WANT_CDCC                                         1

/*
 * Enable builtin ftp support
 */
#define WANT_FTP                                          1

/*
 * Enable builtin screen utility for /detach
 */
#define WANT_DETACH                                       1

/*
 * Enable epic helpfile support and /ehelp
 */
#define WANT_EPICHELP                                     1

/*
 * Another color option from the dark days of BX.
 */
/* #undef HUMBLE */

/*
 * Xwindows/screen can /window create to create a new "screen"
 */
#define WINDOW_CREATE                                     1

/*
 * Leave this enabled, unless you know it's needed
 */
#define USE_FLOW_CONTROL                                  1

/*
 * Does Ctrl-Z background BX.
 */
#define ALLOW_STOP_IRC                                    1

/*
 * Use only standard chars instead of ibmpc charset
 */
/* #undef ONLY_STD_CHARS */

/*
 * Use only the latin1 charset.
 */
#define LATIN1						1

/*
 * Use the alternate ASCII logos
 */
#define ASCII_LOGO					1

/*
 * Reverse black and white colors for Xterms
 */
/* #undef REVERSE_WHITE_BLACK */

/*
 * If you have trouble with your keyboard, change this
 */
/* #undef EMACS_KEYBINDS */

/*
 * Allow identd faking
 */
#define IDENT_FAKE                                        1

/*
 * Use cidentd .authlie for fake username
 */
#define CIDENTD                                           1

/*
 * Use wdidentd for fake username. Do no enable both cidentd and this
 */
/*
#undef WDIDENT
*/

/*
 * File Globbing support
 */
#define INCLUDE_GLOB_FUNCTION                             1

/*
 * Enable the /exec command
 */
#define EXEC_COMMAND                                      1

/*
 * This disables the dangerous commands, making them unsable
 */
/* #undef PUBLIC_ACCESS */

/*
 * Hebrew Language Support
 */
#define HEBREW                                            1

/*
 * Keyboard Translation tables
 */
#define TRANSLATE                                         1

/*
 *  Support Mirc's Broken resume
 */
#define MIRC_BROKEN_DCC_RESUME                            1

/*
 * Code for performing mode compression on mass mode changes
 */
#define COMPRESS_MODES                                    1

/*
 * Max Number of URLS to save in memory
 */
#define DEFAULT_MAX_URL                                   1

/*
 * Support chatnet's numeric 310
 */
/* #undef WANT_CHATNET */

/*
 * Notify BitchX.com of our version
 */
#define SHOULD_NOTIFY_BITCHX_COM                          1




/*
 * Userlist options
 */
#define DEFAULT_USERLIST                                   1

#define DEFAULT_AOP_VAR                                    0

#define DEFAULT_AINV                                       0

#define DEFAULT_KICK_OPS                                   1

#define DEFAULT_ANNOY_KICK                                 0

#define DEFAULT_LAMELIST                                   1

#define DEFAULT_LAME_IDENT                                 0

#define DEFAULT_SHITLIST                                   1

#define DEFAULT_AUTO_REJOIN                                1

#define DEFAULT_DEOPFLOOD                                  1

#define DEFAULT_DEOPFLOOD_TIME                             30

#define DEFAULT_DEOP_ON_DEOPFLOOD                          3

#define DEFAULT_DEOP_ON_KICKFLOOD                          3

#define DEFAULT_JOINFLOOD                                  1

#define DEFAULT_JOINFLOOD_TIME                             50

#define DEFAULT_KICKFLOOD                                  1

#define DEFAULT_KICKFLOOD_TIME                             30

#define DEFAULT_KICK_ON_KICKFLOOD                          4

#define DEFAULT_KICK_ON_DEOPFLOOD                          3

#define DEFAULT_KICK_ON_JOINFLOOD                          4

#define DEFAULT_NICKFLOOD                                  1

#define DEFAULT_NICKFLOOD_TIME                             30

#define DEFAULT_KICK_ON_NICKFLOOD                          3

#define DEFAULT_PUBFLOOD                                   0

#define DEFAULT_PUBFLOOD_TIME                              20

#define DEFAULT_KICK_ON_PUBFLOOD                           30

#define DEFAULT_KICK_IF_BANNED                             0

/*
 * Values 0 for none, 1 for deop, 2 for announce only
 */
#define DEFAULT_HACKING                                    0

#define DEFAULT_AUTO_UNBAN                                 600




/*
 * Flood options
 */
#define DEFAULT_FLOOD_PROTECTION                           1

#define DEFAULT_CTCP_FLOOD_PROTECTION                      1

#define DEFAULT_CTCP_FLOOD_AFTER                           10

#define DEFAULT_CTCP_FLOOD_RATE                            3

#define DEFAULT_FLOOD_KICK                                 1

#define DEFAULT_FLOOD_RATE                                 5

#define DEFAULT_FLOOD_AFTER                                4

#define DEFAULT_FLOOD_USERS                                10

#define DEFAULT_FLOOD_WARNING                              0

#define DEFAULT_NO_CTCP_FLOOD                              1

#define DEFAULT_CDCC_FLOOD_AFTER                           3

#define DEFAULT_CDCC_FLOOD_RATE                            4

#define DEFAULT_CTCP_DELAY                                 3

#define DEFAULT_CTCP_FLOOD_BAN                             1

#define DEFAULT_VERBOSE_CTCP                               1

#define DEFAULT_CDCC                                       1

#define DEFAULT_IGNORE_TIME                                600




/*
 * DCC options
 */
/*
 * Enable DCC fast support on supported hosts.
 */
#define DEFAULT_DCC_FAST                                   1

#define DEFAULT_DCC_BLOCK_SIZE                             2048

#define DEFAULT_DCC_AUTORENAME                             1

/*
 *  0 for color bargraph, 1 for non-color bar
 */
#define DEFAULT_DCC_BAR_TYPE                               0

#define DEFAULT_DCC_AUTOGET                                0

#define DEFAULT_DCC_GET_LIMIT                              0

#define DEFAULT_DCC_SEND_LIMIT                             5

#define DEFAULT_DCC_QUEUE_LIMIT                            10

#define DEFAULT_DCC_LIMIT                                  10

#define DEFAULT_DCCTIMEOUT                                 600

#define DEFAULT_QUEUE_SENDS                                0

#define DEFAULT_MAX_AUTOGET_SIZE                           2000000




/*
 * Server options
 */
#define DEFAULT_AUTO_AWAY                                  0

#define DEFAULT_SEND_AWAY_MSG                              0

#define DEFAULT_AUTO_AWAY_TIME                             600

#define DEFAULT_AUTO_UNMARK_AWAY                           0

#define DEFAULT_CHANNEL_NAME_WIDTH                         10

#define DEFAULT_SOCKS_PORT                                 1080

#define DEFAULT_NOTIFY                                     1

#define DEFAULT_MAX_SERVER_RECONNECT                       2

#define DEFAULT_CONNECT_TIMEOUT                            30

#define DEFAULT_DISPATCH_UNKNOWN_COMMANDS                  0

#define DEFAULT_NO_FAIL_DISCONNECT                         0

#define DEFAULT_SERVER_GROUPS                              0

#define DEFAULT_WINDOW_DESTROY_PART                        0

#define DEFAULT_SUPPRESS_SERVER_MOTD                       1

#define DEFAULT_AUTO_RECONNECT                             1

#define DEFAULT_SHOW_AWAY_ONCE                             1

#define DEFAULT_SHOW_CHANNEL_NAMES                         1

#define DEFAULT_SHOW_END_OF_MSGS                           0

#define DEFAULT_SHOW_NUMERICS                              0

#define DEFAULT_SHOW_STATUS_ALL                            0

#define DEFAULT_SHOW_WHO_HOPCOUNT                          0

#define DEFAULT_SEND_IGNORE_MSG                            0

#define DEFAULT_HIDE_PRIVATE_CHANNELS                      0

#define IRC_PORT                                           6667

#define DEFAULT_CPU_SAVER_AFTER                            0

#define DEFAULT_CPU_SAVER_EVERY                            0




/*
 * Misc options
 */
/*
 * 0 1 2
 */
#define DEFAULT_PING_TYPE                                  1

/*
 * Which ctcp's do we respond too. 0 all. 1. ping 2. none
 */
#define DEFAULT_CLOAK                                      1

#define DEFAULT_MSGLOG                                     1

#define DEFAULT_AUTO_NSLOOKUP                              0

#define DEFAULT_LLOOK                                      0

#define DEFAULT_LLOOK_DELAY                                120

#define DEFAULT_ALWAYS_SPLIT_BIGGEST                       1

#define DEFAULT_AUTO_WHOWAS                                0

#define DEFAULT_COMMAND_MODE                               0

#define DEFAULT_COMMENT_HACK                               1

#define DEFAULT_DISPLAY                                    1

#define DEFAULT_EIGHT_BIT_CHARACTERS                       1

#define DEFAULT_EXEC_PROTECTION                            1

#define DEFAULT_HIGH_BIT_ESCAPE                            0

#define DEFAULT_HISTORY                                    100

#define DEFAULT_HOLD_MODE                                  0

#define DEFAULT_HOLD_MODE_MAX                              0

#define DEFAULT_LASTLOG                                    1000

#define DEFAULT_LOG                                        0

/*
 *  0 1 2
 */
#define DEFAULT_MAIL                                       2

#define DEFAULT_NOTIFY_ON_TERMINATION                      0

#define DEFAULT_SCROLL_LINES                               1

#define DEFAULT_SHELL_LIMIT                                0

#define DEFAULT_META_STATES                                5

#define DEFAULT_MAX_DEOPS                                  2

#define DEFAULT_MAX_IDLEKICKS                              2

#define DEFAULT_NUM_BANMODES                               4

#define DEFAULT_NUM_KICKS                                  4

#define DEFAULT_NUM_OF_WHOWAS                              4

#define DEFAULT_NUM_OPMODES                                4

#define DEFAULT_HELP_PAGER                                 1

#define DEFAULT_HELP_PROMPT                                1

#define DEFAULT_HELP_WINDOW                                0

#define DEFAULT_FTP_GRAB                                   0

#define DEFAULT_HTTP_GRAB                                  0

#define DEFAULT_NICK_COMPLETION                            1

#define DEFAULT_NICK_COMPLETION_LEN                        2

/*
 *  0 1 2
 */
#define DEFAULT_NICK_COMPLETION_TYPE                       0

#define DEFAULT_FULL_STATUS_LINE                           1

#define DEFAULT_STATUS_NO_REPEAT                           1

#define DEFAULT_DOUBLE_STATUS_LINE                         1

#define DEFAULT_STATUS_DOES_EXPANDOS                       0

#define DEFAULT_OPERVIEW_HIDE                              0

#define DEFAULT_OPER_VIEW                                  0

#define DEFAULT_TAB                                        1

#define DEFAULT_TAB_MAX                                    8

#define DEFAULT_BEEP                                       1

#define DEFAULT_BEEP_MAX                                   3

#define DEFAULT_BEEP_WHEN_AWAY                             0

#define DEFAULT_BOLD_VIDEO                                 1

#define DEFAULT_BLINK_VIDEO                                1

#define DEFAULT_INVERSE_VIDEO                              1

#define DEFAULT_UNDERLINE_VIDEO                            1

#define DEFAULT_CLOCK                                      1

#define DEFAULT_CLOCK_24HOUR                               0

#define DEFAULT_FLOATING_POINT_MATH                        0

#define DEFAULT_INDENT                                     1

#define DEFAULT_INPUT_ALIASES                              0

#define DEFAULT_INSERT_MODE                                1

#define DEFAULT_DISPLAY_ANSI                               1

#define DEFAULT_DISPLAY_PC_CHARACTERS                      4

#define DEFAULT_SCROLLBACK_LINES                           512

#define DEFAULT_SCROLLBACK_RATIO                           50

#define DEFAULT_ND_SPACE_MAX                               160





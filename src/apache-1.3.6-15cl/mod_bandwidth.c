/* ====================================================================
 * Copyright (c) 1995 The Apache Group.  All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer. 
 *
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in
 *    the documentation and/or other materials provided with the
 *    distribution.
 *
 * 3. All advertising materials mentioning features or use of this
 *    software must display the following acknowledgment:
 *    "This product includes software developed by the Apache Group
 *    for use in the Apache HTTP server project (http://www.apache.org/)."
 *
 * 4. The names "Apache Server" and "Apache Group" must not be used to
 *    endorse or promote products derived from this software without
 *    prior written permission.
 *
 * 5. Redistributions of any form whatsoever must retain the following
 *    acknowledgment:
 *    "This product includes software developed by the Apache Group
 *    for use in the Apache HTTP server project (http://www.apache.org/)."
 *
 * THIS SOFTWARE IS PROVIDED BY THE APACHE GROUP ``AS IS'' AND ANY
 * EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE APACHE GROUP OR
 * IT'S CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 * NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 * STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 * ====================================================================
 *
 * This software consists of voluntary contributions made by many
 * individuals on behalf of the Apache Group and was originally based
 * on public domain software written at the National Center for
 * Supercomputing Applications, University of Illinois, Urbana-Champaign.
 * For more information on the Apache Group and the Apache HTTP server
 * project, please see <http://www.apache.org/>.
 *
 */

/****************************************************************************
 * Title       : Bandwidth management
 * File        : mod_bandwidth.c
 * Author      : Yann Stettler (stettler@cohprog.com)
 * Date        : 19 June 98
 * Version     : 1.2 for Apache 1.3.0
 *
 * Description :
 *   Provide bandwidth usage limitation either on the whole server or
 *   one a per connection basis based on the size of files, directory
 *   location or remote domain/IP.
 *
 * Revision    : 08/04/97 - "-1" value for LargeFileLimit to disable any
 *                          limits for that kind of files.
 *               01/26/98 - Include in_domain() and in_ip() in this file and
 *                          make them static so it will work with Apache 1.3x
 *               03/29/98 - Change to set bandwidth in VirtualHost directive
 *
 ***************************************************************************
 * Copyright (c)1997 Yann Stettler and CohProg SaRL. All rights reserved.
 * Written for the Apache Group by :
 *
 * Yann Stettler
 * stettler@cohprog.com
 * http://www.cohprog.com/
 * http://www.animanga.com/
 *
 * Based on the original default_handler module and on bw_module 0.2 from
 * Etienne BERNARD (eb@via.ecp.fr) at VIA Centrale Reseaux, ECP, France
 * 
 * Many thanks to Colba Net Inc (Montreal) for their sponsoring of 
 * improvements to this module.
 *
 ***************************************************************************/


/*
 * Instruction :
 * -------------
 *
 * Note : this module was writen for Apache 1.2b7 and tested on it
 *
 * Installation :
 *
 * 1) Insert the following line at the end of the "Configuration" file :
 *    Module bandwidth_module      mod_bandwidth.o
 *
 * 2) Run the "Configure" program and re-compile the server with "make".
 *
 * 3) Create the following directories with "rwx" permission to everybody :
 *    /tmp/apachebw
 *    /tmp/apachebw/link
 *    /tmp/apachebw/master
 *
 * Note that if any of those directories doesn't exist, or if they can't
 * be accessed by the server, the module is totaly disabled except for
 * logging an error message in the logfile.
 *
 * Server configuration directive :
 * --------------------------------
 *
 * -  BandWidthModule 
 *    Syntax  : BandWidthModule <On|Off>
 *    Default : Off
 *    Context : per server config
 *
 *    Enable or disable totaly the whole module. By default, the module is
 *    disable so it is safe to compile it in the server anyway.
 *
 * Directory / Server / Virtual Server configuration directive :
 * -------------------------------------------------------------
 *
 * -  BandWidth
 *    Syntax  : BandWidth <domain|ip|all> <rate>
 *    Default : none
 *    Context : per directory, .htaccess
 *
 *    Limit the bandwidth for files in this directory and
 *    sub-directories based on the remote host <domain> or
 *    <ip> address or for <all> remote hosts.
 *
 *    The <rate> is in Bytes/second.
 *    A <rate> of "0" means no bandwidth limit.
 *
 *    Several BandWidth limits can be set for the same
 *    directory to set different limits for different
 *    hosts. In this case, the order of the "BandWidth"
 *    keywords is important as the module will take the
 *    first entry which matches the client address.
 *
 *    Example :
 *       <Directory /home/www>
 *       BandWidth ecp.fr 0
 *       BandWidth 138.195 0
 *       BandWidth all 1024
 *       </Directory>
 *
 *      This will limit the bandwith for directory /home/www and 
 *      all it's subdirectories to 1024Bytes/sec, except for 
 *      *.ecp.fr or 138.195.*.* where no limit is set.
 *
 * -  LargeFileLimit
 *    Syntax  : LargeFileLimit <filesize> <rate>
 *    Default : none
 *    Context : per directory, .htaccess
 *
 *    Set a maximal <rate> (in bytes/sec) to use when transfering
 *    a file of <filesize> KBytes or more.
 *
 *    Several "LargeFileLimit" can be set for various files sizes
 *    to create range. The rate used for a given file size will be
 *    the one of the matching range.
 *
 *    A <rate> of "0" mean that there isn't any limit based on
 *    the size.
 *
 *    A <rate> of "-1" mean that there isn't any limit for that type
 *    of file. It's override even a BandWidth limit. I found this usefull
 *    to give priority to very small files (html pages, very small pictures)
 *    while seting limits for larger files... (users with their video files
 *    can go to hell ! :)
 *
 *    Example :
 *    If the following limits are set :
 *       LargeFileLimit 200 3072
 *       LargeFileLimit 1024 2048
 *
 *       That's mean that a file of less than 200KBytes won't be
 *       limited based on his size. A file with a size between
 *       200KBytes (included) and 1023Kbytes (included) will be
 *       limited to 3072Bytes/sec and a file of 1024Kbytes or more
 *       will be limited to 2048Bytes/sec.
 *
 * -  MinBandWidth
 *    Syntax  : MinBandWidth <domain|ip|all> <rate>
 *    Default : all 256
 *    Context : per directory, .htaccess
 *
 *    Set a minimal bandwidth to use for transfering data. This
 *    over-ride both BandWidth and LargeFileLimit rules as well
 *    as the calculated rate based on the number of connections.
 *
 *    The first argument is used in the same way as the first
 *    argument of BandWidth.
 *
 *    <rate> is in bytes per second.
 *
 *    A rate of "0" explicitly means to use the default minimal
 *    value (256 KBytes/sec).
 *
 *    A rate of "-1" means that the minimal rate is equal to the
 *    actual rate defined by BandWidth and LargeFileLimit.
 *    In fact, that means that the final rate won't depend
 *    of the number of connections but only on what was defined.
 *
 *    Example :
 *    If BandWidth is set to "3072" (3KBytes/sec) and MinBandWidth
 *    is set to "1024" (1KBytes/sec) that means :
 *       - if there is one connection, the file will be transfered
 *         at 3072 Bytes/sec.
 *       - if there is two connections, each files will be transfered
 *         at 1536 Bytes/sec. 
 *       - if there is three or more connections, each files will be
 *         transfered at 1024 Bytes/sec. (Minimal of 1024 Bytes/sec).
 *
 *    If MinBandWidth is set to "-1" that means :
 *       - if there is one connection, the file will be transfered
 *         at 3072 Bytes/sec.
 *       - if there is two or more connections, each files will be
 *         transfered at 3072 Bytes/sec. In effect, the rate doesn't
 *         depend anymore on the number of connections but only on
 *         the configuration values.
 *
 *    Note that the total transfer rate will never exceed your physical
 *    bandwidth limitation.
 *
 * Note : If both a "BandWidth" and a "LargeFileLimit" limit apply,
 *        the lowest one will be used. (But never lower than the
 *        "MinBandWidth" rate)
 *
 *        If both a virtual server limit is defined and another
 *        apply for a directory under this virtual server, the
 *        directory limit will over-ride it.
 *
 *        If a limit is defined outside a Directory or VirtualHost
 *        directive, it will act as default on a per virtual server
 *        basis. (Ie: each virtual server will have that limit,
 *        _independantly_ of the other servers)
 *
 * Implementation notes :
 * ----------------------
 * 
 * 1) This module isn't called when serving a cgi-script. In this
 *    case, it's the functions in mod_cgi.c that handle the connection.
 *
 *    That's not a bug : I didn't want to change the cgi_module and
 *    I was too lazy to do it anyway.
 *
 * 2) The rate of data transmission is only calculated. It isn't
 *    measured. Which mean that this module calculates the final
 *    rate that should apply for a file and simply divides this
 *    number by the number of actual connections subject to the
 *    same "per directory" directives.
 * 
 * 3) On the "+" side, the module regulate the speed taking
 *    into account the actual time that was needed to send the
 *    data. Which also mean that if data are read by the client
 *    at a slowest rate than the limit, no time will be lost and
 *    data will be sent as fast as the client can read them (but
 *    no faster than the limited rate :) ...
 *
 * 4) Some kind of buffering is done as side effect. Data are
 *    sent in packet of 1024 KBytes which seems a good value
 *    for TCP/IP.
 *    If another packet size is wanted, change the value of
 *    "#define PACKET" in the codes bellow.
 *
 * 5) The default value for MinBandWidth is defined by :
 *    "#define MIN_BW_DEFAULT" (in Bytes/sec)
 *
 * 6) Don't define "BWDEBUG" for a production server :
 *    this would log a _lot_ of useless informations for
 *    debuging purpose.
 *
 */

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <sys/mman.h>

#define CORE_PRIVATE

#include "ap_mmn.h"
#include "httpd.h"
#include "http_config.h"
#include "http_log.h"
#include "http_protocol.h"
#include "http_request.h"
#include "http_core.h"

#define MIN_BW_DEFAULT  256        /* Minimal bandwidth defaulted to 256Bps */
#define PACKET 1024                /* Sent packet of 1024 bytes             */

#define MASTER_DIR  "/tmp/apachebw/master"
#define LINK_DIR    "/tmp/apachebw/link"

#ifdef USE_MMAP_FILES
#include <unistd.h>
#include <sys/mman.h>

/* Define BWDEBUG for debuging purpose only ! */
/* #define BWDEBUG */
#ifdef BWDEBUG
#undef BWDEBUG
#endif 

#define BANDWIDTH_DISABLED             1<<0
#define BANDWIDTH_ENABLED              1<<1

/* mmap support for static files based on ideas from John Heidemann's
 * patch against 1.0.5.  See
 * <http://www.isi.edu/~johnh/SOFTWARE/APACHE/index.html>.
 */

/* Files have to be at least this big before they're mmap()d.  This is to
 * deal with systems where the expense of doing an mmap() and an munmap()
 * outweighs the benefit for small files.
 */
#ifndef MMAP_THRESHOLD
#ifdef SUNOS4
#define MMAP_THRESHOLD          (8*1024)
#else
#define MMAP_THRESHOLD          0
#endif
#endif
#endif

/* Limits for bandwidth and minimal bandwidth based on directory */
typedef struct {
  char *from;
  long rate;
} bw_entry;

/* Limits for bandwidth based on file size */
typedef struct {
  long size;
  long rate;
} bw_sizel;

/* Per directory configuration structure */
typedef struct {
  array_header *limits;
  array_header *minlimits;
  array_header *sizelimits;
  char  *directory;
} bandwidth_config;

/* Per server configuration structure */
typedef struct {
  int   state;
} bandwidth_server_config;

int bw_handler (request_rec *);

module MODULE_VAR_EXPORT bandwidth_module;

/***************************************************************************
 * Configuration functions                                                 *
 ***************************************************************************/

void *create_bw_config(pool *p, char *path) {
  bandwidth_config *new=
	(bandwidth_config *) ap_palloc(p, sizeof(bandwidth_config));
  new->limits=ap_make_array(p,20,sizeof(bw_entry));
  new->minlimits=ap_make_array(p,20,sizeof(bw_entry));
  new->sizelimits=ap_make_array(p,10,sizeof(bw_sizel));
  new->directory=ap_pstrdup(p, path);
  return (void *)new; 
}

void *create_bw_server_config(pool *p, server_rec *s) {
  bandwidth_server_config *new;

  new = (bandwidth_server_config *)ap_pcalloc(p, sizeof(bandwidth_server_config));

  new->state = BANDWIDTH_DISABLED;

  return (void *)new;
}

/***************************************************************************
 * Directive functions                                                     *
 ***************************************************************************/

const char *bandwidthmodule(cmd_parms *cmd, bandwidth_config *dconf, int flag) {
   bandwidth_server_config *sconf;

   sconf = (bandwidth_server_config *)ap_get_module_config(cmd->server->module_config, &bandwidth_module);
   sconf->state = (flag ? BANDWIDTH_ENABLED : BANDWIDTH_DISABLED);

   return NULL;
}

const char *bandwidth(cmd_parms *cmd, void *s, char *from, char *bw) {
  bandwidth_config *conf=(bandwidth_config *)s;
  bw_entry *a;
  long int temp;

  if (bw && *bw && isdigit(*bw))
    temp = atol(bw);
  else
    return "Invalid argument";

  if (temp<0)
    return "BandWidth must be a number of bytes/s";

  a = (bw_entry *)ap_push_array(conf->limits);
  a->from = ap_pstrdup(cmd->pool,from);
  a->rate = temp;
  return NULL;
}

const char *minbandwidth(cmd_parms *cmd, void *s, char *from, char *bw) {
  bandwidth_config *conf=(bandwidth_config *)s;
  bw_entry *a;
  long int temp;

  if (bw && *bw && (*bw=='-' || isdigit(*bw)))
    temp = atol(bw);
  else
    return "Invalid argument";

  a = (bw_entry *)ap_push_array(conf->minlimits);
  a->from = ap_pstrdup(cmd->pool,from);
  a->rate = temp;
  return NULL;
}

const char *largefilelimit(cmd_parms *cmd, void *s, char *size, char *bw) {
  bandwidth_config *conf=(bandwidth_config *)s;
  bw_sizel *a;
  long int temp, tsize;

  if (bw && *bw && (*bw=='-' || isdigit(*bw)))
    temp = atol(bw);
  else
    return "Invalid argument";

  if (size && *size && isdigit(*size))
    tsize = atol(size);
  else
    return "Invalid argument";

  /*
  if (temp<0)
    return "BandWidth must be a number of bytes/s";
  */

  if (tsize<0)
    return "File size must be a number of Kbytes";

  a = (bw_sizel *)ap_push_array(conf->sizelimits);
  a->size = tsize;
  a->rate = temp;
  return NULL;
}

command_rec bw_cmds[] = {
{ "BandWidth", bandwidth, NULL, RSRC_CONF | OR_LIMIT, TAKE2,
    "a domain (or ip, or all for all) and a bandwidth limit (in bytes/s)" },
{ "MinBandWidth", minbandwidth, NULL, RSRC_CONF | OR_LIMIT, TAKE2,
    "a domain (or ip, or all for all) and a minimal bandwidth limit (in bytes/s)" },
{ "LargeFileLimit", largefilelimit, NULL, RSRC_CONF | OR_LIMIT, TAKE2,
    "a filesize (in Kbytes) and a bandwidth limit (in bytes/s)" },
{ "BandWidthModule",   bandwidthmodule,  NULL, OR_FILEINFO, FLAG, 
      "On or Off to enable or disable (default) the whole bandwidth module" },
{ NULL }
};

/***************************************************************************
 * Internal functions                                                      *
 ***************************************************************************/

#ifdef USE_MMAP_FILES
struct mmap {
    void *mm;
    size_t length;
};

static void mmap_cleanup (void *mmv)
{
    struct mmap *mmd = mmv;

    munmap(mmd->mm, mmd->length);
}
#endif

static int in_domain(const char *domain, const char *what) {
    int dl=strlen(domain);
    int wl=strlen(what);

    if((wl-dl) >= 0) {
        if (strcasecmp(domain,&what[wl-dl]) != 0) return 0;

        /* Make sure we matched an *entire* subdomain --- if the user
         * said 'allow from good.com', we don't want people from nogood.com
         * to be able to get in.
         */

        if (wl == dl) return 1; /* matched whole thing */
        else return (domain[0] == '.' || what[wl - dl - 1] == '.');
    } else
        return 0;
}

static int in_ip(char *domain, char *what) {

    /* Check a similar screw case to the one checked above ---
     * "allow from 204.26.2" shouldn't let in people from 204.26.23
     */
    
    int l = strlen(domain);
    if (strncmp(domain,what,l) != 0) return 0;
    if (domain[l - 1] == '.') return 1;
    return (what[l] == '\0' || what[l] == '.');
}

static int is_ip(const char *host)
{
    while ((*host == '.') || isdigit(*host))
        host++;
    return (*host == '\0');
}

long get_bw_rate(request_rec *r, array_header *a) {
  bw_entry *e = (bw_entry *)a->elts;
  const char *remotehost = NULL;
  int i;

  for (i=0; i< a->nelts; i++) {
    if (!strcmp(e[i].from,"all"))
      return e[i].rate;
    remotehost = ap_get_remote_host(r->connection, r->per_dir_config,
                                 REMOTE_HOST);
    if ((remotehost==NULL) || is_ip(remotehost)) {
      if (in_ip(e[i].from, r->connection->remote_ip))
	return e[i].rate;
    }
    else {
      if (in_domain(e[i].from,remotehost))
	return e[i].rate;
    }
  }
  return 0;
}

long get_bw_filesize(request_rec *r, array_header *a, off_t filesize) {
  bw_sizel *e = (bw_sizel *)a->elts;
  int i;
  long int tmpsize=0, tmprate=0;

  if (!filesize)
    return(0);
 
  filesize /= 1024;

  for (i=0; i< a->nelts; i++) {
    if (e[i].size <= filesize )
       if (tmpsize <= e[i].size) {
          tmpsize=e[i].size;
          tmprate=e[i].rate;
       }
  }

  return(tmprate);
}

int current_connection(char *filename) {
   struct stat mdata;

   /*
    * Here, we will do the main work. And that won't take
    * long !
    */

    if (stat(filename, &mdata) < 0) 
       return(1);   /* strange... should not occure */

    return(mdata.st_nlink-1);

    /*
     * I told you it wouldn't be long... :)
     */
}

struct timeval timediff(struct timeval *a, struct timeval *b)
{
   struct timeval rslt, tmp;

   tmp=*a;
  
   if ((rslt.tv_usec = tmp.tv_usec - b->tv_usec) < 0) {
      rslt.tv_usec += 1000000;
      --(tmp.tv_sec);
   }
   if ((rslt.tv_sec = tmp.tv_sec - b->tv_sec) < 0) {
      rslt.tv_usec=0;
      rslt.tv_sec=0;
   }
   return(rslt);
}

/***************************************************************************
 * Main function, module core                                              *
 ***************************************************************************/

int handle_bw(request_rec *r) {
  int rangestatus, errstatus;
  FILE *f;
  bandwidth_config *conf =
     (bandwidth_config *)ap_get_module_config(r->per_dir_config, &bandwidth_module);
  bandwidth_server_config *sconf =
     (bandwidth_server_config *)ap_get_module_config(r->server->module_config, &bandwidth_module);
  long int bw_rate=0, bw_min=0, bw_f_rate=0, cur_rate;
  int bwlast=0, fd;
  long int tosend, bytessent, filelength;
  struct stat fdata;
  struct timeval opt_time, last_time, now, timespent, timeout;
  char masterfile[128], filelink[128], *directory;

#ifdef USE_MMAP_FILES
    caddr_t mm;
#endif

  /* This handler has no use for a request body (yet), but we still
   * need to read and discard it if the client sent one.
   */
  if ((errstatus = ap_discard_request_body(r)) != OK)
      return errstatus;

  /* Return as fast as possible if request is not a GET or if module not
     enabled */
  if (r->method_number != M_GET || sconf->state == BANDWIDTH_DISABLED)
     return DECLINED;

  if (!conf->directory) {
     directory=ap_document_root(r);
  } else {
     directory=conf->directory;
  }

  bw_rate=get_bw_rate(r,conf->limits);
  bw_min=get_bw_rate(r, conf->minlimits);
  bw_f_rate=get_bw_filesize(r, conf->sizelimits , r->finfo.st_size);

  if ((bw_rate==0 && bw_f_rate==0) || bw_f_rate < 0 || !directory) return DECLINED;

  if (r->finfo.st_mode == 0 || (r->path_info && *r->path_info)) {
      ap_log_reason("File does not exist", r->filename, r);
      return NOT_FOUND;
  }

  ap_update_mtime (r, r->finfo.st_mtime);
  ap_set_last_modified(r);
  ap_set_etag(r);
  if (((errstatus = ap_meets_conditions(r)) != OK)
      || (errstatus = ap_set_content_length (r, r->finfo.st_size))) {
          return errstatus;
  }

  /* 
   * Create name of the master file.
   * Will use the inode and device number of the "limited"
   * directory.
   */

  if (stat(directory, &fdata) < -1) {
     /* Dunno if this may happen... but well... */
     return DECLINED;
  }
  sprintf(masterfile,"%s/%d:%ld",  MASTER_DIR, (short int)fdata.st_dev, (long int)fdata.st_ino);

  /*
   * Check if master file already exist, else create it.
   * Then we create a hardlink to it using the pid as name.
   */
  if ((fd=open(masterfile, O_RDONLY|O_CREAT, 0777)) < 0) {
     ap_log_printf(r->server, "mod_bandwidth : Can't create/access master file %s",masterfile);
     return DECLINED;
  }
  close(fd);

  sprintf(filelink,"%s/%d", LINK_DIR, getpid());
  if (link(masterfile, filelink) < 0) {
     ap_log_printf(r->server, "mod_bandwidth : Can't create hard link %s", filelink);
     return DECLINED;
  }

  f = ap_pfopen(r->pool, r->filename,"r");

  if (f == NULL) {
     ap_log_error(APLOG_MARK, APLOG_ERR, r->server,
                "file permissions deny server access: %s", r->filename);
     return FORBIDDEN;
  }

  /*
   * Calculate bandwidth for this file based on location limits and
   * file size limit.
   *
   * The following rules applies :
   * 1) File size limit over-rule location limit if it's slower.
   * 2) Whatever the resuling limit and number of connections, never
   *    go bellow the minimal limit for this location.
   * 3) A file size limit of zero mean that we don't care about the
   *    size of the file for this purpose.
   *
   */

#ifdef BWDEBUG
  ap_log_printf(r->server, "mod_bandwidth : Directory : %s Rate : %d Minimum : %d Size rate : %d", directory, bw_rate, bw_min, bw_f_rate);
#endif

  if (bw_f_rate && (bw_rate > bw_f_rate || !bw_rate))
      bw_rate=bw_f_rate;

  if (bw_min < 0)
     bw_min=bw_rate;
  else if (! bw_min)
     bw_min=MIN_BW_DEFAULT;

#ifdef USE_MMAP_FILES
  ap_block_alarms();
  if ((r->finfo.st_size >= MMAP_THRESHOLD)
      && ( !r->header_only)) {
    /* we need to protect ourselves in case we die while we've got the
       * file mmapped */
      mm = mmap (NULL, r->finfo.st_size, PROT_READ, MAP_PRIVATE,
                  fileno(f), 0);
  } else {
      mm = (caddr_t)-1;
  }

  if (mm == (caddr_t)-1) {
      ap_unblock_alarms();

      if (r->finfo.st_size >= MMAP_THRESHOLD) {
          ap_log_error(APLOG_MARK, APLOG_CRIT, r->server,
                      "mmap_handler: mmap failed: %s", r->filename);
      }
#endif

  rangestatus = ap_set_byterange(r);
  ap_send_http_header(r);
 
  if (!r->header_only) {
      if (!rangestatus) {
          filelength=r->finfo.st_size;
          bytessent=0;
          bwlast=0;
          while(!bwlast) {
             tosend=PACKET;
             if (tosend+bytessent >= filelength) {
                tosend=filelength-bytessent;
                bwlast=1;
             }

             cur_rate=(long int)bw_rate / current_connection(masterfile);
             if (cur_rate < bw_min)
                cur_rate=bw_min;

#ifdef BWDEBUG
             ap_log_printf(r->server, "mod_bandwidth : Current rate : %d [%d/%d] Min : %d",
                cur_rate, bw_rate, current_connection(masterfile), bw_min);
#endif
             /*
              * I feel rather foolish to use select and use the 
              * 1/1000000 of sec for my calculation. But as long as I
              * am at it, let's do it well...
              *
              * Note that my loop don't take into account the time
              * spent outside the send_fd_length function... but in
              * this case, I feel that I have the moral right to do so :)
              */

             opt_time.tv_sec=(long int) PACKET / cur_rate;
             opt_time.tv_usec=(long int)PACKET*1000000/cur_rate-opt_time.tv_sec*1000000;

             gettimeofday(&last_time, (struct timezone *) 0);

             ap_send_fd_length(f, r, tosend);
             bytessent += tosend;
             if (r->connection->aborted)
                break;
             if (!bwlast) {
                /* We sleep... */
                gettimeofday(&now, (struct timezone *) 0);
                timespent=timediff(&now, &last_time);
                timeout=timediff(&opt_time, &timespent);

#ifdef BWDEBUG
                    ap_log_printf(r->server, "mod_bandwidth : Sleep : %ld/%ld (Op time : %ld/%ld Spent : %ld/%ld)",
                      timeout.tv_sec, timeout.tv_usec, opt_time.tv_sec, opt_time.tv_usec,
                      timespent.tv_sec, timespent.tv_usec);
#endif

                select(0, (fd_set *)0, (fd_set *)0, (fd_set *)0, &timeout);
             }
          }
      } else {
          long offset, length;
          while (ap_each_byterange(r, &offset, &length)) {
              fseek(f, offset, SEEK_SET);

              filelength=length;
              bytessent=0;
              bwlast=0;
              while(!bwlast) {
                 tosend=PACKET;
                 if (tosend+bytessent >= filelength) {
                    tosend=filelength-bytessent;
                    bwlast=1;
                 }

                 cur_rate=(long int)bw_rate / current_connection(masterfile);
                 if (cur_rate < bw_min)
                    cur_rate=bw_min;

#ifdef BWDEBUG
                 ap_log_printf(r->server, "mod_bandwidth : Current rate : %d [%d/%d] Min : %d",
                   cur_rate, bw_rate, current_connection(masterfile), bw_min);
#endif
 
                 opt_time.tv_sec=(long int) PACKET / cur_rate;
                 opt_time.tv_usec=(long int)PACKET*1000000/cur_rate-opt_time.tv_sec*1000000;
    
                 gettimeofday(&last_time, (struct timezone *) 0);
   
                 ap_send_fd_length(f, r, tosend);
                 bytessent += tosend;
                 if (r->connection->aborted)
                    break;
                 if (!bwlast) {
                    /* We sleep... */
                    gettimeofday(&now, (struct timezone *) 0);
                    timespent=timediff(&now, &last_time);
                    timeout=timediff(&opt_time, &timespent);

#ifdef BWDEBUG
                    ap_log_printf(r->server, "mod_bandwidth : Sleep : %ld/%ld (Op time : %ld/%ld Spent : %ld/%ld)", 
                      timeout.tv_sec, timeout.tv_usec, opt_time.tv_sec, opt_time.tv_usec,
                      timespent.tv_sec, timespent.tv_usec);
#endif

                    select(0, (fd_set *)0, (fd_set *)0, (fd_set *)0, &timeout);
                 }
              }
          }
      }
  }

#ifdef USE_MMAP_FILES
    } else {
        struct mmap *mmd;

        mmd = ap_palloc (r->pool, sizeof (*mmd));
        mmd->mm = mm;
        mmd->length = r->finfo.st_size;
        ap_register_cleanup (r->pool, (void *)mmd, mmap_cleanup, mmap_cleanup);
        ap_unblock_alarms();

        rangestatus = ap_set_byterange(r);
        ap_send_http_header (r);

        if (!r->header_only) {
           if (!rangestatus) {
              filelength=r->finfo.st_size;
              bytessent=0;
              bwlast=0;
              while(!bwlast) {
                tosend=PACKET;
                if (tosend+bytessent >= filelength) {
                   tosend=filelength-bytessent;
                   bwlast=1;
                }

                cur_rate=(long int)bw_rate / current_connection(masterfile);
                if (cur_rate < bw_min)
                   cur_rate=bw_min;

#ifdef BWDEBUG
             ap_log_printf(r->server, "mod_bandwidth : Current rate : %d [%d/%d] Min : %d",
                cur_rate, bw_rate, current_connection(masterfile), bw_min);
#endif
                /*
                 * I feel rather foolish to use select and use the 
                 * 1/1000000 of sec for my calculation. But as long as I
                 * am at it, let's do it well...
                 *
                 * Note that my loop don't take into account the time
                 * spent outside the send_fd_length function... but in
                 * this case, I feel that I have the moral right to do so :)
                 */

                opt_time.tv_sec=(long int) PACKET / cur_rate;
                opt_time.tv_usec=(long int)PACKET*1000000/cur_rate-opt_time.tv_sec*1000000;

                gettimeofday(&last_time, (struct timezone *) 0);

                ap_send_mmap(mm, r, bytessent, tosend);
                bytessent += tosend;
                if (r->connection->aborted)
                   break;
                if (!bwlast) {
                   /* We sleep... */
                   gettimeofday(&now, (struct timezone *) 0);
                   timespent=timediff(&now, &last_time);
                   timeout=timediff(&opt_time, &timespent);

#ifdef BWDEBUG
                    ap_log_printf(r->server, "mod_bandwidth : Sleep : %ld/%ld (Op time : %ld/%ld Spent : %ld/%ld)",
                      timeout.tv_sec, timeout.tv_usec, opt_time.tv_sec, opt_time.tv_usec,
                      timespent.tv_sec, timespent.tv_usec);
#endif

                   select(0, (fd_set *)0, (fd_set *)0, (fd_set *)0, &timeout);
                }
             }
         } else {
             long offset, length;
             while (ap_each_byterange(r, &offset, &length)) {

                filelength=length;
                bytessent=0;
                bwlast=0;
                while(!bwlast) {
                   tosend=PACKET;
                   if (tosend+bytessent >= filelength) {
                      tosend=filelength-bytessent;
                      bwlast=1;
                   }

                   cur_rate=(long int)bw_rate / current_connection(masterfile);
                   if (cur_rate < bw_min)
                      cur_rate=bw_min;

#ifdef BWDEBUG
                 ap_log_printf(r->server, "mod_bandwidth : Current rate : %d [%d/%d] Min : %d",
                   cur_rate, bw_rate, current_connection(masterfile), bw_min);
#endif
 
                   opt_time.tv_sec=(long int) PACKET / cur_rate;
                   opt_time.tv_usec=(long int)PACKET*1000000/cur_rate-opt_time.tv_sec*1000000;
    
                   gettimeofday(&last_time, (struct timezone *) 0);
   
                   ap_send_mmap(mm, r, offset, tosend);
                   bytessent += tosend;
                   if (r->connection->aborted)
                      break;
                   if (!bwlast) {
                      /* We sleep... */
                      gettimeofday(&now, (struct timezone *) 0);
                      timespent=timediff(&now, &last_time);
                      timeout=timediff(&opt_time, &timespent);

#ifdef BWDEBUG
                    ap_log_printf(r->server, "mod_bandwidth : Sleep : %ld/%ld (Op time : %ld/%ld Spent : %ld/%ld)", 
                      timeout.tv_sec, timeout.tv_usec, opt_time.tv_sec, opt_time.tv_usec,
                      timespent.tv_sec, timespent.tv_usec);
#endif

                      select(0, (fd_set *)0, (fd_set *)0, (fd_set *)0, &timeout);
                   }
                }
            }
        }
    }
    }
#endif

    ap_pfclose(r->pool, f);

    /* Remove the hardlink */
     unlink(filelink);

    return OK;
}

static const handler_rec bw_handlers[] = {
{ "*/*", handle_bw },
{ NULL }
};

module MODULE_VAR_EXPORT bandwidth_module = {
   STANDARD_MODULE_STUFF,
   NULL,                        /* initializer */
   create_bw_config,            /* bw config creater */
   NULL,                        /* bw merger --- default is to override */
   create_bw_server_config,     /* server config */
   NULL,                        /* merge server config */
   bw_cmds,                     /* command table */
   bw_handlers,                 /* handlers */
   NULL,                        /* filename translation */
   NULL,                        /* check_user_id */
   NULL,                        /* check auth */
   NULL,                        /* check access */
   NULL,                        /* type_checker */
   NULL,                        /* fixups */
   NULL                         /* logger */
};

void *mod_bandwidth=&bandwidth_module;
